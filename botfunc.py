import discord
import datetime
import feedparser
import messageparser


discord_user_id = 'user_id'
discord_server_id = 'server_id' #Amiable Server ID.
discord_server_id2 = 'server_id' #Ambition Server ID.
discord_server_id3 = 'server_id' #Division Server ID.
command_not_done = 'Sorry, This Command is not working properly yet.'
fang = "Fang loves Chung. He loves Chung so much he __manes__ it."
kirbu = "Kirbu loves Meth. He loves Meth so much we had to __Barium__."
ramby = "Ramby loves Aisha. She loves Aisha so much she  hunts __Add__ with it."
rea = "Rea loves Asura. She loves Asura so much she married __Jobber__ with it."

def commands(client, message):
    if(message.content.startswith('!smite')):
        client.change_status(game_id=19, idle=False)
    elif(message.content.startswith('!els')):
        client.change_status(game_id=316, idle=False)
    elif(message.content.startswith('!pso2')):
        if message.channel.server:
            client.change_status(game_id=355, idle=False)
    elif(message.content.startswith('!roleinfo')):
        for role in message.channel.server.roles:
            roleinfo = "role name: {0}, role id: {1}".format(role.name, role.id)
            client.send_message(message.channel, "``" + roleinfo + "``")
    elif(message.content.startswith('!text2words')):
        stripped_content = message.content[11:].strip()
        result = stripped_content
        if len(result) <= 0:
            print('Doing nothing.')
        else:
            client.send_message(message.channel, result, tts=True)
    elif(message.content.startswith('!tera')):
        client.change_status(game_id=258, idle=False)
    elif(message.content.startswith('!b3')):
        client.change_status(game_id=463, idle=False)
    elif(message.content.startswith('!wait')):
        client.send_message(message.channel, 'What are you waiting for? Meth?')
    elif(message.content.startswith('!market')):
        print('Command not finished.')
        client.send_message(message.channel, command_not_done)
    elif(message.content.startswith(':3')):
        data = 'https://i.gyazo.com/da52bad9d25dcf64f1e9cec667f22e26.gif'
        client.send_message(message.channel, data)
    elif(message.content.startswith('!role')):
        role2 = discord.utils.find(lambda role: role.name == 'Admin', message.channel.server.roles)
        role3 = discord.utils.find(lambda role: role.name == 'Guild Master', message.channel.server.roles)
        role4 = discord.utils.find(lambda role: role.name == 'GM', message.channel.server.roles)
        role5 = discord.utils.find(lambda role: role.name == '@admins', message.channel.server.roles)
        if message.author.id == message.channel.server.owner.id or role2 or role3 or role4 or role5:
            for disuser in message.mentions:
                user = discord.utils.find(lambda member: member.name == disuser.name, message.channel.server.members)
                splitcmd = message.content.split()
                if message.channel.server and message.channel.server.id == discord_server_id:
                    if "!admins" in splitcmd:
                        role = discord.utils.find(lambda role: role.name == '@admins', message.channel.server.roles)
                        if role is not None:
                            client.replace_roles(user, role)
                            print('Changed a user to @admins.')
                            client.send_message(message.channel,'Successfully added ' + user.name + ' to @admins.')
                    else:
                        print('role not found.')
                    if "!none" in splitcmd:
                        role = discord.utils.find(lambda role: role.name == '@admins', message.channel.server.roles)
                        if role is not None:
                            client.remove_roles(user, role)
                            print('Changed a user from @admins.')
                            client.send_message(message.channel,'Successfully removed ' + user.name + ' from @admins.')
                else:
                    if "!admin" in splitcmd:
                        role = discord.utils.find(lambda role: role.name == 'Admin', message.channel.server.roles)
                        if role is not None:
                            client.replace_roles(user, role)
                            print('Changed a user to Admin.')
                            client.send_message(message.channel,'Successfully added ' + user.name + ' to Admin.')
                        else:
                            print('role not found.')
                    elif "!member" in splitcmd:
                        role = discord.utils.find(lambda role: role.name == 'Members', message.channel.server.roles)
                        if role is not None:
                            client.replace_roles(user, role)
                            print('Changed a user to Members.')
                            client.send_message(message.channel, 'Successfully added ' + user.name + ' to Members.')
                        else:
                            print('role not found.')
                break
            else:
                print('Name not specified.')
                client.send_message(message.channel, 'You did not specify a user to apply role changes to.')
    elif(message.content.startswith('!prune')):
        if message.channel.server and message.channel.server.id == discord_server_id:
            role4 = discord.utils.find(lambda role: role.name == 'GM', message.channel.server.roles)
            role5 = discord.utils.find(lambda role: role.name == '@admins', message.channel.server.roles)
            if message.author.id == message.channel.server.owner.id or role4 or discord_user_id or role5:
                opt = message.content[len("!prune "):].strip()
                num = 1
                if opt:
                    try:
                        num = int(opt)
                    except:
                        return

                to_remove = [m for m in client.logs_from(message.channel, limit=num + 1)]
                for log_message in to_remove:
                    client.delete_message(log_message)
            else:
                client.send_message(message.channel, 'You are not the Right Role to use this command.')
        if message.channel.server and message.channel.server.id == discord_server_id2:
            role2 = discord.utils.find(lambda role: role.name == 'Guild Leaders', message.channel.server.roles)
            if message.author.id == message.channel.server.owner.id or role2 or discord_user_id:
                opt = message.content[len("!prune "):].strip()
                num = 1
                if opt:
                    try:
                        num = int(opt)
                    except:
                        return

                to_remove = [m for m in client.logs_from(message.channel, limit=num + 1)]
                for log_message in to_remove:
                    client.delete_message(log_message)
            else:
                client.send_message(message.channel, 'You are not the Right Role to use this command.')
        if message.channel.server and message.channel.server.id == discord_server_id3:
            role2 = discord.utils.find(lambda role: role.name == 'Admin', message.channel.server.roles)
            role3 = discord.utils.find(lambda role: role.name == 'Guild Master', message.channel.server.roles)
            if message.author.id == message.channel.server.owner.id or role2 or discord_user_id or role3:
                opt = message.content[len("!prune "):].strip()
                num = 1
                if opt:
                    try:
                        num = int(opt)
                    except:
                        return

                to_remove = [m for m in client.logs_from(message.channel, limit=num + 1)]
                for log_message in to_remove:
                    client.delete_message(log_message)
            else:
                client.send_message(message.channel, 'You are not the Right Role to use this command.')
    elif(message.content.startswith('!ban')):
        if message.channel.server and message.channel.server.id == discord_server_id:
            role = discord.utils.find(lambda role: role.name == 'Banned', message.channel.server.roles)
            role2 = discord.utils.find(lambda role: role.name == 'Admin', message.channel.server.roles)
            role4 = discord.utils.find(lambda role: role.name == 'GM', message.channel.server.roles)
            role5 = discord.utils.find(lambda role: role.name == '@admins', message.channel.server.roles)
            if message.author.id == message.channel.server.owner.id or role2 or discord_user_id or role4 or role5:
                for disuser in message.mentions:
                    user = discord.utils.find(lambda member: member.name == disuser.name, message.channel.server.members)
                    splitcmd = message.content.split()
                    if role is not None:
                        client.replace_roles(user, role)
                        print('Banned ' + user.name + ' from server.')
                        client.send_message(message.channel,'Successfully Banned ' + user.name + ' from the Server.')
                    else:
                        client.send_message(message.channel,'The Roles ``Literally Hitler`` and ``Banned`` are needed to enable this command.')
        if message.channel.server and message.channel.server.id == discord_server_id2:
            role = discord.utils.find(lambda role: role.name == 'Banned', message.channel.server.roles)
            role2 = discord.utils.find(lambda role: role.name == 'Guild Leaders', message.channel.server.roles)
            if message.author.id == message.channel.server.owner.id or role2 or discord_user_id:
                for disuser in message.mentions:
                    user = discord.utils.find(lambda member: member.name == disuser.name, message.channel.server.members)
                    splitcmd = message.content.split()
                    if role is not None:
                        client.replace_roles(user, role)
                        print('Banned ' + user.name + ' from server.')
                        client.send_message(message.channel,'Successfully Banned ' + user.name + ' from the Server.')
                    else:
                        client.send_message(message.channel,'The Roles ``Literally Hitler`` and ``Banned`` are needed to enable this command.')
        if message.channel.server and message.channel.server.id == discord_server_id3:
            role = discord.utils.find(lambda role: role.name == 'Banned', message.channel.server.roles)
            role2 = discord.utils.find(lambda role: role.name == 'Admin', message.channel.server.roles)
            role3 = discord.utils.find(lambda role: role.name == 'Guild Master', message.channel.server.roles)
            if message.author.id == message.channel.server.owner.id or role2 or discord_user_id or role3:
                for disuser in message.mentions:
                    user = discord.utils.find(lambda member: member.name == disuser.name, message.channel.server.members)
                    splitcmd = message.content.split()
                    if role is not None:
                        client.replace_roles(user, role)
                        print('Banned ' + user.name + ' from server.')
                        client.send_message(message.channel,'Successfully Banned ' + user.name + ' from the Server.')
                    else:
                        client.send_message(message.channel,'The Roles ``Literally Hitler`` and ``Banned`` are needed to enable this command.')
    elif(message.content.startswith('!debug')):
        if(message.author.id.startswith(discord_user_id)):
            '''[x for x in range(10)]'''
            stripped_content = message.content[7:].strip()
            result = eval(stripped_content)
            result = str(result)
            result2 = type(result)
            result2 = str(result2)
            result3 = exec(stripped_content)
            result3 = str(result3)
            client.send_message(message.channel, "Eval:\n```Python\n" + result + "\n```" + "\nType:\n```Python\n" + result2 + "\n```" + "\nTraceback:\n```Python\n" + result3 + "\n```")
        else:
            client.send_message(message.channel, 'Sorry, you can not use this command.')
    elif(message.content.startswith('!8ball')):
        stripped_content = message.content[7:].strip()
        result = stripped_content
        user_name = message.author.mention()
        client.send_message(message.channel, user_name +" `" + result + "`: Yes, definitely! :thumbsup: ") or client.send_message(message.channel, user_name +" `" + result + "`: Not sure uh; i'd say Yes.") or client.send_message(message.channel, user_name +" `" + result + "`: Not a Chance.")
    elif message.channel.server and message.channel.server.id == discord_server_id:
        if(message.content.startswith('!fang')):
            client.send_message(message.channel, fang)
        elif(message.content.startswith('!kirbu')):
            client.send_message(message.channel, kirbu)
        elif(message.content.startswith('!ramby')):
            client.send_message(message.channel, ramby)
        elif(message.content.startswith('!rea')):
            client.send_message(message.channel, rea)