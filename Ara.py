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
    if(message.content.startswith('!market')):
        print('Command not finnished.')
        client.send_message(message.channel,'Sorry, This Command is not working properly yet.')
    elif(message.author.id.startswith(discord_user_id)):
        print('is owner')
        """
        if(message.content.startswith('!join')):
            stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('joined server on ' + stamp)
            client.accept_invite(message.content[5:].strip("0SBTUU1wZTYiaHxf"))
            client.send_message(message.channel, 'Alright.')
        elif(message.content.startswith('!leave')):
            stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            server = message.channel.server
            print('leaving server on ' + stamp)
            client.send_message(message.channel, 'See ya.')
            client.leave_server(server)
        """
    response = messageparser.parse(message)
    if(response is not None):
        client.send_message(message.channel, response)

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
