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
    elif(message.author.roles('Guild Master')):
        if(message.content.startswith('!role')):
            print('is Role ' + message.author.roles)
            for mention in message.mentions:
                print('mentioning ' + mention.name)
                mention.mention()
                """ code to add_role to a user. """
            client.send_message(message.channel,'Sorry, No User was specified.')
    elif(message.author.roles('Admin')):
        if(message.content.startswith('!role')):
            print('is Role ' + message.author.roles)
            for mention in message.mentions:
                print('mentioning ' + mention.name)
                mention.mention()
                """ code to add_role to a user. """
            client.send_message(message.channel,'Sorry, No User was specified.')
    elif(message.author.roles('Bots')):
        if(message.content.startswith('!role')):
            print('is Role ' + message.author.roles)
            for mention in message.mentions:
                print('mentioning ' + mention.name)
                mention.mention()
                """ code to add_role to a user. """
            client.send_message(message.channel,'Sorry, No User was specified.')
        
@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
