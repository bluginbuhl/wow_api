#!/usr/bin/env/ python
# encoding: utf-8

import requests
import json


def getToken(client_ID, client_secret):
    """Makes a POST request to Blizzard API to get an access token.
    Requires an API token and secret
    """
    token_url = "https://us.battle.net/oauth/token"
    token_data = {
        'grant_type': "client_credentials"
    }
    
    token_response = requests.post(token_url, data=token_data, auth=(client_ID, client_secret))
 
    if token_response.ok:
        return token_response.json()['access_token']
    else:
        return "Failed to retrieve token. Reason given: " + token_response.reason