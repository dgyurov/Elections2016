import requests
import json

token = "CAACEdEose0cBAGlV9xkyZAN2oY5mxkbJ3lsj4ZCwVhAFKkjqglRzPXVFZCCnjKP8KZCGkeKGZCkXc4MzL4EZCBFjIlLeeZCyLL52QjZCw0afAxfpZClNLu8oa8QSjOZC1zf5opp9shoRBHCfPX0tQtECZBQuZCKXPYc9ZBFlQxy94tALYdT53ZCZCt9SrHBqancOX19VqOcHnpPMgvctwZDZD"
base ="https://graph.beta.facebook.com/v2.5/"
profile = "DonaldTrump"
apiSearch = "posts.limit(100){likes.limit(0).summary(true),message}"
url = base+profile+"?fields="+apiSearch+"&access_token="+token

request = requests.get(url)

json = request.json()

data = json['posts']['data']
newsArr = []

for i in range(0,len(data)):
	try:
		newsArr.append({"message":data[i]['message'],"likes":data[i]['likes']['summary']['total_count']})
	except Exception, e:
		pass

print newsArr
