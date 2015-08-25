import json
import requests

class Customer():

	baseUrl = 'http://api.reimaginebanking.com:80'
	urlWithEntity = baseUrl + '/customers'
	urlWithAccEntity = baseUrl + '/accounts'
	apiKey = '3eab5d0a550c080eab8b72ccbcbde8f8'				# test API key

	# GET
	
	def getAll(self):
		url = '%s?key=%s' % (self.urlWithEntity, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getOne(self, custId):
		url = '%s/%s?key=%s' % (self.urlWithEntity, custId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getOneByAccountId(self, accId):
		url = '%s/%s/customer?key=%s' % (self.urlWithAccEntity, accId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	# PUT

		# Customer data format
			# {
			# 'address': {
			# 'street_number': "",
			# 'street_name': "",
			# 'city': "",
			# 'state': "",
			# 'zip': ""
			# }
			# }

	def updateCustomer(self, custId, data): 
		url = '%s/%s?key=%s' % (self.urlWithEntity, custId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(data), headers=headers)
		print response
		return response

c = Customer()
custId = '555bed95a520e036e52b23c1'
payload = {
	'address': {
	'street_number': '123',
	'street_name': 'Birchtree Court',
	'city': 'State College',
	'state': 'PA',
	'zip': '16801'
	}
}
c.updateCustomer(custId, payload)


