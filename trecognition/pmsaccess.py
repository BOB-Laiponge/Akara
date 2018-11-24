class RestrictedCommandAccess:

    def __init__(self, permissions=None, deny_msg="Désolé, tu n'as pas l'autorisation d'effectuer cette action"):
        """ This class is only used for method decoration.
        It checks the permissions of the command and executes the method if permissions are enough. It says that there's
        a problem instead. You can change dynamically the error's message depending of the command, by providing
        a deny_msg argument at init.
        @:param permissions {Array} the permissions required to execute the action
        @:param deny_msg {String} the message which will be send if permissions are not valid

        WARNING:
        You can ONLY decorate methods whose arguments are function(client, message, tag) with this decorator !

        NOTE:
        Don't use `@RestrictedCommandAccess(permissions=['everyone'])` !
        Remove the decorator and the method will be executed faster """
        if permissions is None:
            self.pms = ['everyone']
        else:
            self.pms = permissions
        self.deny = deny_msg

    def __call__(self, func):
        async def wrapped_f(client, message, tag):
            for i in message.author.roles:
                if self.pms[0] == 'everyone':
                    return await func(client, message, tag)
                elif i.id in self.pms:
                    return await func(client, message, tag)
            return await message.channel.send(self.deny)
        return wrapped_f
