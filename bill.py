import json
import requests

class Bill():

	baseUrl = 'http://api.reimaginebanking.com:80'
	accBaseUrl = baseUrl + "/accounts"
	custBaseUrl = baseUrl + "/customers"
	apiKey = '3eab5d0a550c080eab8b72ccbcbde8'

	# GET

	def getAllByCustomerId(self, custId):
		url = '%s/%s/bills?key=%s' % (self.custBaseUrl, custId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	
		return data

	def getOneByCustomerIdBillId(self, custId, billId):
		url = '%s/%s/bills/%s?key=%s' % (self.custBaseUrl, custId, billId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getOneByAccountIdBillId(self, accId, billId):
		url = '%s/%s/bills/%s?key=%s' % (self.accBaseUrl, accId, billId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	# PUT
		# Bill data format
			# {
			# 'status': "pending"
			# 'payee': "Comcast"
			# 'payment_date': "2015-04-20"
			# 'recurring_date': 15
			# 'payment_amount': 100
			# }

	def updateBill(self, accId, billId, data):
		url = '%s/%s/bills/%s?key=%s' % (self.accBaseUrl, accId, billId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(data), headers=headers)
		return response.content

	# POST

	def createBill(self, accId, bill):
		url = '%s/%s/bills?key=%s' % (self.accBaseUrl, accId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.post(url, params=params, data=json.dumps(data), headers=headeres)
		return response.content

	# DELETE
	
	def deleteBill(self, accId, billid):
		url = '%s/%s/bills/%s?key=%s'
		response = requests.delete(url)
		return response.content

b = Bill()
accId = '555bed95a520e036e52b262e'
billId = '555d6da5f5bfc41b4443ef9a'
print b.getOneByAccountIdBillId(accId, billId)