import json
import requests


class Customer():
    base_url = 'http://api.reimaginebanking.com:80'
    url_with_entity = base_url + '/customers'
    url_with_account_entity = base_url + '/accounts'
    api_key = 'ff1fbfb0f1bfaefb769e25299805ddf1'  # test API key

    # GET

    def getAll(self):
        url = '%s?key=%s' % (self.url_with_entity, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    def getOne(self, cust_id):
        url = '%s/%s?key=%s' % (self.url_with_entity, cust_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    def get_one_by_account_id(self, acc_id):
        url = '%s/%s/customer?key=%s' % (self.url_with_account_entity, acc_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    # PUT

    # Customer format
    # {
    # 'address': {
    # 'street_number': "",
    # 'street_name': "",
    # 'city': "",
    # 'state': "",
    # 'zip': ""
    # }
    # }

    def update_customer(self, cust_id, customer):
        url = '%s/%s?key=%s' % (self.url_with_entity, cust_id, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.put(url, params=params, data=json.dumps(customer), headers=headers)
        return response

    # POST
    # Customer format
    # {
    # 'first_name': "",
    # 'last_name': "",
    # 'address': {
    # 'street_number': "",
    # 'street_name': "",
    # 'city': "",
    # 'state': "",
    # 'zip': ""
    # }
    # }

    def create_customer(self, customer):
        url = '%s?key=%s' % (self.url_with_entity, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.post(url, params=params, data=json.dumps(customer), headers=headers)
        return response


c = Customer()
cust_id = '555bed95a520e036e52b23c1'
acc_id = '555bed95a520e036e52b262e'
payload = {
    'address': {
        'street_number': '123',
        'street_name': 'Birchtree Court',
        'city': 'State College',
        'state': 'PA',
        'zip': '16801'
    }
}
create_payload = {
    'first_name': 'Cy',
    'last_name': 'Young',
    'address': {
        'street_number': '111',
        'street_name': 'Baseball Ave',
        'city': 'NYC',
        'state': 'NY',
        'zip': '12345'
    }
}
# print c.get_all()
# print c.get_one(cust_id)
# print c.get_one_by_account_id(acc_id)
# print c.update_customer(cust_id, payload)			# 401 unauthorized
# print c.create_customer(create_payload)				# 401 unauthorized
