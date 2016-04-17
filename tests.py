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
        response = self.account.get_all_by_type(**context.account['get_all_by_type'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['accounts'], list), msg='Did not get a list of accounts')

    def test_get_one(self):
        response = self.account.get_one(**context.account['get_one'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertIsNotNone(response['account'], msg='Got an empty response')

    def test_get_all_by_customer_id(self):
        response = self.account.get_all_by_customer_id(**context.account['get_all_by_customer_id'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['account'], list), msg='Got an empty response')

    def test_update_account(self):
        response = self.account.update_account(**context.account['update_account'])
        self.assertEqual(response['code'], 202, msg='Received a {} status code'.format(response['code']))
        self.assertIsNotNone(response['message'], msg='Got an empty response')

    def test_create_and_delete_account(self):
        # combined in to one test so no artifacts are left behind
        # create a new account
        response = self.account.create_account(**context.account['create_account'])
        self.assertEqual(response['code'], 201, msg='Received a {} status code'.format(response['code']))
        self.assertIsNotNone(response['message'], msg='Got an empty response')
        self.assertTrue(isinstance(response['objectCreated'], dict), msg='Did not get a response object')

        # delete the account we just created
        response = self.account.delete_account(response['objectCreated']['_id'])
        self.assertEqual(response['code'], 204, msg='Received a {} status code'.format(response['code']))
        self.assertEqual(response['message'], '', msg='Did not get an empty response (expected no response body)')

    # TODO:
    #   - make tests to handle the various exceptions (no API key, bad params, all the various failures the backend could throw, etc)


class TestAtmClass(unittest.TestCase):
    atm = atm.Atm()

    def test_get_all(self):
        response = self.atm.get_all()
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['atms'], list), msg='Did not get a list of ATMs')

    def test_get_all_by_location(self):
        response = self.atm.get_all_by_location(**context.atm['get_all_by_location'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['atms'], list), msg='Did not get a list of ATMs')

    def test_get_one(self):
        response = self.atm.get_one(**context.atm['get_one'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['atm'], dict), msg='Could not get ATM description')


class TestBillClass(unittest.TestCase):
    bill = bill.Bill()

    def test_get_all_by_account_id(self):
        response = self.bill.get_all_by_account_id(**context.bill['get_all_by_account_id'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['bills'], list), msg='Did not get a list of bills')

    def test_get_all_by_customer_id(self):
        response = self.bill.get_all_by_customer_id(**context.bill['get_all_by_customer_id'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['bills'], list), msg='Did not get a list of bills')

    def test_get_one(self):
        response = self.bill.get_one(**context.bill['get_one'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['bill'], dict), msg='Did not get bill')

    def test_update_bill(self):
        response = self.bill.update_bill(**context.bill['update_bill'])
        self.assertEqual(response['code'], 202, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['message'], basestring), msg='Did not get a response')

    def test_create_and_delete_bill(self):
        response = self.bill.create_bill(**context.bill['create_bill'])
        self.assertEqual(response['code'], 201, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['message'], basestring), msg='Did not get a response')
        self.assertTrue(isinstance(response['objectCreated'], dict), msg='Did not get a response object')

        # delete the bill that was just created
        response = self.bill.delete_bill(response['objectCreated']['_id'])
        self.assertEqual(response['code'], 204, msg='Received a {} status code'.format(response['code']))


class TestCustomerClass(unittest.TestCase):
    customer = customer.Customer()

    def test_get_all(self):
        response = self.customer.get_all()
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['customers'], list), msg='Did not get a list of customers')

    def test_get_one(self):
        response = self.customer.get_one(**context.customer['get_one'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['customer'], dict), msg='Did not get a customer')

    def test_get_one_by_account_id(self):
        response = self.customer.get_one_by_account_id(**context.customer['get_one_by_account_id'])
        self.assertEqual(response['code'], 200, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['customer'], dict), msg='Did not get a customer')

    def test_update_customer(self):
        response = self.customer.update_customer(**context.customer['update_customer'])
        self.assertEqual(response['code'], 202, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['message'], basestring), msg='Did not get a response')

    def test_create_customer(self):
        response = self.customer.create_customer(**context.customer['create_customer'])
        self.assertEqual(response['code'], 201, msg='Received a {} status code'.format(response['code']))
        self.assertTrue(isinstance(response['message'], basestring), msg='Did not get a response')
        self.assertTrue(isinstance(response['objectCreated'], dict), msg='Did not get a response object')


if __name__ == '__main__':
    fullTestSuite = unittest.TestLoader().loadTestsFromTestCase(TestAccountClass)
    fullTestSuite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAtmClass))
    fullTestSuite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBillClass))
    fullTestSuite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCustomerClass))
    unittest.TextTestRunner(verbosity=2).run(fullTestSuite)

