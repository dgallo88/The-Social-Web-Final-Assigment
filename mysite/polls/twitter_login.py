
def twitter_login():

    # import twitter
    # CONSUMER_KEY = 'Kp1f3hTNbezaAmbD5MCP6Z02l'
    # CONSUMER_SECRET = 'XAUFxgloIdFxMSd1Wnr2T6wsPK8BqjIYth85AYbIKmEIh77XCS'
    # OAUTH_TOKEN = '421413363-Mh7mMTmojDYfdwisc9ja52tidkvf4gFKXivUj1ng' # to get the oauth credential you need to click on the 'Create my access token' button and wait few moments
    # OAUTH_TOKEN_SECRET = 'TlTh5z87I3KiCAWiMAM3m0D27PCIsW7xWm365E202VIx3'
    # auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
    # twitter_api = twitter.Twitter(auth=auth)

    import twitter # Tell Python to use the twitter package
    CONSUMER_KEY = 'XSESgSV3kvZfTlodec4V265Qz'
    CONSUMER_SECRET = 'QqguXvjtCZEPxzJIOHfz0KnbHlfE3GoFWnjOhCXq6eNWjZh4PT'
    OAUTH_TOKEN = '41223011-Ii5zpcmeCf2jGTIavKwJN3z08M25tgv1xxj1ADe8i' # to get the oauth credential you need to click on the 'Create my access token' button and wait few moments
    OAUTH_TOKEN_SECRET = 'pUEnj8AtOk8VLNdEW14TVbpo3VC608D1nGOTLBDG3BR7h'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)

    return twitter_api