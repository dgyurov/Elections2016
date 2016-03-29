import facebook
import requests
import atexit
from threading import Thread
import time
import os.path

token = "CAACEdEose0cBAJh8afXiQuy7nJBXpUJ5AyVAP2BX3flXUAQ58pfbqtvS7CYxZCZApf4ClzCaiNDp7NpupGFE92xcQTksZARxZB82lWWIMyZBwwbZA2jrp4oi3OQZBL9oQ9KljfTfoGrxq6Hs5oOw9EoGZAB9xqLPRBYV6SfPPYJxmWyQLB40hZCDzwWhCV2sJYtZAO19bXQOr0LwZDZD"
graph = facebook.GraphAPI(access_token=token)

listOfCandidates = ["berniesanders",
                    "hillaryclinton",
                    "JohnKasich",
                    "DonaldTrump",
                    "tedcruzpage"]

postsRecorded = [0, 0, 0, 0, 0]


def main():

    atexit.register(exit_handler)

    for candidate in listOfCandidates:
        t = Thread(target=output_file, args=(candidate,))
        t.setDaemon(True)
        t.start()

    time.sleep(60)


def exit_handler():
    output_overview(listOfCandidates)
    print 'The application was ended!'


def output_post(post, candidate, f):
    id = post['id']
    created_time = post['created_time']
    status_type = post['status_type']
    likes = requests.get("https://graph.facebook.com/v2.5/"+post['id']+"?fields=likes.limit(0).summary(true)&access_token="+token).json()['likes']['summary']['total_count']
    shares = requests.get("https://graph.facebook.com/v2.5/"+post['id']+"?fields=shares&access_token="+token).json()['shares']['count']
    comments = requests.get("https://graph.facebook.com/v2.5/"+post['id']+"?fields=comments.limit(0).summary(true)&access_token="+token).json()['comments']['summary']['total_count']

    postOutput = str(id)+", "+str(created_time)+", "+str(status_type)+", "+str(likes)+", "+str(shares)+", "+str(comments)
    print >>f, postOutput
    postsRecorded[listOfCandidates.index(candidate)] += 1
    print("Post added for "+candidate+"!")


def output_overview(candidates):
    f = open(os.path.dirname(__file__)+'/../data/overview.csv', 'w')
    print >>f, 'id, username, likes, numOfPosts'

    for candidate in candidates:
        profile = graph.get_object(candidate)
        numOfPosts = postsRecorded[listOfCandidates.index(candidate)]
        print >>f, str(profile['id'])+", "+str(profile['username'])+", "+str(profile['likes'])+", "+str(numOfPosts)

    f.close()


def output_file(candidate):
    f = open(os.path.dirname(__file__)+'/../data/'+candidate+'.csv', 'w')
    profile = graph.get_object(candidate)
    posts = graph.get_connections(profile['id'], 'posts')

    print >>f, 'id, created_time, status_type, likes, shares, comments'

    while True:
        try:
            for post in posts['data']:
                output_post(post=post, candidate=candidate, f=f)
            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            # When there are no more pages
            break
    f.close()

if __name__ == '__main__':
    # fbsdk.py executed as script
    main()
