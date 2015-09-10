import json
import requests

class Bill():

	baseUrl = 'http://api.nessiebanking.com:80'
	accBaseUrl = baseUrl + "/accounts"
	custBaseUrl = baseUrl + "/customers"
	apiKey = '3eab5d0a550c080eab8b72ccbcbde8'

	# GET
	def getAllByAccountId(self, accId):
		url = '%s/%s/bills?key=%s' % (self.accBaseUrl, accId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getOne(self, billId):
		url = '%s/bills/%s?key=%s' % (self.baseUrl, billId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getAllByCustomerId(self, custId):
		url = '%s/%s/bills?key=%s' % (self.custBaseUrl, custId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	
		return data

	# PUT
		# Bill format
			# {
			# 'status': ""
			# 'payee': ""
			# 'nickname': "",
			# 'payment_date': ""
			# 'recurring_date': 15
			# 'payment_amount': 100
			# }

	def updateBill(self, billId, bill):
		url = '%s/bills/%s?key=%s' % (self.accBaseUrl, billId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(bill), headers=headers)
		return response.content

	# POST
		# Bill format is identical to PUT

	def createBill(self, accId, bill):
		url = '%s/%s/bills?key=%s' % (self.accBaseUrl, accId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.post(url, params=params, data=json.dumps(bill), headers=headers)
		return response.content

	# DELETE
	
	def deleteBill(self, accId, billid):
		url = '%s/%s/bills/%s?key=%s'
		response = requests.delete(url)
		return response.content

b = Bill()
accId = '555bed95a520e036e52b262e'
billId = '555d6da5f5bfc41b4443ef9a'
custId = '555bed95a520e036e52b23c1'
bill = {
	'status': 'pending',
	'payee': 'Comcast',
	'nickname': 'monthly payment',
	'payment_date': '2015-08-22',
	'recurring_date': 20,
	'payment_amount': 60
}
# print b.getAllByCustomerId(custId)						# 401 unauthorized
# print b.getOneByAccountIdBillId(accId, billId)			# 401 unauthorized
# print b.updateBill(accId, billId, bill)					# 401 unauthorized			
# print b.createBill(accId, bill)							# 401 unauthorized