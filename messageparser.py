import datetime
import requests
import feedparser
import elsgear
import badword
import scrape
import urllib

link = "http://www.mediafire.com/download/qxa3q7jqo26v9xq/BloodyAra-master.rar"
commands = "Available commands:\n\n**!blood**\n**!beg**\n**!goodboy**\n**!elwiki <searchterm>**\n**!ibset <short_set_name> <character>**\n**!babel**\n**!na**\n**!uk**\n**!void**\n**!events**\n**!promo**\n**!general**\n**!suggest**\n**!intro**\n**!guild**\n**!google <searchterm>**\n**!gimg <searchterm>**\n**!youtube <searchterm>**\n**!shots**\n**!roast <optionally_mention_user>**\n**!salt <optionally_mention_user>**\n**!lyyin <optionally_mention_user>**\n**!changelog**\n**!source**"
salt = u"\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2584\u2584\u2588\u2588\u2588\u2588\u2588\u2588\u2584\n\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2584\u2584\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2584\n\u2592\u2592\u2592\u2592\u2592\u2592\u2584\u2584\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n\u2592\u2592\u2592\u2584\u2588\u2588\u2588\u2588\u2580\u2580\u2580\u2588\u2588\u2580\u2588\u2588\u258c\u2588\u2588\u2588\u2580\u2580\u2580\u2588\u2588\u2588\u2588\n\u2592\u2592\u2590\u2580\u2588\u2588\u2588\u2588\u258c\u2580\u2588\u2588\u258c\u2580\u2590\u2588\u258c\u2588\u2588\u2588\u2588\u258c\u2588\u2588\u2588\u2588\u2588\u258c\n\u2592\u2592\u2588\u2592\u2592\u2580\u2588\u2588\u2580\u2580\u2590\u2588\u2590\u2588\u258c\u2588\u258c\u2580\u2580\u2588\u2588\u258c\u2588\u2588\u2588\u2588\u2588\u2588\n\u2592\u2592\u2588\u2592\u2592\u2592\u2592\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u258c\n\u2592\u2592\u2592\u258c\u2592\u2592\u2592\u2592\u2588\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2588\u2588\u2588\u2588\u2588\u2588\u2580\n\u2592\u2592\u2592\u2580\u2584\u2593\u2593\u2593\u2592\u2588\u2588\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2588\u2588\u2588\u2588\u2588\u2580\u2580\n\u2592\u2592\u2592\u2592\u2580\u2591\u2593\u2593\u2592\u2590\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2580\u2580\u2592\n\u2592\u2592\u2592\u2592\u2592\u2591\u2591\u2592\u2592\u2590\u2588\u2588\u2588\u2588\u2588\u2580\u2580\u2592\u2592\u2592\u2592\u2592\u2592\n\u2592\u2592\u2591\u2591\u2591\u2591\u2591\u2580\u2580\u2580\u2580\u2580\u2580\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\n\u2592\u2592\u2592\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2592\u2592"
lyying = u"\u02b7\u02b0\u02b8 \u1d57\u02b0\u1d49 \u0066\u1d58\u0368\u1d4f \u02b8\u00ba\u1d58 \u02e1\u02b8\u02b8\u02b8\u0027\u207f\u002c \u02b7\u02b0\u02b8 \u02b8\u00ba\u1d58 \u1d43\u02e1\u02b7\u1d43\u02b8\u02e2 \u02e1\u02b8\u02b8\u02b8\u0027\u207f\u002c \u1d50\u1d50\u1d50\u1d50\u1d50\u1d50 \u00ba\u02b0 \u1d50\u02b8 \u1d4d\u00ba\u1d48 \u02e2\u1d57\u00ba\u0070 \u0066\u1d58\u0368\u1d4f\u0027\u207f \u02e1\u02b8\u02b8\u02b8\u0027\u207f"
changelog = "Added a few commands:\n\n**!beg**\n**!goodboy**\n**!events**\n**!changelog**\n**!source**\n**!promo**\n**!general**\n**!suggest**\n**!intro**\n**!guild**\n\n** Changes: Discovered how to make commands be ignored when you provide a Server ID that you know all of the commands would conflict with another bot.**\n\nv1.3.0.14"
source = "Download the Latest Source Code at: \n" + link + "."

