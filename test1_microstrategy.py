import requests
import json
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np

#105773011 código de página Ad Manager

### Parameters ###
#username = 'core'
#password = 'core2k'
#iserver = '10.4.113.99'
#projectId = 'B19DEDCC11D4E0EFC000EB9495D0F44F'
#projectName = 'MicroStrategy Tutorial'
#baseURL = "http://bi.mercadolibre.com/MicroStrategyLibrary/api/" #replace with your own URL for MicroStrategy Library AP

username = 'Administrator'
password = ''
iserver = '10.4.0700.0140'
projectId = 'B19DEDCC11D4E0EFC000EB9495D0F44F'
projectName = 'MicroStrategy Tutorial'
baseURL = "http://bi.mercadolibre.com/MicroStrategyLibrary/api/" #replace with your own URL for MicroStrategy Library API

def login(baseURL,username,password):
    """
    Authenticate a user and create an HTTP session on the web server.
    
    Parameters:
    -----------
    baseURL, username, password
    
    Returns:
    --------
    authToken and sessionId.
    
    Example:
    --------
    authToken, cookies = login(baseURL, username, password)
    """
    header = {'username': username,
                'password': password,
                'loginMode': 1}
    r = requests.post(baseURL + 'auth/login', data=header)
    if r.ok:
        authToken = r.headers['X-MSTR-AuthToken']
        cookies = dict(r.cookies)
        print("Token: " + authToken)
        print("Session ID: {}".format(cookies))
        return authToken, cookies
    else:
        print("HTTP {} - {}, Message {}".format(r.status_code, r.reason, r.text))
        return []

authToken, cookies = login(baseURL,username,password)
