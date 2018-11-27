# Akara #
## What is Akara ? ##
Akara is a simple discord bot which performs all the entertainment commands.
This bot has been coded in Python, using the discord.py library.

## Credits ##
Akara has been created by BOB-Laiponge and is maintained by both BOB-Laiponge and AlbanSdl

## Updating the code ##
Here is the list of all the several changes, in order to provide more efficient and quick updates.
If you modify an important part of the code, please write it down here.

### @RestrictedCommandAccess ###
The Decorator is now **REQUIRED** for all the **COMMANDS**, even if the target is 'everyone' \
However, don't use it for @tags if the target is 'everyone', it will make the bot faster

**Why is the Decorator required for commands ?**\
The decorator helps to determine if the current sender of the command has the permission to execute the command.
It's used in other contexts, for example during the `!help` command execution, which checks if the user is allowed to execute the command before displaying it.

**What's the version in which it has changed ?**
```python
VERSION = "0.4.1"
VERSION_CODE = 5
```