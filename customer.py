import json
import requests

class Customer():

	baseUrl = 'http://api.reimaginebanking.com:80'
	urlWithEntity = baseUrl + '/customers'
	urlWithAccEntity = baseUrl + '/accounts'
	apiKey = 'ff1fbfb0f1bfaefb769e25299805ddf1'				# test API key

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

		# Customer format
			# {
			# 'address': {
			# 'street_number': "",
			# 'street_name': "",
			# 'city': "",
			# 'state': "",
			# 'zip': ""
			# }
			# }

	def updateCustomer(self, custId, customer): 
		url = '%s/%s?key=%s' % (self.urlWithEntity, custId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(customer), headers=headers)
		return response

	# POST
		# Customer format
		# {
		# 'first_name': "",
		# 'last_name': "",
		# 'address': {
			# 'street_number': "",
			# 'street_name': "",
			# 'city': "",
			# 'state': "",
			# 'zip': ""
		# }
		# }

	def createCustomer(self, customer):
		url = '%s?key=%s' % (self.urlWithEntity, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.post(url, params=params, data=json.dumps(customer), headers=headers)
		return response

c = Customer()
custId = '555bed95a520e036e52b23c1'
accId = '555bed95a520e036e52b262e'
payload = {
	'address': {
	'street_number': '123',
	'street_name': 'Birchtree Court',
	'city': 'State College',
	'state': 'PA',
	'zip': '16801'
	}
}
createPayload = {
	'first_name': 'Cy',
	'last_name': 'Young',
	'address': {
	'street_number': '111',
	'street_name': 'Baseball Ave',
	'city': 'NYC',
	'state': 'NY',
	'zip': '12345'
	}
}
# print c.getAll()
# print c.getOne(custId)
# print c.getOneByAccountId(accId)
# print c.updateCustomer(custId, payload)			# 401 unauthorized
# print c.createCustomer(createPayload)				# 401 unauthorized


