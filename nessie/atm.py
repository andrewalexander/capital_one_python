import json
import requests


class Atm():
    base_url = 'http://api.reimaginebanking.com:80'
    url_with_entity = base_url + '/atms'
    api_key = 'ff1fbfb0f1bfaefb769e25299805ddf1'  # test API key

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
