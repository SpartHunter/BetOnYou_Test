from flask import request
platform = None
gamertag = None
url = "https://api.fortnitetracker.com/v1/profile/{}/{}".format(platform, gamertag)
