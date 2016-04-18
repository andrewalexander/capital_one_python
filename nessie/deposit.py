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

    def update_deposit(self, deposit_id, deposit):
        """
        Update metadata associated with a deposit

        Format of PUT request:
        'deposit': {
            'medium': 'balance' | 'rewards',
            'amount': int,
            'description': 'string'
            }
        }

        Args:
            deposit_id: ID of the deposit to update
            deposit: dict containing the updated deposit metadata
        Returns:
            dict of status code (202) and response message from Nessie
        """
        url = '%s/deposits/%s?key=%s' % (self.url_with_entity, deposit_id, self.api_key)
        headers = {'content-type': 'application/json'}
        response = requests.put(url, params=None, data=json.dumps(deposit), headers=headers)

        return {
            'code': response.status_code,
            'message': response.json().get('message', None)
        }

    def create_deposit(self, acc_id, deposit):
        """
        Create a new deposit to an acc_id

        Format of POST request:
        'deposit': {
            'medium': 'balance' | 'rewards',
            'transaction_date': 'YYYY-MM-DD',
            'status': 'pending' | 'cancelled' | 'recurring',
            'amount': int,
            'description': 'string'
        }

        Args:
            acc_id: ID of the account to dump the new deposit into
            deposit: dict containing the new deposit metadata
        Returns:
            dict of status code (201) and response object from Nessie
        """
        url = '%s/%s/deposits?key=%s' % (self.url_with_entity, acc_id, self.api_key)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=None, data=json.dumps(deposit), headers=headers)

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
            'code': response.status_code
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
