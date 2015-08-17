# Data type conversion example using json library

import json 

a = Account()				# creates a new instance of an account
aa = a.getAll()				# returns unicode representation of all accounts
s = str(aa)					# returns a string representation of all accounts
l = json.loads(s)			# returns a list of all accounts
firstId = str(l[0]["_id"])	# returns string of id in list item 0



# Test apiKey: 3eab5d0a550c080eab8b72ccbcbde8f8

# Test accId: 555bed95a520e036e52b24ca
# Account types: Checking, Savings, Credit Card

# CustomerId with multiple accounts: 555bed95a520e036e52b2170


# UPDATE METHOD NOT WORKING
import json
import requests

class Account():
	urlWithEntity = 'http://api.reimaginebanking.com:80/accounts'
	baseUrl = 'http://api.reimaginebanking.com:80'
	apiKey = '3eab5d0a550c080eab8b72ccbcbde8f8'

def getAll(self):
		url = '%s?&key=%s' % (self.urlWithEntity, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	# returns json data as a list type
		return data
		
def updateAccount(self, accId, acc):
		accountToUpdate = acc
		url = '%s/%s?key=%s' % (self.urlWithEntity, accId, self.apiKey)
		payload = {'accountId': accId, 'acc': acc}
		r = requests.put(url, data=payload)
		return r.content