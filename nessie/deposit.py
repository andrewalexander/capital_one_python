import json
import requests


class Deposit():
    base_url = 'http://api.reimaginebanking.com:80'
    url_with_entity = base_url + '/accounts'
    api_key = 'ff1fbfb0f1bfaefb769e25299805ddf1'  # test API key

    # GET

    def get_all_by_account_id(self, acc_id):
        url = '%s/%s/deposits?key=%s' % (self.url_with_entity, acc_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    def get_one(self, deposit_id):
        url = '%s/deposits/%s?key=%s' % (self.url, deposit_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    # PUT
    # Deposit format
    # {
    # 'medium': "balance or rewards",
    # 'amount': 0,
    # 'description': ""
    # }

    def update_deposit(self, deposit_id, deposit):
        url = '%s/deposits/%s?key=%s' % (self.url_with_entity, deposit_id, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.put(url, params=params, data=json.dumps(deposit), headers=headers)
        return response.content

    # POST
    # Deposit format
    # {
    # 'medium': "balance or rewards",
    # 'transaction_date': "",
    # 'status': "pending or cancelled or recurring",
    # 'amount': 0,
    # 'description': ""
    # }

    def create_deposit(self, toAcc, deposit):
        url = '%s/%s/deposits?key=%s' % (self.url_with_entity, toAcc, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.post(url, params=params, data=json.dumps(deposit), headers=headers)
        return response

    # DELETE
    def delete_deposit(self, acc_id, deposit_id):
        url = '%s/%s/deposits/%s?key=%s' % (self.url_with_entity, acc_id, deposit_id, self.api_key)
        response = requests.delete(url)
        return response


# Test Data
d = Deposit()
acc_id = '555bed95a520e036e52b262e'
deposit_id = '55c8fb422644c1aa10651625'
update_payload = {
    'medium': 'balance',
    'amount': "0",
    'description': 'successful update'
}
# print d.get_all_by_account_id(acc_id)
# print d.getOneByAccountIdDepositId(acc_id, deposit_id)
# want get_one to accept:
#   acc_id
#   deposit_id (opt)?
# print d.update_deposit(acc_id, deposit_id, update_payload)
