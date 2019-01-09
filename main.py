import sys

import discord
from discord import Game

from database.db import execute_sql
from trecognition.tanalysis import Analysis
from utils.presence import get_random_presence

client = discord.Client()
text_analyser = Analysis(client)

''' These properties are used in order to retrieve the current version of the bot.
Version code can be used in add-ons for example, in order to check if the version is new enough for a feature'''
VERSION = "0.4.5"
VERSION_CODE = 9


@client.event
async def on_ready():
    print('Logged in as :', client.user.name)
    print('Version : ', VERSION)
    print('ID:', client.user.id)
    activity = await execute_sql([
        "SELECT * FROM bot WHERE property='activity'"
    ], 1, client)
    await client.change_presence(
        status=discord.Status.online,
        afk=False,
        activity=Game(
            name=get_random_presence() if activity is None else activity[1]
        )
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await text_analyser.perform_analysis(message)


client.run(sys.argv[1])
