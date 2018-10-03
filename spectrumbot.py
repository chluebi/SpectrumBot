import discord
import json

client = discord.Client()

with open('/home/chluebi/Documents/PythonFiles/SpectrumBotv0.0.1/tokens.json') as f:
    tokens = json.load(f)

with open('/home/chluebi/Documents/PythonFiles/SpectrumBotv0.0.1/roles.txt') as f:
    roles = f.read()

print(roles)


discordtoken = tokens['discord']['token']
prefix = '$$'

def parse(msg):  # parses the received message for better handling
    try:
        return msg.split()
    except TypeError:
        pass

@client.event
async def on_ready():
    print('Logged in as ' + client.user.name)
    server = client.get_guild(496658459354464276)
    print('Found server: ' + server.name)


@client.event
async def on_message(message):
    msg = parse(message.content[len(prefix):])

    if message.content.startswith(prefix):
        if msg[0] == 'roles':
            await message.channel.send(roles)





client.run(discordtoken)