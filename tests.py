import unittest
import nessie
import json

class TestInput(unittest.TestCase):
    def test_invalid_api_key(self):
        with open('tests/invalid_api_key.json', 'r') as fh:
            config = json.load(fh)

        api_key = config.get('api_key')
        client_type = config.get('client_type')
        with self.assertRaises(Exception) as e:
            nessie.NessieClient(api_key, client_type)

            self.assertTrue(isinstance(e, Exception), 'Did not raise the Exception for invalid API key')

    def test_invalid_client_type(self):
        with open('tests/invalid_client_type.json', 'r') as fh:
            config = json.load(fh)

        api_key = config.get('api_key')
        client_type = config.get('client_type')
        with self.assertRaises(Exception) as e:
            nessie.NessieClient(api_key, client_type)

            self.assertTrue(isinstance(e, Exception), 'Did not raise the Exception for invalid client type')

    def test_valid_input(self):
        with open('tests/valid_input.json', 'r') as fh:
            config = json.load(fh)

        api_key = config.get('api_key')
        client_type = config.get('client_type')
        client = nessie.NessieClient(api_key, client_type)
        self.assertTrue(isinstance(client, nessie.NessieClient), msg='Did not get a valid NessieClient() object')


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        with open('tests/valid_input.json', 'r') as fh:
            config = json.load(fh)

        api_key = config.get('api_key')
        client_type = config.get('client_type')
        self.client = nessie.NessieClient(api_key, client_type)

    def test_base_endpoint(self):
        # GET /accounts
        response = self.client.api_call('accounts', 'GET')
        accounts = response.get('content')
        account_id = accounts[0].get('_id')
        self.assertEqual(response.get('status_code'), 200)

    def test_endpoint_with_id(self):
        response = self.client.api_call('accounts', 'GET')
        accounts = response.get('content')
        account_id = accounts[0].get('_id')

        # GET /accounts/{id}
        response = self.client.api_call('accounts/{}'.format(account_id), 'GET')
        self.assertEqual(response.get('status_code'), 200)

    def test_secondary_endpoint(self):
        response = self.client.api_call('accounts', 'GET')
        accounts = response.get('content')
        account_id = accounts[0].get('_id')

        # GET /accounts/{id}/purchases
        response = self.client.api_call('accounts/{}/customer'.format(account_id), 'GET')
        self.assertEqual(response.get('status_code'), 200)

    def test_tertiary_endpoint_and_secondary_id(self):
        response = self.client.api_call('accounts', 'GET')
        accounts = response.get('content')
        account_id = accounts[0].get('_id')

        response = self.client.api_call('merchants'.format(account_id), 'GET')
        merchants = response.get('content')
        merchant_id = merchants[0].get('_id')

        # GET /merchants/{merchant_id}/accounts/{account_id}/purchases
        response = self.client.api_call('merchants/{}/accounts/{}/purchases'.format(merchant_id, account_id), 'GET')
        self.assertEqual(response.get('status_code'), 200)

if __name__ == '__main__':
    fullTestSuite = unittest.TestLoader().loadTestsFromTestCase(TestInput)
    fullTestSuite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestEndpoints))
    unittest.TextTestRunner(verbosity=2).run(fullTestSuite)

