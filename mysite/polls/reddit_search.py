#This function searches reddit for specific keywords
#Note: Reddit does not use hastags (#)

import time
from datetime import datetime
from datetime import timedelta
import requests

def reddit_search(q1, max_iterations):
    #max_iterations = 5
    startTime = datetime.now()

    headers = {
        "User-Agent": "Something/1.0"
    }

    reddit_count = [0,0,0,0,0,0,0]

    max_id = ""

    #Rest of the pages
    iterations = 0    #condition will change
    while (iterations < max_iterations and max_id is not None):
        if iterations == 0:
            max_id = 'None'
        count=0
        r = requests.get(r'http://www.reddit.com/search.json?q=%s&t=week&sort=new&limit=100&after=%s'% (q1,max_id), headers=headers)
        r.text
        data = r.json()
        max_id = data['data']['after']

        #Create list with length depending on how much results Reddit API returns
        if iterations == 0:
            reddit_set = []
            for i in range(len(data['data']['children'])):
                reddit_set.append(0)


        for child in data['data']['children']:
            reddit_set[count] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(child['data']['created_utc']))
            reddit_set[count] = datetime.strptime(reddit_set[count], "%Y-%m-%d %H:%M:%S")
            difference = startTime - reddit_set[count]

            if difference < timedelta(hours=24) :
                reddit_count[0] += 1
            elif difference >= timedelta(hours=24) and difference < timedelta(hours=48) :
                reddit_count[1] += 1
            elif difference >= timedelta(hours=48) and difference < timedelta(hours=72) :
                reddit_count[2] += 1
            elif difference >= timedelta(hours=72) and difference < timedelta(hours=96) :
                reddit_count[3] += 1
            elif difference >= timedelta(hours=96) and difference < timedelta(hours=120) :
                reddit_count[4] += 1
            elif difference >= timedelta(hours=120) and difference < timedelta(hours=144) :
                reddit_count[5] += 1
            else :
                reddit_count[6] += 1

            count = count+1
        iterations += 1
    print reddit_count[:]
    return reddit_count



