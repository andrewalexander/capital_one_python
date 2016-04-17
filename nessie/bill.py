import json
import requests
import config


class Bill():
    def __init__(self):
        self.base_url = config.base_url
        self.account_base_url = self.base_url + "/accounts"
        self.cust_base_url = self.base_url + "/customers"
        self.api_key = config.api_key

    # GET
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
        data = json.loads(str(json.dumps(response.text)))
        return data

    def get_one(self, bill_id):
        url = '%s/bills/%s?key=%s' % (self.base_url, bill_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    def get_all_by_customer_id(self, cust_id):
        url = '%s/%s/bills?key=%s' % (self.cust_base_url, cust_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    # PUT
    # Bill format
    # {
    # 'status': ""
    # 'payee': ""
    # 'nickname': "",
    # 'payment_date': ""
    # 'recurring_date': 15
    # 'payment_amount': 100
    # }

    def update_bill(self, bill_id, bill):
        url = '%s/bills/%s?key=%s' % (self.account_base_url, bill_id, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.put(url, params=params, data=json.dumps(bill), headers=headers)
        return response.content

    # POST
    # Bill format is identical to PUT

    def create_bill(self, acc_id, bill):
        url = '%s/%s/bills?key=%s' % (self.account_base_url, acc_id, self.api_key)
        headers = {'content-type': 'application/json'}
        params = {'key': self.api_key}
        response = requests.post(url, params=params, data=json.dumps(bill), headers=headers)
        return response.content

    # DELETE

    def delete_bill(self, acc_id, bill_id):
        url = '%s/%s/bills/%s?key=%s'
        response = requests.delete(url)
        return response.content


b = Bill()
acc_id = '555bed95a520e036e52b262e'
bill_id = '555d6da5f5bfc41b4443ef9a'
bill_put = {'nickname': 'updated payment'}
cust_id = '555bed95a520e036e52b23c1'
bill_post = {
    'status': 'pending',
    'payee': 'Comcast',
    'nickname': 'monthly payment',
    'payment_date': '2015-08-22',
    'recurring_date': 20,
    'payment_amount': 60
}
# print b.get_all_by_customer_id(cust_id)					# 401 unauthorized
# print b.getOne(acc_id, bill_id)			                # 401 unauthorized
# print b.update_bill(acc_id, bill_id, bill)					# 401 unauthorized			
# print b.create_bill(acc_id, bill)							# 401 unauthorized
