# Config file for the appwide variables

# The FB access token, get one from developers.facebook.com/tools/explorer/
token = "CAACEdEose0cBADW2rWGGqdE0sRkczpYHHx8QskmTDlGKu9ga5u76QT3JHmdNRg9WqvOisje0BeqZA03ZBRJ78BeL7TjUyaVfBVbpaZAMrQzS0ZCPVKyGEZCBHvRhBsBvFWCoMfPQtMZBIvKB1wZCNXYvijEBCPBxadrcIOPCSCOvHaJ11kgYY8RDzImUO7fZA3oBLJyoHH0X4gZDZD"

# List of the FB usernames from which we will gather information
listOfCandidates = [
                    "berniesanders",
                    "hillaryclinton",
                    "JohnKasich",
                    "DonaldTrump",
                    "tedcruzpage"
                    ]

# Supported extra fields:
# "full_picture", "icon", "instagram_eligibility", "link", "message",
# "name", "object_id", "picture", "status_type", "timeline_visibility",
# "type", "updated_time", "full_picture", "icon", "story", "caption", "source"

# List of the post fields used in the request to the facebook API
listOfExtraPostFields = []

# Should we delete the files in the Data folder before this iteration
clearDataFolder = True

# The time during which the program will gather posts from FB (in seconds)
timeout = 60
