

def register(channel_id):
    channel_list = listeners()
    print(channel_list)
    if(channel_list.find(channel_id) == -1):
        print('adding...')
        with open("channels", "w+") as out_file:
            out_file.write(channel_id + ',')
            out_file.close()
        return 'Channel ' + channel_id + ' has been registered.'
    else:
        return 'Channel ' + channel_id + ' is already registered.'
            


def unregister(channel_id):
    channel_list = listeners()
    print(channel_list)
    if(channel_list.find(channel_id) != -1):
        print('removing...')
        new_list = channel_list.replace(channel_id + ',', '')
        with open("channels", "w+") as out_file:
            out_file.seek(0)
            out_file.truncate()
            out_file.write(new_list)
            print('done')
        return 'Channel ' + channel_id + ' has been unregistered.'
    else:
        return 'Channel ' + channel_id + ' is not registered.'


def listeners():
    channel_list = ""
    print('opening')
    with open("channels", "w+") as out_file:
        channel_list = out_file.read()
    print(channel_list)
    return channel_list


