import json
import requests
import config


class Customer():
    """
    Customer class - get/update customer information
    """

    def __init__(self):
        self.base_url = config.base_url
        self.url_with_entity = self.base_url + '/customers'
        self.url_with_account_entity = self.base_url + '/accounts'
        self.api_key = config.api_key

    def get_all(self):
        """
        Get descriptions for all customers

        Returns:
            dict of status code and list of customers
        """
        url = '%s?key=%s' % (self.url_with_entity, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'customers': response.json()
        }

    def get_one(self, cust_id):
        """
        Get a single customer description

        Args:
            cust_id: ID of the customer to fetch
        Returns:
            dict of status code and the customer description
        """
        url = '%s/%s?key=%s' % (self.url_with_entity, cust_id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'customer': response.json()
        }

    def get_one_by_account_id(self, acc_id):
        """
        Get the customer description from account ID

        Args:
            acc_id: account ID to fetch customer info from
        Returns:
            dict of status code and the customer description
        """
        url = '%s/%s/customer?key=%s' % (self.url_with_account_entity, acc_id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'customer': response.json()
        }

    def update_customer(self, cust_id, customer):
        """
        Update customer information

        Format of PUT request:
         'customer': {
            'address': {
                'street_number': '42',
                'street_name': 'Life Universe Everything Way',
                'city': 'Undefined',
                'state': 'CO',
                'zip': '42424'
            }
        }

        Args:
            cust_id: ID of the customer to update
            customer: dict of updated customer metadata
        Returns:
            dict of status code (202) and message from Nessie backend
        """
        url = '%s/%s?key=%s' % (self.url_with_entity, cust_id, self.api_key)
        headers = {'content-type': 'application/json'}
        # params = {'key': self.api_key}
        response = requests.put(url, params=None, data=json.dumps(customer), headers=headers)

        return {
            'code': response.status_code,
            'message': response.json().get('message', None)
        }

    def create_customer(self, customer):
        """
        Create a new customer

        Format for POST request:
        'customer': {
            'address': {
                'street_number': '1',
                'street_name': 'Infinite Circle',
                'city': 'Nontain View',
                'state': 'CA',
                'zip': '12345'
            },
            'first_name': 'Test',
            'last_name': 'Customer'
        }

        Args:
            customer: dict of new customer metadata
        Returns:
            dict of status code and response object from create
        """
        url = '%s?key=%s' % (self.url_with_entity, self.api_key)
        headers = {'content-type': 'application/json'}
        response = requests.post(url, params=None, data=json.dumps(customer), headers=headers)

        return {
            'code': response.status_code,
            'message': response.json().get('message', None),
            'objectCreated': response.json().get('objectCreated', None)
        }
