import requests
import json

class Purchase():

	baseUrl = "http://api.nessiebanking.com:80"
	urlWithEntity = baseUrl + "/purchases"
	apiKey = '330681dbf73436832cafac4f11622452'				# test API key


	# GET

	def getAllByAccountId(self, accId):
		url = '%s/accounts/%s/purchases?key=%s' % (self.baseUrl, accId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	# returns json data as a list type
		return data


	def getOne(self, purchId):
		url = '%s/%s?key=%s' % (self.urlWithEntity, purchId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	# returns json data as a list type
		return data


	# POST

	def createPurchase(self, accId, purchase):
		url = '%s/accounts/%s/purchases?key=%s' % (self.baseUrl, accId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.post(url, params=params, data=json.dumps(purchase), headers=headers)
		return response


	# PUT

	def updatePurcahse(self, purchId, purchase):
		url = '%s/%s?key=%s' % (self.urlWithEntity, purchId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(purchase), headers=headers)
		return response.content

	# DELETE
	def deletePurchase(self, purchId):
		url = '%s/%s?key=%s' % (self.urlWithEntity, purchId, self.apiKey)
		response = requests.delete(url)
		return response.content