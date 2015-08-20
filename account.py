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
	def updateAccount(self, accId, data):
		url = '%s/%s' % (self.urlWithEntity, accId)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		r = requests.put(url, params=params, data=json.dumps(data), headers=headers)
		print r.content
		return r.content
