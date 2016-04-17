import json
import requests
import config


class Account:
    """
    Account class - get/update account information

    """
    def __init__(self):
        self.base_url = config.base_url
        self.url_with_entity = self.base_url + '/accounts'
        self.api_key = config.api_key

    def get_all(self):
        """
        Get all accounts

        Returns:
            dict with status code (200) and list of all accounts
        """
        url = '%s?&key=%s' % (self.url_with_entity, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'accounts': response.json()
        }

    def get_all_by_type(self, acc_type):
        """
        Filter the get_all by account type

        Args
            acc_type: 'string'
                Valid options: 'Credit Card' | 'Checking' | 'Savings'
        Returns:
            dict with status code and list of all accounts of the requested type
        """
        url = '%s?type=%s&key=%s' % (self.url_with_entity, acc_type, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'accounts': response.json()
        }

    def get_one(self, acc_id):
        """
        Get one account by acc_id

        Args:
            acc_id: account ID to fetch
        Returns:
            dict with status code (200) and the account information for acc_id
        """
        url = '%s/%s?key=%s' % (self.url_with_entity, acc_id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'account': response.json()}

    def get_all_by_customer_id(self, cust_id):
        """
        Get all accounts for a customer

        Args:
            cust_id: string for customer ID
        Returns:
            dict with status code (200) and list of accounts for cust_id
        """
        url = '%s/customers/%s/accounts?key=%s' % (self.base_url, cust_id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'account': response.json()
        }

    def update_account(self, acc_id, request_data):
        """
        Updates account information for specified acc_id

        Format for PUT request:
        {
            'nickname': 'some string here'
        }

        Args:
            acc_id: account ID for account to update
            request_data: dict of PUT data following the format above
        Returns:
            dict with status code (202) and response message from Nessie backend
        """
        url = '%s/%s' % (self.url_with_entity, acc_id)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.put(url, params=params, data=json.dumps(request_data), headers=headers)

        return {
            'code': response.status_code,
            'message': response.json()['message']
        }

    def create_account(self, cust_id, request_data):
        """
        Creates a new account for cust_id using the details in request_data

        Format for POST request:
        {
            'type': 'Checking' | 'Credit Card',
            'nickname': 'string',
            'rewards': int,
            'balance': float
        }

        Args:
            cust_id: The owner of the new account we are creating
            request_data: The dict containing the details of the new account following the format above
        Returns:
             dict with status code (201) and response object from Nessie backend with details about created object:
             {
                "code": 201,
                "message": "Account created",
                "objectCreated": {
                    "type": "Credit Card",
                    "nickname": "Brand New test Account",
                    "rewards": 0,
                    "balance": 0,
                    "customer_id": "string",
                    "_id": "string"
                }
             }
        """
        url = '%s/customers/%s/accounts?key=%s' % (self.base_url, cust_id, self.api_key)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=None, data=json.dumps(request_data), headers=headers).json()

        return {
            'code': response['code'],
            'message': response['message'],
            'objectCreated': response['objectCreated']
        }

    def delete_account(self, acc_id):
        """
        Delete the account specified by acc_id

        Args:
            acc_id: The account ID to delete
        Returns:
             dict with status code (204) and empty response
        """
        url = '%s/%s?key=%s' % (self.url_with_entity, acc_id, self.api_key)
        response = requests.delete(url)

        return {
            'code': response.status_code,
            'message': response.content
        }
