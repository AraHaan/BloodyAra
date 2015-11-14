import os
import discord
import botfunc
import messageparser

discord_user_email = 'email'
discord_user_password = 'password'
client = discord.Client()
client.login(discord_user_email, discord_user_password)

@client.event
def on_message(message):
    response = messageparser.parse(message)
    if(response is not None):
        client.send_message(message.channel, response)
    botfunc.commands(client, message)


@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
