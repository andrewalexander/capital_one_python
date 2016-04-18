import json
import requests
import config


class Bill():
    """ 
    Bill class - get/create/update bills for customer or account
    
    """

    def __init__(self):
        self.base_url = config.base_url
        self.account_base_url = self.base_url + "/accounts"
        self.cust_base_url = self.base_url + "/customers"
        self.api_key = config.api_key

    def get_all_by_account_id(self, acc_id):
        """
        Get all bills associated with the given account ID

        Args:
            acc_id: Account ID to fetch all bills for
        Returns:
            dict with status code and list of bills
        """
        url = '%s/%s/bills?key=%s' % (self.account_base_url, acc_id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'bills': response.json()
        }

    def get_one(self, bill_id):
        """
        Get a single bill description from given bill ID

        Args:
            bill_id: ID of bill to fetch
        Returns:
            dict of status code and single bill
        """
        url = '%s/bills/%s?key=%s' % (self.base_url, bill_id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'bill': response.json()
        }

    def get_all_by_customer_id(self, cust_id):
        """
        Get all bills associated with the given customer ID

        Args:
            cust_id: ID of the customer to fetch the bills for
        Returns:
            dict of status code and list of bills
        """
        url = '%s/%s/bills?key=%s' % (self.cust_base_url, cust_id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'bills': response.json()
        }

    def update_bill(self, bill_id, bill):
        """
        Update metadata associated with a bill.
        
        Format for PUT Request:
        ::
            {
                'status': 'pending' | 'cancelled' | 'completed' | 'recurring' ,
                'payee': 'string',
                'nickname': 'string',
                'payment_date': 'YYYY-MM-DD',
                'recurring_date': int [1-31],
                'payment_amount': int
            }


        Args:
            bill_id: ID of the bill to update
            bill: dict containing the new metadata for the bill
        Returns:
            dict with status code (202) and response from Nessie backend
        """
        url = '%s/bills/%s?key=%s' % (self.base_url, bill_id, self.api_key)
        headers = {'content-type': 'application/json'}
        response = requests.put(url, params=None, data=json.dumps(bill), headers=headers)

        return {
            'code': response.status_code,
            'message': response.json().get('message', None)
        }

    def create_bill(self, acc_id, bill):
        """
        Create a new bill inside a given account

        Format for POST Request:
        ::
            {
              'status': 'pending' | 'cancelled' | 'completed' | 'recurring' ,
              'payee': 'string',
              'nickname': 'string',
              'payment_date': 'YYYY-MM-DD',
              'recurring_date': int [1-31],
              'payment_amount: int
            }

        Args:
            acc_id: ID of the account where bill will be added
            bill: dict containing the new metadata for the bill
        Returns:
            dict with status code (201) and response object from Nessie backend
        """
        url = '%s/%s/bills?key=%s' % (self.account_base_url, acc_id, self.api_key)
        headers = {'content-type': 'application/json'}
        # params = {'key': self.api_key}
        response = requests.post(url, params=None, data=json.dumps(bill), headers=headers)

        return {
            'code': response.status_code,
            'message': response.json().get('message', None),
            'objectCreated': response.json().get('objectCreated', None)
        }

    def delete_bill(self, bill_id):
        """
        Delete bill for given bill ID

        Args:
            bill_id: ID of the bill to delete
        Returns:
            dict with status code (204)
        """
        url = '%s/bills/%s?key=%s' % (self.base_url, bill_id, self.api_key)
        response = requests.delete(url)
        return {
            'code': response.status_code
        }
