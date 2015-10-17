import bs4
import requests

def scrape(response):
    soup = bs4.BeautifulSoup(response, "lxml")
    print('soup made')
    if(len(soup.select('ul.mw-search-results')) != 0):
        url = 'http://elwiki.net' + soup.select('ul.mw-search-results')[0].find_all('a')[0].get('href')
        print(url)
        return url
    else:
        print('nothing found')
        return None

def scrape_void():
    r = requests.get('http://www.elsword.to/forum/index.php?/forum/4-news-and-announcements/')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    print('soup made')
    topics = soup.select('table.topic_list')
    if(len(topics) != 0):
        topiclist = topics[0].select('tr.__topic')
        latest_id = "0"
        for topic in topiclist:
            topic_id = topic['data-tid']
            if(topic_id > latest_id):
                latest_id = topic_id
        
        latest = topics[0].find("tr", {"data-tid" : latest_id})
        link = latest.find('a').get('href')
        title = latest.find('a').find('span').string
        return('Latest Void update - ' + title + ' ' + link)
        
    return 'I could not connect to the VoidEls forums.'
    
def vevent():
    r = requests.get('http://www.elsword.to/forum/index.php?/forum/5-events-contests/')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    print('soup made')
    topics = soup.select('table.topic_list')
    if(len(topics) != 0):
        topiclist = topics[0].select('tr.__topic')
        latest_id = "0"
        for topic in topiclist:
            topic_id = topic['data-tid']
            if(topic_id > latest_id):
                latest_id = topic_id
        
        latest = topics[0].find("tr", {"data-tid" : latest_id})
        link = latest.find('a').get('href')
        title = latest.find('a').find('span').string
        return('Latest Void Event & Contest - ' + title + ' ' + link)
        
    return 'I could not connect to the VoidEls forums.'
    
def vpromotions():
    r = requests.get('http://www.elsword.to/forum/index.php?/forum/25-promotions/')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    print('soup made')
    topics = soup.select('table.topic_list')
    if(len(topics) != 0):
        topiclist = topics[0].select('tr.__topic')
        latest_id = "0"
        for topic in topiclist:
            topic_id = topic['data-tid']
            if(topic_id > latest_id):
                latest_id = topic_id
        
        latest = topics[0].find("tr", {"data-tid" : latest_id})
        link = latest.find('a').get('href')
        title = latest.find('a').find('span').string
        return('Latest Void Promotion update - ' + title + ' ' + link)
        
    return 'I could not connect to the VoidEls forums.'
    
def vgeneral():
    r = requests.get('http://www.elsword.to/forum/index.php?/forum/6-general-discussion/')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    print('soup made')
    topics = soup.select('table.topic_list')
    if(len(topics) != 0):
        topiclist = topics[0].select('tr.__topic')
        latest_id = "0"
        for topic in topiclist:
            topic_id = topic['data-tid']
            if(topic_id > latest_id):
                latest_id = topic_id
        
        latest = topics[0].find("tr", {"data-tid" : latest_id})
        link = latest.find('a').get('href')
        title = latest.find('a').find('span').string
        return('Latest Void General Discussion Topic - ' + title + ' ' + link)
        
    return 'I could not connect to the VoidEls forums.'
    
def vsuggestions():
    r = requests.get('http://www.elsword.to/forum/index.php?/forum/7-suggestions/')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    print('soup made')
    topics = soup.select('table.topic_list')
    if(len(topics) != 0):
        topiclist = topics[0].select('tr.__topic')
        latest_id = "0"
        for topic in topiclist:
            topic_id = topic['data-tid']
            if(topic_id > latest_id):
                latest_id = topic_id
        
        latest = topics[0].find("tr", {"data-tid" : latest_id})
        link = latest.find('a').get('href')
        title = latest.find('a').find('span').string
        return('Latest Void Elsword Suggestions - ' + title + ' ' + link)
        
    return 'I could not connect to the VoidEls forums.'
    
def vintro():
    r = requests.get('http://www.elsword.to/forum/index.php?/forum/8-introduction-farewell/')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    print('soup made')
    topics = soup.select('table.topic_list')
    if(len(topics) != 0):
        topiclist = topics[0].select('tr.__topic')
        latest_id = "0"
        for topic in topiclist:
            topic_id = topic['data-tid']
            if(topic_id > latest_id):
                latest_id = topic_id
        
        latest = topics[0].find("tr", {"data-tid" : latest_id})
        link = latest.find('a').get('href')
        title = latest.find('a').find('span').string
        return('Latest Void Intro/Farewell - ' + title + ' ' + link)
        
    return 'I could not connect to the VoidEls forums.'
    
def vmarket():
    r = requests.get('http://www.elsword.to/forum/index.php?/forum/14-void-marketplace/')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    print('soup made')
    topics = soup.select('table.topic_list')
    if(len(topics) != 0):
        topiclist = topics[0].select('tr.__topic')
        latest_id = "0"
        for topic in topiclist:
            topic_id = topic['data-tid']
            if(topic_id > latest_id):
                latest_id = topic_id
        
        latest = topics[0].find("tr", {"data-tid" : latest_id})
        link = latest.find('a').get('href')
        title = latest.find('a').find('span').string
        return('Latest Void Market Topic - ' + title + ' ' + link)
        
    return 'I could not connect to the VoidEls forums.'
    
def vguilds():
    r = requests.get('http://www.elsword.to/forum/index.php?/forum/16-guilds/')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    print('soup made')
    topics = soup.select('table.topic_list')
    if(len(topics) != 0):
        topiclist = topics[0].select('tr.__topic')
        latest_id = "0"
        for topic in topiclist:
            topic_id = topic['data-tid']
            if(topic_id > latest_id):
                latest_id = topic_id
        
        latest = topics[0].find("tr", {"data-tid" : latest_id})
        link = latest.find('a').get('href')
        title = latest.find('a').find('span').string
        return('Latest Void Guild Topic - ' + title + ' ' + link)
        
    return 'I could not connect to the VoidEls forums.'
    
