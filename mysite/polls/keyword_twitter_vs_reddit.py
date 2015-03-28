from reddit_search import reddit_search
from hashtag_comparison import hashtag_comparison
from twitter_login import twitter_login
from line_chart import line_chart

#Compare 1 keyword in multiple sources
def keyword_twitter_vs_reddit(q1):

    max_iterations = 100
    reddit_dataset_q1 = [0,0,0,0,0,0,0]
    twitter_dataset_q1 = [0,0,0,0,0,0,0]

    reddit_dataset_q1 = reddit_search(q1, max_iterations) #reddit does not use hashtags
    twitter_dataset_q1 = hashtag_comparison(q1)
    line_chart(reddit_dataset_q1, twitter_dataset_q1, '%s (Reddit)' % q1, '%s (Twitter' %q1)