def parse(message):
    if(message.content.startswith('!blood')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('sending hello to ' + message.author.name + ' ' + stamp)
        return ('Is that blood I smell? ' + stamp)
    elif(message.content.startswith('!commands')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('sending command list ' + stamp)
        return (commands)
    elif(message.content.startswith('!changelog')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('sending changelog ' + stamp)
        return (changelog)
    elif(message.content.startswith('!source')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('sending source ' + stamp)
        return (source)
    if(message.content.startswith('!beg')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('Frozen Pizza ' + message.author.name + ' ' + stamp)
        return ('Can I have that Frozen Pizza? ' + stamp)
    if(message.content.startswith('!goodboy')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('Treat ' + message.author.name + ' ' + stamp)
        return ('Can I have my Treat now? ' + stamp)
    elif(message.content.startswith('!elwiki')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        searchterm = message.content[7:].strip()
        if (len(searchterm) == 0):
            print('no argument specified')
            return ('Tell me what to look for, and I shall deliver.')
        if (searchterm.lower().find('seris') != -1):
            print('not looking for seris')
            return ('Some old mistakes should not be touched upon. Mistakes are often a scab to an old, deep wound.')
        if (badword.has_profanity(searchterm)):
            return ('You should reconsider your words if you value your life, ' + message.author.mention())
        print('looking up ' + searchterm)
        r = requests.get('http://elwiki.net/wiki/index.php?search=' + searchterm, allow_redirects=False)
        print(r.status_code)
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if (r.status_code == 302):
            answer = r.headers['Location']
            print(answer + ' sent on ' + stamp)
            return ('Page for ' + searchterm + ' : ' + answer)
        if (r.status_code == 200):
            print('scraping')
            answer = scrape.scrape(r.text)
            if(answer is None):
                return 'I could not find a match for that.'
            else:
                return ('First match for ' + searchterm + ' : ' + answer)
    elif(message.content.startswith('!babel')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('looking up babel on ' + stamp)
        babelfeed = feedparser.parse('http://elwiki.net/babel/?feed=rss2')
        answer = babelfeed.entries[0]['title'] + ' ' + babelfeed.entries[0]['link']
        print(answer)
        return ('Last post on Babel - ' + answer)
    elif(message.content.startswith('!na')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('looking up na on ' + stamp)
        nafeed = feedparser.parse('http://en.elswordonline.com/feed/')
        answer = nafeed.entries[0]['title'] + ' ' + nafeed.entries[0]['link']
        print(answer)
        return ('Last NA update - ' + answer)
    elif(message.content.startswith('!uk')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('looking up uk on ' + stamp)
        ukfeed = feedparser.parse('http://board.en.elsword.gameforge.com/index.php?page=ThreadsFeed&format=rss2&boardID=8')
        answer = ukfeed.entries[0]['title'] + ' ' + ukfeed.entries[0]['link']
        print(answer)
        return ('Last UK update - ' + answer)
    elif(message.content.startswith('!void')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('looking up void on ' + stamp)
        return scrape.scrape_void()
    elif(message.content.startswith('!events')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('looking up void events and contests on ' + stamp)
        return scrape.vevent()
    elif(message.content.startswith('!promo')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('looking up void promotions on ' + stamp)
        return scrape.vpromotions()
    elif(message.content.startswith('!general')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('looking up void void general topics on ' + stamp)
        return scrape.vgeneral()
    elif(message.content.startswith('!suggest')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('looking up void void suggestions on ' + stamp)
        return scrape.vsuggestions()
    elif(message.content.startswith('!intro')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('looking up void Intro/Farewells on ' + stamp)
        return scrape.vintro()
    elif(message.content.startswith('!guild')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('looking up void guild topics on ' + stamp)
        return scrape.vguilds()
    elif(message.content.startswith('!shots')):
        stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('sending shots fired ' + stamp)
        return ('Hmm. It appears as if shots have been fired.')
    elif(message.content.startswith('!ibset')):
        searchterm = message.content[6:].strip()
        return elsgear.lookup(searchterm)
    elif(message.content.startswith('!google')):
        searchterm = message.content[7:].strip()
        if(len(searchterm) == 0):
            return ('Tell me what to look for, and I shall deliver.')
        if (badword.has_profanity(searchterm)):
            return ('You should reconsider your words if you value your life, ' + message.author.mention())
        return ('https://www.google.com/search?q=' + urllib.parse.quote_plus(searchterm))
    elif(message.content.startswith('!gimg')):
        searchterm = message.content[5:].strip()
        if(len(searchterm) == 0):
            return ('Tell me what to look for, and I shall deliver.')
        if (badword.has_profanity(searchterm)):
            return ('You should reconsider your words if you value your life, ' + message.author.mention())
        return ('https://www.google.com/search?q=' + urllib.parse.quote_plus(searchterm) + '&tbm=isch')
    elif(message.content.startswith('!youtube')):
        searchterm = message.content[8:].strip()
        if(len(searchterm) == 0):
            return ('Tell me what to look for, and I shall deliver.')
        if (badword.has_profanity(searchterm)):
            return ('You should reconsider your words if you value your life, ' + message.author.mention())
        return ('https://www.youtube.com/results?search_query=' + urllib.parse.quote_plus(searchterm))
    elif(message.content.startswith('!roast')):
        print('delivering roast')
        response = 'http://i.imgur.com/rSMtLIM.gif'
        for mention in message.mentions:
            print('mentioning ' + mention.name)
            response += (' ' + mention.mention())
        return response
    elif(message.content.startswith('!salt')):
        print('delivering salt')
        response = ''
        for mention in message.mentions:
            print('mentioning ' + mention.name)
            response += (' ' + mention.mention())
        return response + '\n\n' + salt
    elif(message.content.startswith('!lyyin')):
        response = ''
        for mention in message.mentions:
            print('mentioning ' + mention.name)
            response += (mention.mention() + ' ')
        response += lyying
        return response
    else:
        return None
