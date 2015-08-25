import json
import requests

class Transaction():

	baseUrl = 'http://api.reimaginebanking.com:80'
	urlWithEntity = baseUrl + '/accounts'
	apiKey = '3eab5d0a550c080eab8b72ccbcbde8f8'				# test API key

	# GET
	def getAllByAccountId(self, accId):
		url = '%s/%s/transactions?key=%s' % (self.urlWithEntity, accId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getAllByAccountIdPayee(self, accId):
		url = '%s/%s/transactions?type=payee&key=%s' % (self.urlWithEntity, accId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getOneByAccountIdTransactionId(self, accId, transId):
		url = '%s/%s/transactions/%s?key=%s' % (self.urlWithEntity, accId, transId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	# PUT
		# Transaction format
			# {
			# 'medium': "balance or rewards",
			# 'payee_id': "",
			# 'amount': 0,
			# 'description': ""
			# }

	def updateTransaction(self, accId, transId, trans):
		url = '%s/%s/transactions/%s?key=%s' % (self.urlWithEntity, accId, transId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(trans), headers=headers)
		return response


	# POST
		# Transaction format
			# {
			# 'medium': "balance or rewards",
			# 'payee_id': "",
			# 'amount': 0,
			# 'transaction_date': "",
			# 'status': "",
			# 'description': ""
			# }

	def createTransaction(self, toAcc, trans):
		url = '%s/%s/transactions?key=%s' % (self.urlWithEntity, toAcc, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.post(url, params=params, data=json.dumps(trans), headers=headers)
		return response

	# DELETE
	def deleteTransaction(self, accId, transId):
		url = '%s/%s/transactions/%s?key=%s' % (self.urlWithEntity, accId, transId, self.apiKey)
		response = requests.delete(url)
		return response

# Test data
t = Transaction()
accId = '555bed95a520e036e52b262e'
accId2 = '55ca24432644c1aa1065163b'
transId = '555d681bc34e2890417b2744'
# print t.getAllByAccountId(accId)
# print t.getAllByAccountIdPayee(accId)
# print t.getOneByAccountIdTransactionId(accId, transId)
# print t.updateTransaction(accId, transId, payload)
# print t.createTransaction(accId, payload)
