import sys
from random import choice

import discord
from discord import Game
from trecognition.tanalysis import Analysis

client = discord.Client()
text_analyser = Analysis(client)


''' These properties are used in order to retrieve the current version of the bot.
Version code can be used in add-ons for example, in order to check if the version is new enough for a feature'''
VERSION = "0.4.3"
VERSION_CODE = 7


@client.event
async def on_ready():
    print('Logged in as :', client.user.name)
    print('Version : ', VERSION)
    print('ID:', client.user.id)
    await client.change_presence(
        status=discord.Status.online,
        afk=False,
        activity=Game(
            name=choice([
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
        )
    )


@client.event
async def on_message(message):
    if message.author.id == 332179155145981965:
        tag = "Père"
    else:
        tag = "<@" + str(message.author.id) + ">"

    if message.author == client.user:
        return

    await text_analyser.perform_analysis(message, tag)


client.run(sys.argv[1])
