import json
import requests

class Account():

	baseUrl = 'http://api.nessiebanking.com:80'
	urlWithEntity = baseUrl + '/accounts'
	apiKey = '330681dbf73436832cafac4f11622452'				# test API key

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
		# Account format
		# {
		# 'nickname': ""
		# }

	def updateAccount(self, accId, account):
		url = '%s/%s' % (self.urlWithEntity, accId)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(account), headers=headers)
		return response.content

	# POST
		# Account format
		# { 
		# 'type': "",
		# 'nickname': "",
		# 'rewards': 0,
		# 'balance': 0
		# }

	def createAccount(self, custId, account):
		url = '%s/customers/%s/accounts?key=%s' % (self.baseUrl, custId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.post(url, params=params, data=json.dumps(account), headers=headers)
		return response

	# DELETE
	
	def deleteAccount(self, accId):
		url = '%s/%s?key=%s' % (self.urlWithEntity, accId, self.apiKey)
		response = requests.delete(url)
		return response.content

a = Account()
accId = '555bed95a520e036e52b262e'
custId = '555bed95a520e036e52b23c1'
account = {'nickname': 'Brand New Update'}
accountToCreate = {
	'type': 'Checking',
	'nickname': 'Brand New Test Account',
	'rewards': 0,
	'balance': 300
}
# print a.getAll()
# print a.getOne(accId)
# print a.getAllByCustomerId(custId)
# print a.updateAccount(accId, account)
# print a.createAccount(custId, accountToCreate)		# 401 unauthorized