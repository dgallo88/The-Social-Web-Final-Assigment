
from datetime import datetime
from datetime import timedelta
from twitter_login import twitter_login

def hashtag_comparison(q1, q2=None, loc=None):
    count = 100
    twitter_api = twitter_login()

    #from country name to ID
    if loc is not None:
        result = twitter_api.geo.search(query=loc, granularity="country")
        place_id = result['result']['places'][0]['id']
        loc=place_id


    from twitter_search2 import twitter_search2
    statuses1 = twitter_search2(twitter_api, q1, count, loc)



    #For 1st word
    created_at1 = [ status['created_at']
        for status in statuses1 ]


    startTime = datetime.now()

    #For first word
    group1 = [0,0,0,0,0,0,0]
    for x in range(0, len (created_at1)):
        date_object = datetime.strptime(created_at1[x], '%a %b %d %H:%M:%S +0000 %Y')
        difference = startTime - date_object

        if difference < timedelta(hours=24) :
            group1[0] += 1
        elif difference >= timedelta(hours=24) and difference < timedelta(hours=48) :
            group1[1] += 1
        elif difference >= timedelta(hours=48) and difference < timedelta(hours=72) :
            group1[2] += 1
        elif difference >= timedelta(hours=72) and difference < timedelta(hours=96) :
            group1[3] += 1
        elif difference >= timedelta(hours=96) and difference < timedelta(hours=120) :
            group1[4] += 1
        elif difference >= timedelta(hours=120) and difference < timedelta(hours=144) :
            group1[5] += 1
        else :
            group1[6] += 1


    #For second word
    if q2 is not None:
        statuses2 = twitter_search2(twitter_api, q2, count, loc)
        created_at2 = [ status['created_at']
            for status in statuses2 ]

        group2 = [0,0,0,0,0,0,0]
        for x in range(0, len (created_at2)):
            date_object = datetime.strptime(created_at2[x], '%a %b %d %H:%M:%S +0000 %Y')
            difference = startTime - date_object

            if difference < timedelta(hours=24) :
                group2[0] += 1
            elif difference >= timedelta(hours=24) and difference < timedelta(hours=48) :
                group2[1] += 1
            elif difference >= timedelta(hours=48) and difference < timedelta(hours=72) :
                group2[2] += 1
            elif difference >= timedelta(hours=72) and difference < timedelta(hours=96) :
                group2[3] += 1
            elif difference >= timedelta(hours=96) and difference < timedelta(hours=120) :
                group2[4] += 1
            elif difference >= timedelta(hours=120) and difference < timedelta(hours=144) :
                group2[5] += 1
            else :
                group2[6] += 1

        print group1
        print group2

        import numpy as np
        import matplotlib.pyplot as plt

        N = 7

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, group1[::-1], width, color='b')

        rects2 = ax.bar(ind+width, group2[::-1], width, color='r')

        ax.set_ylabel('Frequency')
        ax.set_xlabel('Past 7 days till now -->')
        ax.set_title("Hashtags '%s' and '%s' used per day" % (q1, q2))
        ax.set_xticks(ind+width)
        ax.set_xticklabels( ('6', '5', '4', '3', '2', '1', '0') )
        axes = plt.gca()
        axes.set_ylim([0,max(max(group1), max(group2))*1.10]) #Determines range y-axis, by checking for the max result and add 10% for some white space on top of the barplot

        ax.legend( (rects1[0], rects2[0]), ('%s'% q1, '%s' % q2) )

        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                        ha='center', va='bottom')

        #autolabel(rects1)
        #autolabel(rects2)

        plt.plot()
        plt.draw()
        plt.figure()


        from line_chart import line_chart
        line_chart(group1, group2, q1, q2)

        return group1, group2

    else:
        return group1






