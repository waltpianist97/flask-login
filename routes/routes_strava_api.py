import os
import urllib
import requests
from flask import Flask, redirect, request, url_for, session
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required


def authorize_url():
    """Generate authorization uri"""
    port = 5000
    app_url = os.environ.get('APP_URL')
    params = {
        "client_id": os.environ.get('STRAVA_CLIENT_ID'),
        "response_type": "code",
        "redirect_uri": f"{app_url}:{port}/authorization_successful",
        "scope": "read,profile:read_all,activity:read",
        "state": 'https://github.com/sladkovm/strava-oauth',
        "approval_prompt": "force"
    }
    values_url = urllib.parse.urlencode(params)
    base_url = 'https://www.strava.com/oauth/authorize'
    rv = base_url + '?' + values_url
    return rv


@app.route("/authorize")
@login_required
def authorize():
    """Redirect user to the Strava Authorization page"""
    return redirect(authorize_url())


@app.route("/authorization_successful")
@login_required
def authorization_successful():
    """Exchange code for a user token"""
    params = {
        "client_id": os.environ.get('STRAVA_CLIENT_ID'),
        "client_secret": os.environ.get('STRAVA_CLIENT_SECRET'),
        "code": request.args.get('code'),
        "grant_type": "authorization_code"
    }
    r = requests.post("https://www.strava.com/oauth/token", params)
    session['strava_token'] = r.json()["access_token"]
    return redirect(url_for("user_profile"))
