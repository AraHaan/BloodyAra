import os
import discord
import logging
import datetime
import messageparser


discord_user_email = 'email'
discord_user_password = 'password'
discord_user_id = 'user_id'
client = discord.Client()
client.login(discord_user_email, discord_user_password)

@client.event
def on_message(message):
    response = messageparser.parse(message)
    if(response is not None):
        client.send_message(message.channel, response)
    elif(message.content.startswith('!market')):
        print('Command not finished.')
        client.send_message(message.channel,'Sorry, This Command is not working properly yet.')
    elif(message.content.startswith('!role')):
        if message.author.id == message.channel.server.owner.id:
            for disuser in message.mentions:
                user = discord.utils.find(lambda member: member.name == disuser.name, message.channel.server.members)
                splitcmd = message.content.split()
                if "!admin" in splitcmd:
                    role = discord.utils.find(lambda role: role.name == 'Admin', message.channel.server.roles)
                    if role is not None:
                        client.replace_roles(user, role)
                        client.send_message(message.channel,'Successfully added ' + user.name + ' to Members.')
                elif "!member" in splitcmd:
                    role = discord.utils.find(lambda role: role.name == 'Members', message.channel.server.roles)
                    if role is not None:
                        client.replace_roles(user, role)
                        client.send_message(message.channel, 'Successfully added ' + user.name + ' to Members.')
                    print('role not found')
            client.send_message(message.channel, 'You did not specify a user to Apply Role changes to')
        else:
            client.send_message(message.channel, "Sorry, you don't have the correct Role to use this command")

    # Does not work yet. Do not mess with it unless you can help. gg
    """elif(message.author.id.startswith(discord_user_id)):
        print('is owner')
        if(message.content.startswith('!join')):
            stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('joined server on ' + stamp)
            response = messageparser.parse(message)
            client.send_message(message.channel, 'Alright.')
            if(response is not None):
                client.send_message(message.channel, response)
        elif(message.content.startswith('!leave')):
            stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            server = message.channel.server
            print('leaving server on ' + stamp)
            client.send_message(message.channel, 'See ya.')
            server_id = message.channel.server.id
            if message.channel.server and message.channel.server.id == server_id:
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
                    return"""
        
@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
