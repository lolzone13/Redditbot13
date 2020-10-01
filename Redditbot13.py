#redditbot13
import time
import random
import praw



def login():
    print("Establishing a connection")
    reddit = praw.Reddit(client_id ='rJsWxciCOfn_eQ',client_secret ='lYTyCSCHgiV1-qMFZ0y7Fme_xI4',
                         username='goodbot13',password='!!Password1234#',user_agent='goodbot')

    print("Connected")
    return reddit

def main():
    a=login()

    subreddit = a.subreddit('bottesting')

    for submission in subreddit.stream.submissions():
        commanddetect(submission)

def commanddetect(submission):
    command='!comm'
    for top_level_comment in submission.comments:


        if command in top_level_comment.body:
            print('found')
            l=['All our dreams can come true, if we have the courage to pursue them.',
            'The secret of getting ahead is getting started.',
            'The best time to plant a tree was 20 years ago.The second best time is now.',
            'Only the paranoid survive.',
            'If people are doubting how far you can go, go so far that you can’t hear them anymore.',
            'Write it.Shoot it.Publish it.Crochet it, sauté it, whatever.MAKE.',

            'Everything you can imagine is real.',
            'Do one thing every day that scares you.',
            'Whatever you are, be a good one.',
            'Hold the vision, trust the process.']




            rand=random.randint(0,9)
            top_level_comment.reply(l[rand])

            print("this worked")
            break

while True:

    main()

