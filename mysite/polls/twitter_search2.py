

def twitter_search2(twitter_api, q, count, loc = None):

    max_iterations = 70
    import twitter
    import json

    if loc is not None:
        q = q + ' AND place:' + loc

    #q_extend = q + ' AND place:879d7cfc66c9c290'
    print q

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
    if len(ids) > 0:
        lowerID = ids[0]
        for id in ids:
            if id < lowerID:
                lowerID=id

        print 'Lower id: ' + str( lowerID )
        #print "**********PRINTING IDs************"
        #print json.dumps(ids, indent=1)   #If you want to see the ID, uncomment this line

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