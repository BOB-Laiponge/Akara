import discord

from trecognition.pmsaccess import RestrictedCommandAccess

"""
Here is the syntax of all the arguments provided for each command:
command_func(client, message, tag, params, Analysis, *, **)
"""


@RestrictedCommandAccess(['everyone'])
async def help_command(client, message, tag, params, analysis, *args, **kwargs):
    """ The commands have these three args but tag (for pmsaccess compat) is ALWAYS NULL"""
    help_message = "**Aide pour les commandes d'Akara**\n" \
                   "Toutes les commandes du bot commencent avec un `!`:\n\n"
    for i, k in analysis.get_commands().items():
        if await k[0](client, message, test=True):
            help_message += "`!" + i + "` : *" + k[1] + "*\n"
    return await message.channel.send(help_message)


@RestrictedCommandAccess([420316404881817613, 439740999326105601])
async def presence(client, message, tag, params, *args, **kwargs):
    """ This command is used in order to change the presence of the bot
    The presence message will be the args (provided as string) """
    await client.change_presence(
        status=discord.Status.online,
        afk=False,
        activity=discord.Game(params))
    return await message.channel.send("Je suis maintenant en train de jouer à : `{0}`".format(params))
