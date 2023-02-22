import discord
TOKEN = "...." # your bot token.

client = discord.Client(intents=discord.Intents.all()) # create the client, with all intents enabled.

@client.event
async def on_ready(): # when the bot starts up.
  print(f'{client.user} bot is online') # print the name of the bot.

@client.event
async def on_guild_join(self, guild): # when the bot joins a server.
  print(f"Joined {guild.name}!") # print the name of the server.

@client.event
async def on_message(message): # when a message is sent.
  content = message.content.lower() # make the message lowercase.
  if message.author.id == client.user.id: # check if the message is from the bot.
    return # dont do anything if it is.
  if "first" in content: # check if the message contains what you want.
    await message.reply('first reply!') # reply with this.
  elif "second" in content: # a second reply.
    await message.reply('second reply!')

client.run(TOKEN) # run the bot.
