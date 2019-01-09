from random import randrange

from utils.users import get_proper_user_mention


async def say_hello(client, message, *args, user=None, **kwargs):
    return await message.channel.send("Bonjour " + get_proper_user_mention(message, user)
                                      + ", je suis heureuse de te revoir :grin: ")


async def say_hello_2(client, message, *args, user=None, **kwargs):
    return await message.channel.send("Bonsoir " + get_proper_user_mention(message, user)
                                      + ", je suis heureuse de te revoir :grin: ")


async def say_cc(client, message, *args, user=None, **kwargs):
    return await message.channel.send("Coucou, " + get_proper_user_mention(message, user) + "  :grinning: ")


async def say_hey(client, message, *args, user=None, **kwargs):
    return await message.channel.send("Hey, " + get_proper_user_mention(message, user)
                                      + ", heureuse de te revoir  :grinning: ")


async def say_hi(client, message, *args, user=None, **kwargs):
    return await message.channel.send("Salut, " + get_proper_user_mention(message, user)
                                      + ", j'espère que tu vas bien, aujourd'hui  :grinning: ")


async def say_hello_en(client, message, *args, user=None, **kwargs):
    return await message.channel.send("Hello, " + get_proper_user_mention(message, user)
                                      + ", j'espère que tu vas bien, aujourd'hui  :grinning: ")


async def say_good_night(client, message, *args, user=None, **kwargs):
    return await message.channel.send("Bonne nuit, " + get_proper_user_mention(message, user)
                                      + " :full_moon_with_face: ")


async def say_good_bye(client, message, *args, user=None, **kwargs):
    return await message.channel.send("Au revoir, " + get_proper_user_mention(message, user)
                                      + ", j'espère te revoir très vite :wave: ")


async def say_plus_plus(client, message, *args, user=None, **kwargs):
    return await message.channel.send("++ " + get_proper_user_mention(message, user) + " :wave: ")


async def say_bye(client, message, *args, user=None, **kwargs):
    if randrange(100) > 25:
        return await message.channel.send("Bye " + get_proper_user_mention(message, user) + " :wave: ")
    else:
        await message.channel.send("Désolée, je suis une machine, je ne baille pas...")
        await message.channel.send("Oh... Cette blague ne vous a pas fait rire")
        return await message.channel.send("Diminution du paramètre \"Humour\" à 75%")
