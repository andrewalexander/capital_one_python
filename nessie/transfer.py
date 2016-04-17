import requests
import json


class Transfer():
    base_url = "http://api.reimaginebanking.com:80"
    acc_base_url = base_url + "/accounts"
    trans_base_url = base_url + "/transfers"
    api_key = 'ff1fbfb0f1bfaefb769e25299805ddf1'

    # GET

    def get_all_by_account_id(self, acc_id):
        url = '%s/%s/transfers?key=%s' % (self.acc_base_url, acc_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))  # returns json data as a list type
        return data

    def get_all_by_type(self, acc_id, transType):
        url = '%s/%s/transfers?type=%s&key=%s' % (self.acc_base_url, acc_id, transType, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))  # returns json data as a list type
        return data

    def get_one(self, trans_id):
        url = '%s/%s?key=%s' % (self.trans_base_url, trans_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))  # returns json data as a list type
        return data

    # POST

    def create_transfer(self, acc_id, transfer):
        url = '%s/%s/transfers?key=%s' % (self.acc_base_url, acc_id, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.post(url, params=params, data=json.dumps(transfer), headers=headers)
        return response

    # PUT

    def update_transfer(self, trans_id, transfer):
        url = '%s/%s?key=%s' % (self.trans_base_url, trans_id, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.put(url, params=params, data=json.dumps(transfer), headers=headers)
        return response.content

    # DELETE

    def delete_transfer(self, trans_id):
        url = '%s/%s?key=%s' % (self.trans_base_url, trans_id, self.api_key)
        response = requests.delete(url)
        return response.content
