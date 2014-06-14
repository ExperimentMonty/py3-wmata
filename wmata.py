import datetime
import urllib
import json

class WmataError(Exception):
    pass

class Wmata(object):

    base_url = 'http://api.wmata.com/%(svc)s.svc/json/%(endpoint)s'
    # By default, we'll use the WMATA demonstration key
    api_key = 'kfgpmgvfgacx98de9q3xazww' 

    def __init__(self, api_key=None):
        if api_key is not None:
            self.api_key = api_key