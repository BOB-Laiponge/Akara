from random import randrange


async def say_hello(client, message, tag):
    return await message.channel.send("Bonjour " + tag + ", je suis heureuse de te revoir :grin: ")


async def say_hello_2(client, message, tag):
    return await message.channel.send("Bonsoir " + tag + ", je suis heureuse de te revoir :grin: ")


async def say_cc(client, message, tag):
    return await message.channel.send("Coucou, " + tag + "  :grinning: ")


async def say_hey(client, message, tag):
    return await message.channel.send("Hey, " + tag + ", heureuse de te revoir  :grinning: ")


async def say_hi(client, message, tag):
    return await message.channel.send("Salut, " + tag + ", j'espère que tu vas bien, aujourd'hui  :grinning: ")


async def say_hello_en(client, message, tag):
    return await message.channel.send("Hello, " + tag + ", j'espère que tu vas bien, aujourd'hui  :grinning: ")


async def say_good_night(client, message, tag):
    return await message.channel.send("Bonne nuit, " + tag + " :full_moon_with_face: ")


async def say_good_bye(client, message, tag):
    return await message.channel.send("Au revoir, " + tag + ", j'espère te revoir très vite :wave: ")


async def say_plus_plus(client, message, tag):
    return await message.channel.send("++ " + tag + " :wave: ")


async def say_bye(client, message, tag):
    if randrange(100) > 25:
        return await message.channel.send("Bye " + tag + " :wave: ")
    else:
        await message.channel.send("Désolée, je suis une machine, je ne baille pas...")
        await message.channel.send("Oh... Cette blague ne vous a pas fait rire")
        return await message.channel.send("Diminution du paramètre \"Humour\" à 75%")
