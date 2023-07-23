from stravaio import StravaIO, strava_oauth2
from datetime import datetime
from flask import g

def get_strava_client():
    if 'strava_client' not in g:
        # Obtain the access token (You already have this part)
        token = strava_oauth2(client_id=105259, client_secret="1cda7c21f96f8878286a89f0b8ad51779696e062")
        # Create and store the StravaIO client object
        g.strava_client = StravaIO(access_token=token['access_token'])
    return g.strava_client