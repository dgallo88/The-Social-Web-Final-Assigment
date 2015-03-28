from hashtag_comparison import hashtag_comparison
from reddit_search import reddit_search
from line_chart import line_chart

def two_keywords_twitter_and_reddit(q1, q2):

    #iterations (for every result page (100 results) an iteration)
    max_iterations = 5

    #Create empty datasets
    reddit_dataset_q1 = [0,0,0,0,0,0,0]
    reddit_dataset_q2 = [0,0,0,0,0,0,0]
    twitter_dataset_q1 = [0,0,0,0,0,0,0]
    twitter_dataset_q2 = [0,0,0,0,0,0,0]
    total_dataset_q1 = [0,0,0,0,0,0,0]
    total_dataset_q2 = [0,0,0,0,0,0,0]


    #Compare 2 keywords using multiple sources
    reddit_dataset_q1 = reddit_search(q1, max_iterations)
    reddit_dataset_q2 = reddit_search(q2, max_iterations)
    twitter_dataset_q1, twitter_dataset_q2 = hashtag_comparison("#%s"% q1,"#%s"% q2)
    total_dataset_q1 = [sum(i) for i in zip(reddit_dataset_q1,twitter_dataset_q1)]
    total_dataset_q2 = [sum(e) for e in zip(reddit_dataset_q2,twitter_dataset_q2)]
    line_chart(total_dataset_q1, total_dataset_q2, '%s (Reddit+Twitter)' %q1, '%s (Reddit+Twitter)' % q2)
