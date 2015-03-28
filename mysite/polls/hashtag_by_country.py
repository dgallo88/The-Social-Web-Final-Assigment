from twitter_search import twitter_search

def hashtag_by_country(q):
#q='#happy'
    count = 100

    statuses = twitter_search(q=q, count=count)

    print len(statuses)

    hashtag_by_country = {}
    i=1
    for status in statuses:
        place = status['place']
        if place:
            country = place['country']
            if country:
                if not hashtag_by_country.has_key(country):
                    hashtag_by_country[country]=0
                hashtag_by_country[country]+=1
                i+=1

    print hashtag_by_country

    import operator
    sorted_hashtag_by_country = sorted(hashtag_by_country.items(), reverse=True, key=operator.itemgetter(1))
    print sorted_hashtag_by_country
    print 'Total of countries: ' + str(len(sorted_hashtag_by_country))

    #calculating the top 10 and rest of the world
    topten = sorted_hashtag_by_country[0:10]
    labels=[];
    fracs=[];
    for c in topten:
        labels.append(c[0])
        fracs.append(c[1])
    rest = sorted_hashtag_by_country[11: len(sorted_hashtag_by_country)]
    if len(rest) > 0:
        counter_rest=0
        for r in rest:
            counter_rest+=r[1]
        labels.append('Others')
        fracs.append(counter_rest)

    # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    # fracs = [15, 30, 45, 10]

    from pie_chart import PieChart
    PieChart(labels, fracs)









