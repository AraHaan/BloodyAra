import os
import discord
import logging
import datetime
import messageparser
import botfunc


discord_user_email = 'email'
discord_user_password = 'password'
discord_user_id = 'user_id'
client = discord.Client()
client.login(discord_user_email, discord_user_password)

@client.event
def on_message(message):
    botfunc.on_client(message)

    # Does not work yet. Do not mess with it unless you can help. gg
    elif(message.author.id.startswith(discord_user_id)):
        '''botfunc.on_owner(message)'''
        
@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
