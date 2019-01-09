import discord


class ChannelLimitation:

    def __init__(self, channel_type: str, deny_msg="Désolée, tu ne peux pas effectuer une telle action dans `{0} "
                                                   "channel`"):
        """ This class is only used for method decoration.
        This decorator restricts the usage of a given command in a channel type
        (eg command not allowed in DMChannels)

        Channel Types are :
            text
            private
            other
        """
        self.__channel_type = channel_type
        self.__deny = deny_msg

    def __call__(self, func):
        async def ck_channel(client, message, *args, test=False, **kwargs):
            if isinstance(message.channel, discord.abc.PrivateChannel):
                chnl_type = "private"
            elif isinstance(message.channel, discord.TextChannel):
                chnl_type = "text"
            else:
                chnl_type = "other"
            if chnl_type is not self.__channel_type:
                if not test:
                    return await message.channel.send(self.__deny.format(chnl_type))
                return False
            if test:
                return await func(client, message, *args, test=True, **kwargs)
            else:
                return await func(client, message, *args, **kwargs)
        return ck_channel
