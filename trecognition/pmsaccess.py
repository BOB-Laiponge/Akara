class RestrictedCommandAccess:

    def __init__(self, permissions=None, deny_msg="Désolée, tu n'as pas l'autorisation d'effectuer cette action "
                                                  ":confounded:"):
        """ This class is only used for method decoration.
        It checks the permissions of the command and executes the method if permissions are enough. It says that there's
        a problem instead. You can change dynamically the error's message depending of the command, by providing
        a deny_msg argument at init.
        @:param permissions {Array} the permissions required to execute the action
        @:param deny_msg {String} the message which will be send if permissions are not valid

        WARNING:
        You can ONLY decorate methods whose arguments are function(client, message, tag) with this decorator !
        Since VERSION_CODE 5, tag is not necessary and you can add more arguments if needed, args or/and kwargs

        NOTE & WARNING:
        Don't use `@RestrictedCommandAccess(permissions=['everyone'])` for @tags !
        Remove the decorator and the method will be executed faster.
        HOWEVER, THIS USAGE IS MANDATORY FOR COMMANDS (!command)

        Example:

        @RestrictedCommandAccess([123456789123456789, 234567891234567891])
        def some_function(client, message, *):
            pass

        """
        if permissions is None:
            self.pms = ['everyone']
        else:
            self.pms = permissions
        self.deny = deny_msg

    def __call__(self, func):
        async def ck_perm(client, sender, message, *args, test=False, **kwargs):
            for i in sender.roles:
                if self.pms[0] == 'everyone':
                    if not test:
                        return await func(client, sender, message, *args, **kwargs)
                    return True
                elif i.id in self.pms:
                    if not test:
                        return await func(client, sender, message, *args, **kwargs)
                    return True
            if not test:
                return await message.channel.send(self.deny)
            return False
        return ck_perm
