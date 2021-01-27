import discord


class MyClient(discord.Client):
    def __init__(self, intents):
        discord.Client.__init__(self, intents=intents)
        return

    async def on_ready(self):
        print("{} was conntected".format(self.user.name))
        return

    async def on_member_join(self, member):
        guild = self.get_guild(804083891631554580)
        channel = guild.get_channel(804085755906883604)
        await channel.send(":lock:password:lock:", delete_after=10)
        return

    async def on_message(self, message):
        if message.author.id == 804084214978445364:
            return
        if message.channel.id == 804085755906883604:
            if len(message.author.roles) == 1:
                if message.content == "portail inferieur":
                    role = message.guild.get_role(804090037738143774)
                    await message.author.add_roles(role)
                    channel = message.guild.get_channel(804087465987014706)
                    await channel.send(
                        "{}\nBienvenu dans la pim's corporation".format(
                            message.author.mention))
                else:
                    await message.author.kick(reason="Indigne")
            await message.delete()
        return
