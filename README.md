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
```
import nessie

client = nessie.handler.NessieClient('my_api_key_here', 'customer' | 'enterprise')
accounts = client.api_call('accounts')
account_from_id = client.api_call('accounts/abcd1234abcd1234')
```

Response structure is always of the form:
```
{
    'status_code': Integer of HTTP Status Code,
    'response': String of HTTP Status Reason/Response,
    'requests_response': Raw <Requests.Response> object from the requests library,
    'content': Dict containing the response from Nessie
}
```
