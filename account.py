import json
import requests

class Account():

	baseUrl = 'http://api.reimaginebanking.com:80'
	urlWithEntity = baseUrl + '/accounts'
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

	def updateAccount(self, accId, data):
		url = '%s/%s' % (self.urlWithEntity, accId)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(data), headers=headers)
		return response.content

	# POST

	def createAccount(self, custId, data):
		url = '%s/customers/%s/accounts?key=%s' % (self.baseUrl, custId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.post(url, params=params, data=json.dumps(data), headers=headers)
		print response.content
		return response.content

	# DELETE
	
	def deleteAccount(self, accId):
		url = '%s/%s?key=%s' % (self.urlWithEntity, accId, self.apiKey)
		response = requests.delete(url)
		return response.content

a = Account()
print a.getAll()
# print a.getOne('555bed95a520e036e52b262e')