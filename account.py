import json
import requests

class Account():

	urlWithEntity = 'http://api.reimaginebanking.com:80/accounts'
	baseUrl = 'http://api.reimaginebanking.com:80'
	apiKey = '3eab5d0a550c080eab8b72ccbcbde8f8'				# test API key

	# GET

	def getAll(self):
		url = '%s?&key=%s' % (self.urlWithEntity, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	# returns json data as a list type
		return data

	def getAllByType(self, accType):
		url = '%s?type=%s&key=%s' % (self.urlWithEntity, accType, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getOne(self, accId):
		url = '%s/%s?key=%s' % (self.urlWithEntity, accId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getAllByCustomerId(self, custId):
		url = '%s/customers/%s/accounts?key=%s' % (self.baseUrl, custId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	# PUT

	def updateAccount(self, accId, acc):
		url = '%s/%s?key=%s' % (self.urlWithEntity, accId, self.apiKey)
		payload = {'accountId': accId, 'acc': acc}
		r = requests.put(url, params=payload)
		print r.content
		
# Output to demonstrate updateAccount() issue
a = Account()
pl = {"rewards": 9}
print a.getOne('555bed95a520e036e52b25e7')
a.updateAccount('555bed95a520e036e52b25e7', pl)
print a.getOne('555bed95a520e036e52b25e7')