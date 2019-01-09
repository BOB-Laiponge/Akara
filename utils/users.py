import discord


def get_proper_user(message: discord.Message, user) -> discord.Member:
    """ Returns the User used as executor in the execution of the code"""
    return message.author if user is None else user


def get_proper_user_mention(message: discord.Message, user) -> str:
    """ Returns the mention of the user performing a command / tag """
    if get_proper_user(message, user).id is 332179155145981965:
        return "Père"
    else:
        return get_proper_user(message, user).mention
