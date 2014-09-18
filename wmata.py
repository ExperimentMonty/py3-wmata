import datetime
import urllib
import json

class WmataError(Exception):
    pass

class Wmata(object):

    api_url = 'http://api.wmata.com/%(svc)s.svc/json/%(endpoint)s'

    # By default, we'll use the WMATA demonstration key
    def __init__(self, api_key='kfgpmgvfgacx98de9q3xazww'):
        self.api_key = api_key

    def _get(self, function, arguments):
        pass

    def rail_lines(self):
        pass

    def rail_stations(self):
        pass

    def rail_station_info(self):
        pass

    def rail_station_entrances(self):
        pass

    def rail_path(self):
        pass

    def rail_predictions(self):
        pass

    def rail_incidents(self):
        pass

    def bus_routes(self):
        pass

    def bus_route_schedue(self):
        pass

    def bus_route_details(self):
        pass

    def bus_positions(self):
        pass

    def bus_stops(self):
        pass

    def bus_stop_schedule(self):
        pass

    def bus_prediction(self):
        pass

    def elevator_incidents(self, station_code='All'):
        pass

