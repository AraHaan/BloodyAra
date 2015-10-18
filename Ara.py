import os
import discord
import logging
import datetime
import messageparser
import updatecheck


client = discord.Client()
client.login('email', 'password')
server_id = 'server_id'

@client.event
def on_message(message):
    if message.channel.server and message.channel.server.id == 'server_id':
        if(message.content.startswith('!blood')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!commands')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!changelog')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!source')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        if(message.content.startswith('!beg')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        if(message.content.startswith('!goodboy')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!elwiki')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!babel')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!na')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!uk')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!void')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!events')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!promo')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!general')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!suggest')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!intro')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!guild')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!shots')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!ibset')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!google')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!gimg')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!youtube')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!roast')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!salt')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        elif(message.content.startswith('!lyyin')):
            client.send_message(message.channel,'Sorry, Ignoring Commands for this Server.\n' + server_id)
        return
    response = messageparser.parse(message)
    if(response is not None):
        client.send_message(message.channel, response)
        if(message.content.startswith('!market')):
            client.send_message(message.channel,'Sorry, This Command is not ready yet.')
    elif(message.author.id.startswith('creator_id')):
        print('is owner')
        if(message.content.startswith('!join')):
            stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('joined server on ' + stamp)
            client.accept_invite(message.content[5:].strip())
            client.send_message(message.channel, 'Alright.')
        elif(message.content.startswith('!leave')):
            stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            server = message.channel.server
            print('leaving server on ' + stamp)
            client.send_message(message.channel, 'See ya.')
            client.leave_server(server)
        elif(message.content.startswith('!register')):
            stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('registering channel ' + message.channel.id + ' ' + stamp)
            client.send_message(message.channel, updatecheck.register(message.channel.id))
        elif(message.content.startswith('!unregister')):
            stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('unregistering channel ' + message.channel.id + ' ' + stamp)
            client.send_message(message.channel, updatecheck.unregister(message.channel.id))
        elif(message.content.startswith('!list')):
            stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('channel list ' + ' ' + stamp)
            client.send_message(message.channel, 'Channels registered for updates: ' + updatecheck.listeners())

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
