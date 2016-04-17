import requests
import json


class Withdrawal():
    base_url = 'http://api.reimaginebanking.com:80'
    url_with_entity = base_url + '/accounts'
    api_key = 'ff1fbfb0f1bfaefb769e25299805ddf1'  # test API key

    # GET

    def get_all_by_account(self, acc_id):
        url = '%s/%s/withdrawals?key=%s' % (self.url_with_entity, acc_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    def get_one(self, withdrawal_id):
        url = '%s/withdrawals/%s?key=%s' % (self.url, withdrawal_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    # PUT
    # Withdrawal format
    # {
    # 'medium': "",
    # 'amount': 0,
    # 'description': ""
    # }

    def update_withdrawal(self, withdrawal_id, withdrawal):
        url = '%s/withdrawals/%s?key=%s' % (self.url_with_entity, withdrawal_id, self.api_key)
        headers = {
            'Authorization': 'Token token=<ff1fbfb0f1bfaefb769e25299805ddf1>',
            'content-type': 'application/json'
        }
        params = {'key': self.api_key}
        response = requests.put(url, params=params, data=json.dumps(withdrawal), headers=headers)
        return response

    # POST
    # Withdrawal format
    # {
    # 'medium': "",
    # 'amount': 0,
    # 'transaction_date': "",
    # 'status': "",
    # 'description': ""
    # }

    def create_withdrawal(self, to_acc, withdrawal):
        url = '%s/%s/withdrawals?key=%s' % (self.url_with_entity, to_acc, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.post(url, params=params, data=json.dumps(withdrawal), headers=headers)
        return response

    # DELETE

    def delete_withdrawal(self, withdrawal_id):
        url = '%s/withdrawals/%s?key=%s' % (self.url_with_entity, acc_id, withdrawal_id, self.api_key)
        response = requests.delete(url)
        return response.content


# Test Data
w = Withdrawal()
acc_id = '555bed95a520e036e52b262e'
withdrawal_id = '555d6927c34e2890417b274d'
payload = {
    'medium': 'balance',
    'amount': 4,
    'description': 'successfully updated via update_withdrawal'
}
create_payload = {
    'medium': 'balance',
    'amount': 40,
    'transaction_date': "2015-08-20",
    'status': 'pending',
    'description': 'hello, withdrawal'
}
# print w.get_all_by_account(acc_id)
# print w.get_one(acc_id, withdrawal_id)
# print w.update_withdrawal(acc_id, withdrawal_id, payload)
# print w.create_withdrawal(acc_id, create_payload)
# print w.delete_withdrawal(acc_id, '555d6a83c34e2890417b2750')
