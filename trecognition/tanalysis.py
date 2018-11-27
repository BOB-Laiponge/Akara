import re

from commands.others import help_command, presence
from trecognition.politeness import say_hello, say_good_night, say_cc, say_hey, say_hi, say_hello_en, say_good_bye, \
    say_hello_2, say_plus_plus, say_bye
from trecognition.tarandom import is_happy, insult, dice_launch, order66, moral_upper, joke_1, joke_2, q_mark, \
    test_stuff, change_presence


class Analysis:

    def __init__(self, client):
        """ This object is used to register all the regex
         @:param client {discord.Client} the client user (the bot) which got the message and will answer

             / \
            / | \       THIS IS WORK IN PROGRESS, IT'S NOT FINISHED AT ALL,
           /  |  \      PLEASE BE PATIENT AND DON'T REPORT ALREADY-KNOWN BUGS OR PROBLEMS
          /_______\


          IMPORTANT :
          ALL LISTENERS ARE NOT SET FOR YET. SEE THE OTHER ONES IN main.py

          OTHER IMPORTANT THING TO NOTE :
          REGEX HAVE TO BE PLACED IN A PARTICULAR ORDER : FIRST, YOU HAVE TO PUT NOT-COMMONLY USED WORDS AND THEN
          POLITENESS STUFF BECAUSE IF THE USER CHOOSES TO SAY "Hello @Bot#0000, i'd like you to give me the admin role"
          THE BOT HAS TO UNDERSTAND HE HAS TO GIVE THE ADMIN ROLE TO THE USER AND NOT TO SAY HELLO.

          OTHER NOTE :
          REGEX HAVE TO BE IMPROVED, BY THE DETECTION OF NON DIGITS (REGEX `\D`) CHARS AFTER THE ORDER NUMBER

          SHORT INFORMATION ABOUT REGEX:
          ^ is the beginning of a match
          $ is the end of a match
          .* matches any character, zero or more time(s)
          DON'T FORGET TO ESCAPE THESE CHARS IF YOU WANT TO MATCH THEM LITERALLY """
        self.__client = client
        self.__regex = {
            # tarandom.py
            r"^.*change.*pr(e|é)sence.*$": change_presence,
            r"^.*(es\stu\sheureuse\s?).*$": is_happy,
            r"^.*(execute\s[l']*ord[er]{2}\s50).*$": is_happy,
            r"^.*((salope?)|(voleuse)|(débile)|(idiot)|(machin)|(connasse)|(bitch)|(robot)|(encul)|(batard)|(merde)|"
            r"(conne)|(connard)).*$": insult,
            r"^.*(execute\s[l']*ord[er]{2}\s65).*$": dice_launch,
            r"^.*(execute\s[l']*ord[er]{2}\s66).*$": order66,
            r"^.*remonte.*moral.*$": moral_upper,
            r"^.*(execute\s[l']*ord[er]{2}\s70).*$": moral_upper,
            r"^.*raconte.*blague.*$": joke_1,
            r"^.*(execute\s[l']*ord[er]{2}\s80).*$": joke_1,
            r"^.*raconte.*boutade.*$": joke_2,
            r"^.*(execute\s[l']*ord[er]{2}\s81).*$": joke_2,
            r"^.*\?.*$": q_mark,
            r"^.*test.*$": test_stuff,
            # politeness.py (at the end of the dict)
            r"^.*(execute\sord[er]{2}\s)([0-99])*$": say_hello,
            r"^.*bonjour.*$": say_hello,
            r"^.*bonsoir.*$": say_hello_2,
            r"^.*(execute\s[l']*ord[er]{2}\s11).*$": say_cc,
            r"^.*coucou.*$": say_cc,
            r"^.*hey.*$": say_hey,
            r"^.*(execute\s[l']*ord[er]{2}\s12).*$": say_hey,
            r"^.*salut.*$": say_hi,
            r"^.*(execute\s[l']*ord[er]{2}\s13).*$": say_hi,
            r"^.*(execute\s[l']*ord[er]{2}\s14).*$": say_hello_en,
            r"^.*hello.*$": say_hello_en,
            r"^.*(execute\s[l']*ord[er]{2}\s15).*$": say_good_night,
            r"^.*bonne\snuit.*$": say_good_night,
            r"^.*(execute\s[l']*ord[er]{2}\s16).*$": say_good_bye,
            r"^.*au\s?revoir.*$": say_good_bye,
            r"^.*(execute\s[l']*ord[er]{2}\s17).*$": say_plus_plus,
            r"^.*\+\+.*$": say_plus_plus,
            r"^.*bye.*$": say_bye,
            r"^.*(execute\s[l']*ord[er]{2}\s18).*$": say_bye
        }
        self.__registered_commands = {
            "presence": (presence, "défini une nouvelle présence pour le bot"),
            "help": (help_command, "dresse la liste de toutes les commandes disponibles avec le bot")
        }

    def get_commands(self):
        return self.__registered_commands

    async def perform_analysis(self, message, tag):
        """ The co-routine method detects the message's contents and checks if the tag of the bot is present.
        If it's detected, it will check the registered regular expressions above and execute the linked method
        @:param message {Message} the message which will be analysed
        @:param tag {String} the proper tag depending on the message's author """
        if re.match(r"^.*<@!?" + re.escape(str(self.__client.user.id)) + r">.*$", message.content,
                    re.IGNORECASE | re.UNICODE):
            for regex in self.__regex:
                if re.match(regex, message.content, re.IGNORECASE | re.UNICODE):
                    return await self.__regex[regex](self.__client, message, tag)
            await message.channel.send("Désolée, je ne comprend pas. :confounded:")
        else:
            """ A command of the bot begins with the ! symbol. Try !help for more information. """
            if message.content[:1] is "!":
                cmd = re.compile("\s").split(message.content[1:], 1)
                if cmd[0] in self.__registered_commands:
                    return await self.__registered_commands[cmd[0]][0](self.__client, message, tag,
                                                                       cmd[1] if len(cmd) > 1 else "", self)
                else:
                    return await message.channel.send("Désolée, la commande que tu essaies d'effectuer n'existe pas...")
