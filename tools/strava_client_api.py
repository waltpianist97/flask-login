# Replace with the appropriate import
from .stravaio import StravaIO, strava_oauth2


def get_or_create_strava_client():
    # Obtain the access token (You already have this part)
    token = strava_oauth2(
        client_id=105259, client_secret="1cda7c21f96f8878286a89f0b8ad51779696e062")
    # Create and store the StravaIO client object in the session
    strava_client = StravaIO(access_token=token['access_token'])
    return strava_client
