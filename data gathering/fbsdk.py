import facebook
import requests
import atexit
import thread

token = "CAACEdEose0cBAHBYNFtQoNUdpiMAn8Bmp9JFZB2ltrVP2aU5nglVzXiV77OC7o1wfVU31QxIhEQxAQAHkJq0Q1ws7KOrCeluK84PZCTDi3n0iUGCDboHZBomIdbHb4NG0PxYGVB7hI7xZCleUqavMIhAbZBVkPgdpSd4Ga2jsvk3fN4QctqLVBVt01yYN1dX4ZAJDZCY5aDFwZDZD"
graph = facebook.GraphAPI(access_token=token)

listOfCandidates = ["berniesanders",
                    "hillaryclinton",
                    "JohnKasich",
                    "DonaldTrump",
                    "tedcruzpage"]


def main():
    atexit.register(exit_handler)

    for candidate in listOfCandidates:
        try:
            thread.start_new_thread(output_file(candidate))
        except:
            print "Error occured: unable to start thread for "+candidate


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
    print("Post added for "+candidate+"!")


def output_overview(candidates):
    f = open('results/overview.csv', 'w')
    print >>f, 'id, username, likes, about'

    for candidate in candidates:
        profile = graph.get_object(candidate)
        print >>f, str(profile['id'])+", "+str(profile['username'])+", "+str(profile['likes'])+", "+str(profile['about'])

    f.close()


def output_file(candidate):
    f = open('results/'+candidate+'.csv', 'w')
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

main()
