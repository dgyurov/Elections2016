import requests
import atexit
import time
import os.path
import config
import facebook
from threading import Thread

token = config.token
graph = facebook.GraphAPI(access_token=token)
listOfCandidates = config.listOfCandidates
postsRecorded = []


def main():
    print 'Gathering initiated:'
    atexit.register(exit_handler)

    print 'The gathering will end in '+str(config.timeout)+' seconds...'

    for candidate in listOfCandidates:
        postsRecorded.append(0)
        t = Thread(target=output_file, args=(candidate,))
        t.setDaemon(True)
        t.start()
        print 'Started a gathering thread for '+candidate

    # Timeout for auto-gathering
    time.sleep(config.timeout)


def exit_handler():
    output_overview(listOfCandidates)
    print 'The gathering has ended!'


def output_post(post, candidate, f):
    id = post['id']
    created_time = post['created_time']

    if 'status_type' not in post:
        status_type = 'null'
    else:
        status_type = post['status_type']

    # Check if shares exist at first place
    if 'shares' not in post:
        shares = 'null'
    else:
        shares = post['shares']['count']

    likes = post['likes']['summary']['total_count']
    comments = post['comments']['summary']['total_count']
    if not config.listOfExtraPostFields:
        postOutput = str(id)+", "+str(created_time)+", "+str(status_type)+", "+str(likes)+", "+str(shares)+", "+str(comments)
    else:
        postOutput = str(id)+", "+str(created_time)+", "+str(status_type)+", "
        for field in config.listOfExtraPostFields:
            if field not in post:
                postOutput += "null,"
            else:
                fieldContent = post[field]
                fieldContent = ''.join(ch for ch in fieldContent if ch.isalnum() or ch == ' ' or ch == '#' or ch=='?' or ch=='!' or ch=='.' or ch=='@' or ch=='$' or ch=='%' or ch=='' or ch=='/' or ch==':' or ch=='=')
                postOutput += fieldContent.encode('utf-8')+","
        postOutput += str(likes)+", "+str(shares)+", "+str(comments)

    print >>f, postOutput
    postsRecorded[listOfCandidates.index(candidate)] += 1


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

    # Build the request
    if not config.listOfExtraPostFields:
        posts = requests.get("https://graph.facebook.com/v2.5/"+profile['id']+"?fields=posts.limit(100){id,created_time,status_type,shares,likes.limit(0).summary(true),comments.limit(0).summary(true)}&access_token="+token).json()['posts']
    else:
        extraFieldsUnited = ""
        for field in config.listOfExtraPostFields:
            extraFieldsUnited += field+','
        posts = requests.get("https://graph.facebook.com/v2.5/"+profile['id']+"?fields=posts.limit(100){id,created_time,status_type,"+extraFieldsUnited+"shares,likes.limit(0).summary(true),comments.limit(0).summary(true)}&access_token="+token).json()['posts']

    # Take care of the csv header
    if not config.listOfExtraPostFields:
        print >>f, 'id, created_time, status_type, likes, shares, comments'
    else:
        print >>f, 'id, created_time, status_type,'+extraFieldsUnited+' likes, shares, comments'

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
