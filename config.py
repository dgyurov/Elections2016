# Config file for the appwide variables

# The FB access token, get one from https://developers.facebook.com/tools/explorer/
token = "EAACEdEose0cBAIwFNa5wv26cVa0l0R65foALJUMdTCbGibJKwquyl4IsL8IiBIMERmpf7ZAkn3lrLxZAfhSEw3LnsyeHMjH9Ew2S9oZCydNDd4m0FZCsZC07kjR4KZC3J6ZAmjACwJ2gFsmjaS72ijMZBG3CdTvdN7ZBOm35e70taRwZDZD"

# List of the FB usernames from which we will gather information
listOfCandidates = [
                    "berniesanders",
                    "hillaryclinton",
                    "JohnKasich",
                    "DonaldTrump",
                    "tedcruzpage"
                    ]

# List of the post fields used in the request to the facebook API
# Supported ExtraFields:
# "full_picture"
# "icon"
# "instagram_eligibility"
# "link"
# "message" Might have some parsing problems
# "name"  Might have some parsing problems
# "object_id"
# "picture"
# "status_type"
# "timeline_visibility"
# "type"
# "updated_time"
# "full_picture"
# "icon"
# "story"  Might have some parsing problems
# "caption" Might have some parsing problems
# "source"



listOfExtraPostFields = ['caption','message','name']

# Should we delete the files in the Data folder before this iteration
clearDataFolder = True

# The time during which the program will gather posts from FB (in seconds)
timeout = 10
