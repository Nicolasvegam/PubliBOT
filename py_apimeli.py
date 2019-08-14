import requests
import json
import urllib.request
import os

class MELIntegration:

    def get_data(self, query):

        text = requests.get(query)
        data = json.loads(text.text)
        return data

    def filter(self, query, to):
        obj = None
        data = self.get_data(query)
        if data:
            for tm in data:
                for to_ in tm['brands']:
                    if to_['name'].lower() == to.lower():
                        obj = to_
            if obj:
                for pict in obj['pictures']:
                    urllib.request.urlretrieve(pict["url"], "images" + os.sep + "{0}.png".format(pict["name"]))

#a = MELIntegration()
#cust_id = 330426443
#to = 'Lippi'
#b = a.give_urls('https://api.mercadolibre.com/sites/MLC/brands', cust_id, to)
#b = a.filter('https://api.mercadolibre.com/sites/MLC/brands', to)
