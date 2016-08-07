# Nessie Python SDK

This package allows a developer to easily interact with the Capital
One Hackathon API, named Nessie.

Docs:
http://andrewalexander.github.io/capital_one_python/

## Getting Started

### Install nessie with [pip](https://pip.pypa.io/en/stable/installing/)

** this package is not yet published, so at the time of writing, the `pip install` will not work. **
```
	pip install nessie 					# you may need to `sudo pip install nessie` depending on your env 
```

## Usage:
Using this SDK is as simple as passing any API endpoint listed on [Nessie documentation](http://api.reimaginebanking.com/documentation) to the `NessieClient.api_call()` method, as well as what kind of method it is is (`GET`, `POST`, `PUT`, or `DELETE`) 

```
import nessie

client = nessie.handler.NessieClient('my_api_key_here', 'customer' | 'enterprise')
# Get all accounts
accounts = client.api_call('accounts', 'GET')

# Get all accounts from a specific account ID
account_id = '56c66be7a73e492741508106'
account_from_id = client.api_call('accounts/{}'.format(account_id), 'GET')
>>> account_from_id
{'content': {u'rewards': 20674, u'customer_id': u'56c66be6a73e4927415074cb', u'type': u'Credit Card', u'_id': u'56c66be7a73e492741508106', u'balance': 38659, u'nickname': u"Harvie's Account"}, 'status_code': 200, 'response': 'OK', 'requests_response': <Response [200]>}

# if you don't like the .format() syntax, you can also just do
account_from_id = client.api_call('accounts/56c66be7a73e492741508106', 'GET')
>>> account_from_id
{'content': {u'rewards': 20674, u'customer_id': u'56c66be6a73e4927415074cb', u'type': u'Credit Card', u'_id': u'56c66be7a73e492741508106', u'balance': 38659, u'nickname': u"Harvie's Account"}, 'status_code': 200, 'response': 'OK', 'requests_response': <Response [200]>}

# POST data is handled as well. For example - to create an account
my_data = {
  'type': 'Credit Card',
  'nickname': 'My New Capital One Card!',
  'rewards': 42,
  'balance': 9001
}
customer_id = '56c66be6a73e4927415074ca'
create_account = client.api_call('customers/{}/accounts'.format(customer_id), 'POST', my_data)
create_account

```

The parser validates each component of the endpoint separately, and at the time of writing, all endpoints listed at the [Nessie documentation](http://api.reimaginebanking.com/documentation) were fully functional. 

Response structure is always of the form:
```
{
    'status_code': Integer of HTTP Status Code,
    'response': String of HTTP Status Reason/Response,
    'requests_response': Raw <Requests.Response> object from the requests library,
    'content': Dict containing the response from Nessie
}
```
