import unittest
from nessie import *
from test_data import context


class TestAccountClass(unittest.TestCase):
    account = account.Account()

    def test_get_all(self):
        response = self.account.get_all()
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['accounts'], list), msg='Did not get a list of accounts')

    def test_get_all_by_type(self):
        response = self.account.get_all_by_type('Credit Card')
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['accounts'], list), msg='Did not get a list of accounts')

    def test_get_one(self):
        response = self.account.get_one(context.account['acc_id'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertIsNotNone(response['account'], msg='Got an empty response')

    def test_get_all_by_customer_id(self):
        response = self.account.get_all_by_customer_id(context.account['cust_id'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['account'], list), msg='Got an empty response')

    def test_update_account(self):
        response = self.account.update_account(context.account['acc_id'], context.account['put_data'])
        self.assertEqual(response['code'], 202, msg='Received a {} status code'.format(response['code']))
        self.assertIsNotNone(response['message'], msg='Got an empty response')

    def test_create_and_delete_account(self):
        # combined in to one test so no artifacts are left behind
        # create a new account
        response = self.account.create_account(context.account['cust_id'], context.account['post_data'])
        self.assertEqual(response['code'], 201, msg='Received a {} status code'.format(response['code']))
        self.assertIsNotNone(response['message'], msg='Got an empty response')

        # delete the account we just created
        response = self.account.delete_account(response['objectCreated']['_id'])
        self.assertEqual(response['code'], 204, msg='Received a {} status code'.format(response['code']))
        self.assertEqual(response['message'], '', msg='Did not get an empty response (expected no response body)')


if __name__ == '__main__':
    accountTestSuite = unittest.TestLoader().loadTestsFromTestCase(TestAccountClass)
    unittest.TextTestRunner(verbosity=2).run(accountTestSuite)

