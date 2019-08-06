import requests
import json

class Integration:

    def get_data(self, query):

        text = requests.get(query)
        data = json.loads(text.text)

        return data

    def filter_data(self, data, seller):

        selected_data = []

        for element in data["data"]:
            if seller in element[0]:
                selected_data.append(element)

        return selected_data
