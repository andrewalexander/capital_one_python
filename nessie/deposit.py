import json
import requests
import config


class Deposit():
    """
    Deposit class - get/create/update deposits
    """

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
        """
        Get deposit description for given deposit ID

        Args:
            deposit_id: ID of the deposit to fetch
        Returns:
            dict of status code (200) and deposit description
        """
        url = '%s/deposits/%s?key=%s' % (self.base_url, deposit_id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'deposit': response.json()
        }

    def update_deposit(self, deposit_id, deposit):
        """
        Update metadata associated with a deposit

        NOTE:
            This will return a 404 if the deposit status is 'executed'
            or 'cancelled', so it should only be called immediately after
            a 'create'.

        Format of PUT request:
        ::
            deposit = {
                'medium': 'balance' | 'rewards',
                'amount': int,
                'description': 'string'
            }

        Args:
            deposit_id: ID of the deposit to update
            deposit: dict containing the updated deposit metadata
        Returns:
            dict of status code (202) and response message from Nessie
        """
        url = '%s/deposits/%s?key=%s' % (self.base_url, deposit_id, self.api_key)
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
        ::
            deposit = {
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

    def delete_deposit(self, deposit_id):
        """
        Delete a deposit

        Args:
            deposit_id: ID of the deposit to delete
        Returns:
            dict of status code (204)
        """
        url = '%s/deposits/%s?key=%s' % (self.base_url, deposit_id, self.api_key)
        response = requests.delete(url)

        return {
            'code': response.status_code
        }