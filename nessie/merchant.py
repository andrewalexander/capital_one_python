import json
import requests


class Merchant():
    base_url = "http://api.reimaginebanking.com:80"
    url_with_entity = base_url + "/merchants"
    api_key = 'ff1fbfb0f1bfaefb769e25299805ddf1'  # test API key

    # GET

    def get_all(self):
        url = '%s?key=%s' % (self.url_with_entity, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))  # returns json data as a list type
        return data

    def get_all_by_location(self, lat, lng, rad):
        url = '%s?lat=%s&lng=%s&rad=%s&key=%s' % (self.url_with_entity, lat, lng, rad, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    def get_one(self, march_id):
        url = '%s/%s?key=%s' % (self.url_with_entity, march_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    # POST

    def create_merchant(self, merchant):
        url = '%s?key=%s' % (self.url_with_entity, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.post(url, params=params, data=json.dumps(account), headers=headers)
        return response

    # PUT

    def update_merchant(self, march_id, merchant):
        url = '%s/%s?key=%s' % (self.url_with_entity, march_id, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.put(url, params=params, data=json.dumps(account), headers=headers)
        return response.content
