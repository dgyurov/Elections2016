# Config file for the appwide variables

# The FB access token, get one from https://developers.facebook.com/tools/explorer/
token = "EAACEdEose0cBAAwzT63V2txBf8bZArQb6NaJnpVAQGrgmF6FtVEiaizVrhnhrA3oFbm0qBC0VksMdLy9ZCyeo2CGLUkU3crbYRVhYDq6DdJlE8HeoiWEZBslNNgQQW8Kk2ZAYqNo0UyKMToPJTnslMN7kEHjxjZACAKN2drZBqjgZDZD"

# List of the FB usernames from which we will gather information
listOfCandidates = [
                    "berniesanders",
                    "hillaryclinton",
                    "JohnKasich",
                    "DonaldTrump",
                    "tedcruzpage"
                    ]

# Should we delete the files in the Data folder before this iteration
clearDataFolder = True

# The time during which the program will gather posts from FB (in seconds)
timeout = 120
