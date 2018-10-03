import discord
import json

client = discord.Client()

with open('/home/chluebi/Documents/PythonFiles/SpectrumBot/tokens.json') as f:
    tokens = json.load(f)

discordtoken = tokens['discord']['token']


print(discordtoken)


client.run(discordtoken)