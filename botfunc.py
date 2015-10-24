import os
import discord
import logging
import datetime
import messageparser

def on_debug(message):
    #STEP 0 - Check permissions (do this later)
    [x for x in range(10)]
    #STEP 1 - remove the !debug from message.content because that's not python code we want to evaluate
    stripped_content = message.content[:len("!debug ")]
    #STEP 2 - send the "cleaned up" message content to python evaluation
    stripped_content = stripped_content.strip()
    result = eval(stripped_content)
    #STEP 3 - send the result to discord
    result = "```Python\n" + result + "\n```"
    client.send_message(message.channel, result)

def on_market(message):
    print('Command not finished.')
    client.send_message(message.channel,'Sorry, This Command is not working properly yet.')

def on_role(message):
    role2 = discord.utils.find(lambda role: role.name == 'Admin', message.channel.server.roles)
    role3 = discord.utils.find(lambda role: role.name == 'Guild Master', message.channel.server.roles)
    role4 = discord.utils.find(lambda role: role.name == 'GM', message.channel.server.roles)
    if message.author.id == message.channel.server.owner.id or role2 or role3 or role4:
        for disuser in message.mentions:
            user = discord.utils.find(lambda member: member.name == disuser.name, message.channel.server.members)
            splitcmd = message.content.split()
            if "!admin" in splitcmd:
                on_admin(message)
            elif "!member" in splitcmd:
                on_member(message)
            break
        else:
            print('Name not specified.')
            client.send_message(message.channel, 'You did not specify a user to apply role changes to.')

def on_admin(message):
    role = discord.utils.find(lambda role: role.name == 'Admin', message.channel.server.roles)
    if role is not None:
        client.replace_roles(user, role)
        print('Changed a User to Admin.')
        client.send_message(message.channel,'Successfully added ' + user.name + ' to Admin.')
    else:
        print('role not found.')

def on_member(message):
    role = discord.utils.find(lambda role: role.name == 'Members', message.channel.server.roles)
    if role is not None:
        client.replace_roles(user, role)
        print('Changed a User to Members.')
        client.send_message(message.channel, 'Successfully added ' + user.name + ' to Members.')
    else:
        print('role not found.')

def on_owner(message):
    print('is owner')
    if(message.content.startswith('!join')):
        on_join(message)
    elif(message.content.startswith('!leave')):
        on_leave(message)
        if message.channel.server and message.channel.server.id == server_id:
            on_commandignore(message)

def on_join(message):
    stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('joined server on ' + stamp)
    response = messageparser.parse(message)
    client.send_message(message.channel, 'Alright.')
    if(response is not None):
        client.send_message(message.channel, response)

def on_leave(message):
    stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    server = message.channel.server
    print('leaving server on ' + stamp)
    client.send_message(message.channel, 'See ya.')
    server_id = message.channel.server.id

def on_client(message):
    response = messageparser.parse(message)
    if(response is not None):
        client.send_message(message.channel, response)
    elif(message.content.startswith('!market')):
        on_market(message)
    elif(message.content.startswith('!role')):
        on_role(message)
    elif(message.content.startswith('!debug')):
        on_Debug(message)

def on_commandignore(message):
    if(message.content.startswith('!leave')):
        return
    if(message.content.startswith('!hall')):
        return
    if(message.content.startswith('!blood')):
        return
    if(message.content.startswith('!commands')):
        return
    if(message.content.startswith('!changelog')):
        return
    if(message.content.startswith('!source')):
        return
    if(message.content.startswith('!beg')):
        return
    if(message.content.startswith('!goodboy')):
        return
    if(message.content.startswith('!elwiki')):
        return
    if(message.content.startswith('!babel')):
        return
    if(message.content.startswith('!na')):
        return
    if(message.content.startswith('!uk')):
        return
    if(message.content.startswith('!void')):
        return
    if(message.content.startswith('!events')):
        return
    if(message.content.startswith('!promo')):
        return
    if(message.content.startswith('!general')):
        return
    if(message.content.startswith('!suggest')):
        return
    if(message.content.startswith('!intro')):
        return
    if(message.content.startswith('!guild')):
        return
    if(message.content.startswith('!shots')):
        return
    if(message.content.startswith('!ibset')):
        return
    if(message.content.startswith('!google')):
        return
    if(message.content.startswith('!gimg')):
        return
    if(message.content.startswith('!youtube')):
        return
    if(message.content.startswith('!lenify')):
        return
    if(message.content.startswith('!roast')):
        return
    if(message.content.startswith('!salt')):
        return
    if(message.content.startswith('!lyyin')):
        return