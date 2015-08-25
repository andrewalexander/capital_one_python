import requests
import json

class Withdrawal():

	baseUrl = 'http://api.reimaginebanking.com:80'
	urlWithEntity = baseUrl + '/accounts'
	apiKey = '3eab5d0a550c080eab8b72ccbcbde8f8'				# test API key

	# GET

	def getAllByAccount(self, accId):
		url = '%s/%s/withdrawals?key=%s' % (self.urlWithEntity, accId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getOneByAccountIdWithdrawalId(self, accId, withdrawalId):
		url = '%s/%s/withdrawals/%s?key=%s' % (self.urlWithEntity, accId, withdrawalId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	# PUT
		# Withdrawal format
			# {
			# 'medium': "",
			# 'amount': 0,
			# 'description': ""
			# }

	def updateWithdrawal(self, accId, withdrawalId, withdrawal):
		url = '%s/%s/withdrawals/%s?key=%s' % (self.urlWithEntity, accId, withdrawalId, self.apiKey)
		headers = {
		'Authorization': 'Token token=<3eab5d0a550c080eab8b72ccbcbde8f8>',
		'content-type': 'application/json'
		}
		params = {'key': self.apiKey} 
		response = requests.put(url, params=params, data=json.dumps(withdrawal), headers=headers)
		return response


	# POST
		# Withdrawal format
			# {
			# 'medium': "",
			# 'amount': 0,
			# 'transaction_date': "",
			# 'status': "",
			# 'description': ""
			# }

	def createWithdrawal(self, toAcc, withdrawal):
		url = '%s/%s/withdrawals?key=%s' % (self.urlWithEntity, toAcc, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.post(url, params=params, data=json.dumps(withdrawal), headers=headers)
		return response

	# DELETE

	def deleteWithdrawal(self, accId, withdrawalId):
		url = '%s/%s/withdrawals/%s?key=%s' % (self.urlWithEntity, accId, withdrawalId, self.apiKey)
		response = requests.delete(url)
		return response.content

w = Withdrawal()
accId = '555bed95a520e036e52b262e'
withdrawalId = '555d6927c34e2890417b274d'
payload = {
	'medium': 'balance',
	'amount': 4,
	'description': 'successfully updated via updateWithdrawal'
}
createPayload = {
	'medium': 'balance',
	'amount': 40,
	'transaction_date': "2015-08-20",
	'status': 'pending',
	'description': 'hello, withdrawal'
}
# print w.getAllByAccount(accId)
# print w.getOneByAccountIdWithdrawalId(accId, withdrawalId)
print w.updateWithdrawal(accId, withdrawalId, payload)
# print w.createWithdrawal(accId, createPayload)
# print w.deleteWithdrawal(accId, '555d6a83c34e2890417b2750')
