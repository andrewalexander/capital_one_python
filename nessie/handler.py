import requests
import six
import json

VALID_BASE_ENDPOINTS = [
    'accounts',
    'atms',
    'bills',
    'branches',
    'customers',
    'deposits',
    'merchants',
    'purchases',
    'transfers',
    'withdrawals'

]
VALID_SECONDARY_ENDPOINTS = [
    'accounts',
    'bills',
    'customer',
    'deposits',
    'purchases',
    'transfers',
    'withdrawals'
]
VALID_METHODS = [
    'GET',
    'POST',
    'PUT',
    'DELETE'
]
VALID_TYPES = [
    'customer',
    'enterprise'
]

class NessieClient:
    def __init__(self, api_key, client_type):
        self._validate_client_inputs(api_key, client_type)
        self.base_url = 'http://api.reimaginebanking.com/{}'

    def _validate_client_inputs(self, api_key, client_type):
        if len(api_key) == 32:
            self.api_key = api_key
        else:
            raise Exception('Invalid API key passed in to NessieClient: {}'.format(api_key))

        if client_type in VALID_TYPES:
            self.client_type = client_type
        else:
            raise Exception('Invalid client type selected for NessieClient: {}'.format(client_type))

    def _validate_api_inputs(self, endpoint, method):
        if self.client_type == 'enterprise':
            enterprise, base, id, secondary_endpoint, secondary_id, tertiary_endpoint = (endpoint.split('/') + [None]*5)[:6]
            if enterprise != 'enterprise':
                raise Exception('Invalid enterprise endpoint passed to \'api_call\: {}'.format(endpoint))
        else:
            base, id, secondary_endpoint, secondary_id, tertiary_endpoint = (endpoint.split('/') + [None]*4)[:5]


        # split up endpoint into sub-components for validation

        if method not in VALID_METHODS:
            raise Exception('Invalid method passed to \'api_call\': {}'.format(method))

        if base not in VALID_BASE_ENDPOINTS:
            raise Exception('Invalid endpoint passed to \'api_call\': {}'.format(base))

        if id and len(id) != 24:
            raise Exception('Invalid ID in endpoint passed to \'api_call\': {}'.format(id))

        if secondary_endpoint and secondary_endpoint not in VALID_SECONDARY_ENDPOINTS:
            raise Exception('Invalid secondary endpoint passed to \'api_call\': {}'.format(secondary_endpoint))

        if secondary_id and len(secondary_id) != 24:
            raise Exception('Invalid secondary ID in endpoint passed to \'api_call\': {}'.format(id))

        if tertiary_endpoint and tertiary_endpoint not in VALID_SECONDARY_ENDPOINTS:
            raise Exception('Invalid tertiary endpoint passed to \'api_call\': {}'.format(tertiary_endpoint))


    def api_call(self, endpoint, method, payload=None):
        # if any inputs are invalid, an exception will be raised
        self._validate_api_inputs(endpoint, method)

        payload = payload or {}
        url = self.base_url.format(endpoint)
        url_params = {'key': self.api_key}

        try:
            if method == 'GET':
                response = requests.get(url, params=url_params)
            elif method == 'POST':
                response = requests.post(url, params=url_params, json=payload)
            elif method == 'PUT':
                response = requests.put(url, params=url_params, json=payload)
            elif method == 'DELETE':
                response = requests.delete(url, params=url_params)
        except requests.exceptions.ConnectionError as e:
            raise Exception('There was an issue hitting the Nessie API. Stacktrace: {}'.format(e))
        except requests.exceptions.Timeout as e:
            raise Exception('The connection to Nessie timed out. Check your network settings. Stacktrace: {}'.format(e))
        except requests.exceptions.HTTPError as e:
            raise Exception('There was an HTTP error that occurred while establishing the connection to Nessie. Stacktrace: {}'.format(e))
        except requests.exceptions.RequestException as e:
            raise Exception('There was an ambiguous exception that occurred. You\'re on your own. Stacktrace: {}'.format(e))


        response_body = {
            'status_code': response.status_code,
            'response': response.reason,
            'requests_response': response,
            'content': response.json()
        }
        return response_body

if __name__ == '__main__':
    api_key = '0d243c701f2b9721efb82640b83e13eb'
    test_string = 'enterprise/customers/56c66be6a73e4927415074ca'
    method = 'GET'
    client_type = 'enterprise'
    client = NessieClient(api_key, client_type)
    resp = client.api_call(test_string, method)
    print(resp)
