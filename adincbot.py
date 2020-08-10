import discord
import config
print(discord.__version__)
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
#    print('detected a message')
    if message.author == client.user:
        return

    if message.content.startswith('!assign-role'):
        role_name = message.content[message.content.find(' ') + 1:].lower()
        print(role_name)
#        await message.guild.create_role(name=role_name)

        try:
            role = discord.utils.get(message.guild.roles, name=role_name)
            await message.author.add_roles(role)
            await message.channel.send('Ok! You are now %s' % role_name)
        except:
            await message.channel.send('Sorry, %s is not currently an accepted role, please contact a mod if you feel it should be.' % role_name)

client.run(config.token)
