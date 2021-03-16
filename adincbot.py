import discord
import config
print(discord.__version__)
client = discord.Client()
message_id = ''
role_name_dictionary = {
        ':fire:': "He/His",
        ':eyes:': "She/Hers",
        ':lightbulb:': "They/Theirs"
    }

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    guild_list = Client.guilds
    adventure_inc = [guild for guild in guild_list if guild.name == "Adventure Incorporated"]
    selected_channel = [channel for channel in adventure_inc.fetch_channels() if channel.name == "bot-testing"]
    # It is possible we could skip the above three lines and simply do the following:
    # selected_channel = discord.utils.find(lambda m: m.name == "bot-testing", Client.guilds.channels)
    # another option could be:
    # selected_channel = discord.utils.get(guild.channels, name="bot-testing")
    # selected_channel = discord.utils.get(Client.guilds[0].channels, name="bot-testing")
    # I'm not sure on these and I can't test them. Here is a link to the part of the documentation I am referencing:
    # https://discordpy.readthedocs.io/en/latest/api.html?highlight=on_reaction#utility-functions
    try:
        await selected_channel.purge()
    except:
        print("Message could not be deleted")
    try:
        #global message_id = await selected_channel.send('Hello! I am here to assist you in selecting a pronoun role. Please react with an emoji below. /n :fire: He/His /n :eyes: She/Hers /n :lightbulb: They/Theirs')
        global message_id = await selected_channel.send('Hello!')
        # I have no idea if this works either. In theory it should, but who knows. My linter is complainging about syntax but I think that's because it doesn't realize this function has a return value of a message.
    except:
        print("Message could not be sent")

@client.event
async def on_reaction_add(reaction, user):
    is_correct_message = (reaction.message.id == message_id)
    if(is_correct_message):
        try:
            role = discord.utils.get(reaction.message.guild.roles, name=role_name_dictionary.get(reaction.emoji))
            await user.add_roles(role)
        except:
            print("Something has gone wrong. Role not added to user.")

@client.event
async def on_reaction_remove(reaction, user):
    is_correct_message = (reaction.message_id == message_id)
    if(is_correct_message):
        try:
            role = discord.utils.get(reaction.message.guild.roles, name=role_name_dictionary.get(reaction.emoji))
            await user.remove_roles(role)
        except:
            print("Something has gone wrong. Role not added to user.")

# @client.event
# async def on_message(message):
# #    print('detected a message')
#     if message.author == client.user:
#         return

#     if message.content.startswith('!assign-role'):
#         role_name = message.content[message.content.find(' ') + 1:].lower()
#         role_name = role_name[0].upper() + role_name[1:]
#         location = role_name.find('/') + 1
#         role_name = role_name[:location] + role_name[location].upper() + role_name[location + 1:]
#         print(role_name)
# #        await message.guild.create_role(name=role_name)

#         try:
#             role = discord.utils.get(message.guild.roles, name=role_name)
#             await message.author.add_roles(role)
#             await message.channel.send('Ok! You are now %s' % role_name)
#         except:
#             await message.channel.send('Sorry, %s is not currently an accepted role, please contact a mod if you feel it should be.' % role_name)

client.run(config.token)
