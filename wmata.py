import datetime
import urllib
import json

class WmataError(Exception):
    pass

class Wmata(object):

    api_url = 'http://api.wmata.com/%(svc)s.svc/json/%(endpoint)s'

    # By default, we'll use the WMATA demonstration key
    def __init__(self, api_key='kfgpmgvfgacx98de9q3xazww'):
        if api_key is not None:
            self.api_key = api_key
