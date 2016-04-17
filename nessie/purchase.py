import requests
import json


class Purchase():
    base_url = "http://api.reimaginebanking.com:80"
    url_with_entity = base_url + "/purchases"
    api_key = 'ff1fbfb0f1bfaefb769e25299805ddf1'  # test API key

    # GET

    def get_all_by_account_id(self, acc_id):
        url = '%s/accounts/%s/purchases?key=%s' % (self.base_url, acc_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))  # returns json data as a list type
        return data

    def get_one(self, purch_id):
        url = '%s/%s?key=%s' % (self.url_with_entity, purch_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))  # returns json data as a list type
        return data

    # POST

    def create_purchase(self, acc_id, purchase):
        url = '%s/accounts/%s/purchases?key=%s' % (self.base_url, acc_id, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.post(url, params=params, data=json.dumps(purchase), headers=headers)
        return response

    # PUT

    def update_purchase(self, purch_id, purchase):
        url = '%s/%s?key=%s' % (self.url_with_entity, purch_id, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.put(url, params=params, data=json.dumps(purchase), headers=headers)
        return response.content

    # DELETE
    def delete_purchase(self, purch_id):
        url = '%s/%s?key=%s' % (self.url_with_entity, purch_id, self.api_key)
        response = requests.delete(url)
        return response.content
