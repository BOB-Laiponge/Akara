from random import randrange, choice

from trecognition.pmsaccess import RestrictedCommandAccess
from utils.channellimitation import ChannelLimitation


async def is_happy(client, message, *args, **kwargs):
    return await message.channel.send("Oh oui ! C'est gentil de t'en inquiéter :relaxed: ")


async def insult(client, message, *args, **kwargs):
    pct_insult = randrange(0, 75)
    if "SALE" in message.content.upper():
        pct_insult += 35
    if "!" in message.content:
        pct_insult += 15
    await message.channel.send("|SYSTEM| : Insulte potentielle détectée\n"
                               "|SYSTEM| : Probabilité : " + str(pct_insult) + "%")
    if pct_insult <= 50:
        return await message.channel.send("|SYSTEM| : Paramètre ACCEPTABLE\n"
                                          "|SYSTEM| : Aucune réponse programmée")
    return await message.channel.send("|SYSTEM| : Paramètre INACCEPTABLE.\n"
                                      "|SYSTEM| : Programmation d'une réponse cinglante.\n"
                                      "Va manger tes morts.")


async def dice_launch(client, message, *args, **kwargs):
    return await message.channel.send("Résultat du jet de dé : " + str(randrange(0, 100)))


@ChannelLimitation("text")
async def order66(client, message, *args, **kwargs):
    list66 = []
    for member in message.channel.guild.members:
        if member.name != message.author.name:
            add = True
            for role in member.roles:
                if role.id == 420316949776564234 or role.id == 420324716105039903:
                    add = False
                    break
            if add:
                list66.append(member.name)
    await message.channel.send("Execution de l'ordre 66")
    while len(list66) > 0:
        player66 = choice(list66)
        list66.remove(player66)
        if str(player66) == "BOB_Laiponge":
            await message.channel.send("`TypeError: User BOB_Laiponge#3011 escaped !`")
        else:
            await message.channel.send(player66 + " : " +
                                       choice(["Eliminé", "Eliminé", "Eliminé", "Eliminé", "Eliminé", "Introuvable"]))
    del list66


async def moral_upper(client, message, *args, **kwargs):
    return await message.channel.send("Voici une vidéo pour te remonter le moral : :smile_cat:\n"
                                      "https://www.youtube.com/")


async def joke_1(client, message, *args, **kwargs):
    return await message.channel.send("Une blague ? C'est parti ! :upside_down:\n"
                                      "*Ceci est une blague qui n'a pas encore été ajoutée…*")


async def joke_2(client, message, *args, **kwargs):
    return await message.channel.send("Une boutade ? J'aime les boutades ! :upside_down:\n"
                                      "*Ceci est une blague qui n'a pas encore été ajoutée…*")


async def q_mark(client, message, *args, **kwargs):
    return await message.channel.send("Est ce que je t'en pose des questions, moi ? ...")


@RestrictedCommandAccess([420316404881817613, 420316949776564234, 439740999326105601])
async def test_stuff(client, message, *args, **kwargs):
    return await message.channel.send("Un test ? Il n'y a pas de test en cours pour le moment ^^")
