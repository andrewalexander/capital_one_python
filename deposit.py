import json
import requests

class Deposit():

	baseUrl = 'http://api.nessiebanking.com:80'
	urlWithEntity = baseUrl + '/accounts'
	apiKey = '330681dbf73436832cafac4f11622452'				# test API key

	# GET
	
	def getAllByAccountId(self, accId):
		url = '%s/%s/deposits?key=%s' % (self.urlWithEntity, accId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getOne(self, depositId):
		url = '%s/deposits/%s?key=%s' % (self.url, depositId, self.apiKey)
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

	def updateDeposit(self, depositId, deposit):
		url = '%s/deposits/%s?key=%s' % (self.urlWithEntity, depositId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(deposit), headers=headers)
		return response.content

	# POST
		# Deposit format
			# {
			# 'medium': "balance or rewards",
			# 'transaction_date': "",
			# 'status': "pending or cancelled or recurring",
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
d = Deposit()
accId = '555bed95a520e036e52b262e'
depositId = '55c8fb422644c1aa10651625'
updatePayload = {
	'medium': 'balance',
	'amount': "0",
	'description': 'successful update'
}
# print d.getAllByAccountId(accId)
# print d.getOneByAccountIdDepositId(accId, depositId)
print d.updateDeposit(accId, depositId, updatePayload)
