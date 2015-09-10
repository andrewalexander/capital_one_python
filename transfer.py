import requests
import json

class Transfer():

	baseUrl = "http://api.nessiebanking.com:80"
	accBaseUrl = baseUrl + "/accounts"
	transBaseUrl = baseUrl + "/transfers"
	apiKey = '330681dbf73436832cafac4f11622452'

	#GET

	def getAllByAccountId(self, accId):
		url = '%s/%s/transfers?key=%s' % (self.accBaseUrl, accId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	# returns json data as a list type
		return data

	def getAllByType(self, accId, transType):
		url = '%s/%s/transfers?type=%s&key=%s' % (self.accBaseUrl, accId, transType, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	# returns json data as a list type
		return data

	def getOne(self, transId):
		url = '%s/%s?key=%s' % (self.transBaseUrl, transId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	# returns json data as a list type
		return data

	# POST 

	def createTransfer(self, accId, transfer):
		url = '%s/%s/transfers?key=%s' % (self.accBaseUrl, accId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.post(url, params=params, data=json.dumps(transfer), headers=headers)
		return response

	# PUT

	def updateTransfer(self, transId, transfer):
		url = '%s/%s?key=%s' % (self.transBaseUrl, transId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(transfer), headers=headers)
		return response.content


	# DELETE

	def deleteTransfer(self, transId):
		url = '%s/%s?key=%s' % (self.transBaseUrl, transId, self.apiKey)
		response = requests.delete(url)
		return response.content
