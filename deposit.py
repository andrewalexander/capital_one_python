import json
import requests

class Deposit():

	baseUrl = 'http://api.reimaginebanking.com:80'
	urlWithEntity = baseUrl + '/accounts'
	apiKey = '3eab5d0a550c080eab8b72ccbcbde8f8'				# test API key

	# GET
	
	def getAllByAccountId(self, accId):
		url = '%s/%s/deposits?key=%s' % (self.urlWithEntity, accId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getOneByAccountIdDepositId(self, accId, depositId):
		url = '%s/%s/deposits/%s?key=%s' % (self.urlWithEntity, accId, depositId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	# PUT
		# Deposit format
		# {
		# 'medium': "balance or rewards",
		# 'amount': 0,
		# 'description': ""
		# }

	def updateDeposit(self, accId, depositId, deposit):
		url = '%s/%s/deposits/%s?key=%s' % (self.urlWithEntity, accId, depositId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(deposit), headers=headers)
		return response

	# POST
		# Deposit format
			# {
			# 'medium': "balance or rewards",
			# 'transaction_date': "",
			# 'status': "",
			# 'amount': 0,
			# 'description': ""
			# }

	def createDeposit(self, toAcc, deposit):
		url = '%s/%s/deposits?key=%s' % (self.urlWithEntity, toAcc, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.post(url, params=params, data=json.dumps(deposit), headers=headers)
		return response

	# DELETE
	def deleteDeposit(self, accId, depositId):
		url = '%s/%s/deposits/%s?key=%s' % (self.urlWithEntity, accId, depositId, self.apiKey)
		response = requests.delete(url)
		return response

# Test Data
# d = Deposit()
# accId = '555bed95a520e036e52b262e'
# depositId = '55c8fb422644c1aa10651625'
# print d.getAllByAccountId('accId')
# print d.getOneByAccountIdDepositId('accId', 'depositId')
