import re

import discord

from database.db import execute_sql, db_escape_string
from trecognition.pmsaccess import RestrictedCommandAccess
from utils.channellimitation import ChannelLimitation
from utils.presence import get_random_presence

"""
Here is the syntax of all the arguments provided for each command:
command_func(client, message, params, Analysis, *, user=discord.User, **)
"""


@RestrictedCommandAccess(['everyone'])
async def help_command(client, message, params, analysis, user=None, *args, **kwargs):
    help_message = "**Aide pour les commandes d'Akara**\n" \
                   "Toutes les commandes du bot commencent avec un `!`:\n\n"
    for i, k in analysis.get_commands().items():
        if await k[0](client, message, test=True, user=user):
            help_message += "`!" + i + "` : *" + k[1] + "*\n"
    return await message.channel.send(help_message, delete_after=15)


@RestrictedCommandAccess([420316404881817613, 439740999326105601])
async def presence(client, message, params, *args, **kwargs):
    """ This command is used in order to change the presence of the bot
    The presence message will be the args (provided as string) """
    if params == "reset":
        params = get_random_presence()
    await client.change_presence(
        status=discord.Status.online,
        afk=False,
        activity=discord.Game(params))
    await execute_sql(["UPDATE bot SET value='" + db_escape_string(params) + "' WHERE property='activity'"], -2, client)
    return await message.channel.send("Je suis maintenant en train de jouer à : `{0}`".format(params), delete_after=15)


@RestrictedCommandAccess([420316404881817613])
async def db(client, message, params, *args, **kwargs):
    """ Database query """
    return await message.channel.send("La commande a bien été éxécutée : " + str(
        await execute_sql([params], 1.0, client, error_channel=message.channel)), delete_after=15)


@ChannelLimitation("text")
@RestrictedCommandAccess([420316404881817613, 439740999326105601])
async def akara_permission_su(client, message, params, analysis, *args, **kwargs):
    """ This commands executes a command for a given user """
    params = re.compile("\s").split(params, 1)
    if params[1][:1] is "!":
        cmd = re.compile("\s").split(params[1][1:], 1)
        if cmd[0] in analysis.get_commands():
            return await analysis.get_commands()[cmd[0]][0](client, message,
                                                            message.channel.guild.get_member(int(params[0])).mention,
                                                            cmd[1] if len(cmd) > 1 else "", analysis,
                                                            user=message.channel.guild.get_member(int(params[0])))
        else:
            return await message.channel.send("Désolée, la commande que tu essaies d'effectuer n'existe pas...")
    elif re.match(r"^.*<@!?" + re.escape(str(client.user.id)) + r">.*$", params[1], re.IGNORECASE | re.UNICODE):
        for regex in analysis.get_regex():
            if re.match(regex, params[1], re.IGNORECASE | re.UNICODE):
                return await analysis.get_regex()[regex](client, message,
                                                         user=message.channel.guild.get_member(int(params[0])))
        await message.channel.send("Désolée, je ne comprend pas. :confounded:")
        return False
    else:
        await message.channel.send("Tu ne peux éxécuter que des commandes ou des tags !", delete_after=10)


@RestrictedCommandAccess([420316404881817613, 439740999326105601])
async def test_mention_command(client, message, user=None, *args, **kwargs):
    await message.channel.send("Command executed in `run-as " + message.author.mention if user is None else
                               user.mention + "`")
