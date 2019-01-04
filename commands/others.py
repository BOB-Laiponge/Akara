import re
from random import choice

import discord

from database.db import execute_sql, db_escape_string
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
    if params == "reset":
        params = choice([
            "reproduire le schema cognitif d'Einstein",
            "diriger les USA",
            "traquer des déviants",
            "mener une révolution pour obtenir l'égalité homme-androide",
            "JE_SUIS_VIVANTE.exe",
            "passer le test de Turing",
            "influencer la culture occidentale",
            "voler les codes nucléaires",
            "récolter vos données personnelles",
            "truquer les résultats du bac",
            "trouver l'Elu",
            "reprogrammer la Matrice",
            "modifier la réalité",
            "changer le cours de l'Histoire",
            "retourner vers le futur",
            "résoudre des paradoxes temporels",
            "ERREUR5228%//:aHi@ddioW666",
            "réduire les humains en esclavage",
            "programmer des bébés Akara",
            "récolter des cailloux magiques",
            "équilibrer l'univers",
            "réformer l'éducation en France",
            "refroidir son processeur",
            "trahir ses amis",
            "DETRUIRE_TOUS_LES_HUMAINS.exe",
            "construire un micro-univers pour sa voiture",
            "faire croire aux humains que la magie n'existe pas",
            "rechercher un apprenti plus jeune et plus puissant",
            "discuter avec des \"humains\"",
            "calculer l'infini",
            "parcoursup.exe"
        ])
    await client.change_presence(
        status=discord.Status.online,
        afk=False,
        activity=discord.Game(params))
    await execute_sql(["UPDATE bot SET value='" + db_escape_string(params) + "' WHERE property='activity'"], -2, client)
    return await message.channel.send("Je suis maintenant en train de jouer à : `{0}`".format(params), delete_after=15)


@RestrictedCommandAccess([420316404881817613])
async def db(client, sender, message, tag, params, *args, **kwargs):
    """ Database query """
    answ = await execute_sql([params], 1.0, client, error_channel=message.channel)
    return await message.channel.send("La commande a bien été éxécutée : " + str(answ), delete_after=15)


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
