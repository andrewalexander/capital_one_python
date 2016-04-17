import json
import requests
import config


class Deposit():
    def __init__(self):
        self.base_url = config.base_url
        self.url_with_entity = self.base_url + '/accounts'
        self.api_key = config.api_key

    def get_all_by_account_id(self, acc_id):
        """
        Get all deposits for given account ID

        Args:
            acc_id: ID of account to fetch deposits for
        Returns:
            dict of status code (200) and list of deposits
        """
        url = '%s/%s/deposits?key=%s' % (self.url_with_entity, acc_id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'deposits': response.json()
        }

    def get_one(self, deposit_id):
        url = '%s/deposits/%s?key=%s' % (self.url, deposit_id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'deposit': response.json()
        }

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

        return {
            'code': response.status_code,
            'message': response.json().get('message', None)
        }

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

        return {
            'code': response.status_code,
            'message': response.json().get('message', None),
            'objectCreated': response.json().get('objectCreated', None)
        }

    # DELETE
    def delete_deposit(self, acc_id, deposit_id):
        url = '%s/%s/deposits/%s?key=%s' % (self.url_with_entity, acc_id, deposit_id, self.api_key)
        response = requests.delete(url)

        return {
            'code': response.status_code,
            'deposits': response.json()
        }


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
