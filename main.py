import discord
import os
import pandas as pd

# Set options for printing Df
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

file_path = 'patch13.xlsx'
df = pd.read_excel(file_path)
df = df.reset_index(drop=True)

#create
listRounds = distinct_names = df['round'].unique()
myDict = {}
j = 0
for i in listRounds:
  myDict[j] = str(i)
  j += 1

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('help') or message.content.startswith('info'):
    await message.channel.send(
      "Type list to see all the Ammo Types " + "\n" +
      "Send name or corresponding number to see desired ballistics info")

  if message.content.startswith('list'):
    result_string = ''
    for key, value in myDict.items():
      result_string += f"{key} --- {value}\n"
    await message.channel.send(result_string)

  for key, value in myDict.items():

    if message.content == str(key) or message.content == str(value):
      mask = df['round'] == value
      # Use the boolean mask to filter the DataFrame
      filtered_df = df[mask]
      # Drop the 'round' column
      filtered_df = filtered_df.drop(columns=['round'])
      filtered_df = filtered_df.drop(columns=['Weight'])
      filtered_df = filtered_df.sort_values(by='₽', ascending=True)

      LEN = len(filtered_df)
      await message.channel.send(f'{value.upper()}')
      await message.channel.send(f'```{filtered_df}```')

  # a little troll for nick
  if message.author == "TheEliteSpy":
    await message.channel.send("Nick has a micropenis")


# Start the discord bot
my_secret = 'MTA0OTg5MDIzOTM5MDQzNzQ5Ng.GKHldg.j2E1v5TmVBUupB2TAAhY97ZUbkjPiaL7ZNuz3M'
client.run(my_secret)
