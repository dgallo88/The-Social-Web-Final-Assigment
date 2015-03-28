
def twitter_search(q='#happy', count=100):
    import twitter
    import json

    CONSUMER_KEY = 'Kp1f3hTNbezaAmbD5MCP6Z02l'
    CONSUMER_SECRET = 'XAUFxgloIdFxMSd1Wnr2T6wsPK8BqjIYth85AYbIKmEIh77XCS'
    OAUTH_TOKEN = '421413363-Mh7mMTmojDYfdwisc9ja52tidkvf4gFKXivUj1ng' # to get the oauth credential you need to click on the 'Create my access token' button and wait few moments
    OAUTH_TOKEN_SECRET = 'TlTh5z87I3KiCAWiMAM3m0D27PCIsW7xWm365E202VIx3'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    #print twitter_api # Nothing to see by displaying twitter_api except that it's now a defined variable

    from datetime import datetime
    startTime = datetime.now()
    print 'Start time: ' +  str(startTime)
    # import time
    # time.sleep(1)

    #q = 'q=place:879d7cfc66c9c290'    #The Netherlands
    #q = '#happy'
    #count = 100 # I can only retrieve as maximiun 100 tweets
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets
    search_results = twitter_api.search.tweets(q=q, count=count, max_id=0)
    statuses = search_results['statuses']
    print 'Amount of tweets: ' + str( len(statuses) )
    ids = [ status['id'] for status in statuses ]
    print 'Amount of ids: ' + str( len(ids) )
    lowerID = ids[0]
    for id in ids:
        if id < lowerID:
            lowerID=id

    print 'Lower id: ' + str( lowerID )
    #print "**********PRINTING IDs************"
    #print json.dumps(ids, indent=1)   #If you want to see the ID, uncomment this line

    max_iterations=50
    iterations = 1    #condition will change
    previous_lowerID = lowerID + 1
    while (iterations < max_iterations and len(ids)> 0 and lowerID < previous_lowerID):
        previous_lowerID = lowerID
        search_results = twitter_api.search.tweets(q=q, count=count, max_id=lowerID-1)
        statuses += search_results['statuses']
        print 'Amount of tweets: ' + str( len(statuses) )

        ids = [ status['id'] for status in statuses ]
        print 'Amount of ids: ' + str( len(ids) )
        for id in ids:
            if id < lowerID:
                lowerID=id
        iterations+=1
        print 'Iteration: ' + str( iterations)
        print 'Lower id: ' + str( lowerID )
        #print "**********PRINTING IDs********"
        #print json.dumps(ids, indent=1)      #If you want to see the ID, uncomment this line


    #This code is to make the visualization in Python
    '''
    import numpy
    wod_counts = {1,2,3,4}
    import matplotlib.pyplot as plt
    plt.loglog(word_counts)
    plt.ylabel("Freq")
    plt.xlabel("Word Rank")
    radius = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    day = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724]
    plt.plot(radius, area)
    plt.show()
    '''

    endTime = datetime.now()
    print 'Start time: ' +  str(startTime)
    print 'End time: ' + str(endTime)
    difference = endTime - startTime
    print 'Elapsed time: ' + str(difference)


    for s in statuses:
        if s['id']==lowerID:
            print 'Lower ID created at: ' + s['created_at']

    print "THE END"

    return statuses