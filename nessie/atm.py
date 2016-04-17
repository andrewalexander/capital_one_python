import json
import requests
import config


class Atm:

    def __init__(self):
        self.base_url = config.base_url
        self.url_with_entity = self.base_url + '/atms'
        self.api_key = config.api_key  # test API key

    # GET

    def get_all(self):
        url = '%s?key=%s' % (self.url_with_entity, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    def get_all_by_location(self, lat, lng, rad):
        url = ('%s?lat=%s&lng=%s&rad=%s&key=%s') % (self.url_with_entity, lat, lng, rad, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    def getOne(self, id):
        url = '%s/%s?key=%s' % (self.url_with_entity, id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

        # Test Data
        # atm = Atm()
        # print atm.get_all()
        # print atm.get_all_by_location(38.882163, -77.1113105, 1)
        # print atm.get_one('555bed94a520e036e52b1d7b')
