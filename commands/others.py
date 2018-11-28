import re

import discord

from trecognition.pmsaccess import RestrictedCommandAccess

"""
Here is the syntax of all the arguments provided for each command:
command_func(client, sender, message, tag, params, Analysis, *, **)
"""


@RestrictedCommandAccess(['everyone'])
async def help_command(client, sender, message, tag, params, analysis, *args, **kwargs):
    """ The commands have these three args but tag (for pmsaccess compat) is ALWAYS NULL"""
    help_message = "**Aide pour les commandes d'Akara**\n" \
                   "Toutes les commandes du bot commencent avec un `!`:\n\n"
    for i, k in analysis.get_commands().items():
        if await k[0](client, sender, message, test=True):
            help_message += "`!" + i + "` : *" + k[1] + "*\n"
    return await message.channel.send(help_message, delete_after=15)


@RestrictedCommandAccess([420316404881817613, 439740999326105601])
async def presence(client, sender, message, tag, params, *args, **kwargs):
    """ This command is used in order to change the presence of the bot
    The presence message will be the args (provided as string) """
    await client.change_presence(
        status=discord.Status.online,
        afk=False,
        activity=discord.Game(params))
    return await message.channel.send("Je suis maintenant en train de jouer à : `{0}`".format(params), delete_after=15)


@RestrictedCommandAccess([420316404881817613, 439740999326105601])
async def akara_permission_su(client, sender, message, tag, params, analysis, *args, **kwargs):
    """ This commands executes a command for a given user """
    params = re.compile("\s").split(params, 1)
    if params[1][:1] is "!":
        cmd = re.compile("\s").split(params[1][1:], 1)
        if cmd[0] in analysis.get_commands():
            return await analysis.get_commands()[cmd[0]][0](client, message.channel.guild.get_member(int(params[0])),
                                                            message,
                                                            message.channel.guild.get_member(int(params[0])).mention,
                                                            cmd[1] if len(cmd) > 1 else "", analysis)
        else:
            return await message.channel.send("Désolée, la commande que tu essaies d'effectuer n'existe pas...")
    else:
        await message.channel.send("Tu ne peux éxécuter que des commandes !", delete_after=10)


@RestrictedCommandAccess([420316404881817613, 439740999326105601])
async def test_mention_command(client, sender, message, tag, *args, **kwargs):
    await message.channel.send("Command executed in `run-as " + sender.mention + "`")
