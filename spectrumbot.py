import discord
import json

client = discord.Client()

with open('/home/chluebi/Documents/PythonFiles/SpectrumBotv0.0.1/tokens.json') as f:
    tokens = json.load(f)

with open('/home/chluebi/Documents/PythonFiles/SpectrumBotv0.0.1/roles.txt') as f:
    roles = f.read()

rolelist = roles.split('\n')

print(rolelist)


discordtoken = tokens['discord']['token']
prefix = '$$'

def parse(msg):  # parses the received message for better handling
    try:
        return msg.split()
    except TypeError:
        pass

def has_role(generator,checkrole):
    for role in generator:
        if role.name == checkrole:
            return True

    return False

def get_role(generator,checkrole):
    for role in generator:
        if role.name == checkrole:
            return role.id
    return None

@client.event
async def on_ready():
    print('Logged in as ' + client.user.name)
    global server 
    server = client.get_guild(496658459354464276)
    print('Found server: ' + server.name)


@client.event
async def on_message(message):
    global roles
    global rolelist
    msg = parse(message.content[len(prefix):])

    if message.content.startswith(prefix):
        if msg[0] == 'roles':
            send = 'Roles: \n' + roles
            if message.author.dm_channel == None:
                await message.author.create_dm()
            await message.author.dm_channel.send(send)

        if msg[0] == 'iam':
            rest = message.content[len(prefix)+len(msg[0])+1:len(message.content)]
            if not rest in rolelist:
                await message.channel.send('The role *{}* doesn\'t exist (yet).'.format(rest))
                return

            if has_role(message.author.roles,rest):
                await message.channel.send('You already have this role!')
            else:
                role_to_add = get_role(message.channel.guild.roles,rest)
                await message.author.add_roles(server.get_role(role_to_add),reason='iam command')
                await message.channel.send('Gave {} the *{}* role.'.format(message.author.mention,rest))

        if msg[0] == 'iamnot':
            rest = message.content[len(prefix)+len(msg[0])+1:len(message.content)]
            if not rest in rolelist:
                await message.channel.send('The role *{}* doesn\'t exist (yet)'.format(rest))
                return

            if not has_role(message.author.roles,rest):
                await message.channel.send('You don\'t have this role!')
            else:
                role_to_remove = get_role(message.channel.guild.roles,rest)
                await message.author.remove_roles(server.get_role(role_to_remove),reason='iamnot command')
                await message.channel.send('Removed the *{}* role from {}.'.format(rest,message.author.mention))

        if msg[0] == 'addrole':
            if not has_role(message.author.roles,'Admins'):
                await message.channel.send('You don\'t have the permission to do this')
                return

            rest = message.content[len(prefix)+len(msg[0])+1:len(message.content)]
            if rest in rolelist and get_role(server.roles,rest) != None:
                await message.channel.send('This role already exists in the server and in the bot.')
            elif rest in rolelist and get_role(server.roles,rest) == None:
                await message.channel.send('This role existed in the bot but not in the server, added the role to the server.')
                await server.create_role(name=rest,reason='addrole command')
            elif (not rest in rolelist) and get_role(server.roles,rest) != None:
                await message.channel.send('This role existed in the server but not in the bot, added the role to the bot.')
                with open("/home/chluebi/Documents/PythonFiles/SpectrumBotv0.0.1/roles.txt", "a+") as f:
                    f.write(rest + '\n')
                with open('/home/chluebi/Documents/PythonFiles/SpectrumBotv0.0.1/roles.txt') as f:
                    roles = f.read()
                rolelist = roles.split('\n')
                print(rolelist)
            else:
                await server.create_role(name=rest,reason='addrole command')
                with open("/home/chluebi/Documents/PythonFiles/SpectrumBotv0.0.1/roles.txt", "a+") as f:
                    f.write(rest + '\n')
                with open('/home/chluebi/Documents/PythonFiles/SpectrumBotv0.0.1/roles.txt') as f:
                    roles = f.read()
                rolelist = roles.split('\n')
                print(rolelist)
                await message.channel.send('Created the role: *{}*'.format(rest))

                    














client.run(discordtoken)