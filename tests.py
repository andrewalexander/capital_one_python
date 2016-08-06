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
            nessie.handler.NessieClient(api_key, client_type)

            self.assertTrue(isinstance(e, Exception), 'Did not raise the Exception for invalid API key')

    def test_invalid_client_type(self):
        with open('tests/invalid_client_type.json', 'r') as fh:
            config = json.load(fh)

        api_key = config.get('api_key')
        client_type = config.get('client_type')
        with self.assertRaises(Exception) as e:
            nessie.handler.NessieClient(api_key, client_type)

            self.assertTrue(isinstance(e, Exception), 'Did not raise the Exception for invalid client type')

    def test_valid_input(self):
        with open('tests/valid_input.json', 'r') as fh:
            config = json.load(fh)

        api_key = config.get('api_key')
        client_type = config.get('client_type')
        client = nessie.handler.NessieClient(api_key, client_type)
        self.assertTrue(isinstance(client, nessie.handler.NessieClient), msg='Did not get a valid NessieClient() object')

if __name__ == '__main__':
    fullTestSuite = unittest.TestLoader().loadTestsFromTestCase(TestInput)
    unittest.TextTestRunner(verbosity=2).run(fullTestSuite)

