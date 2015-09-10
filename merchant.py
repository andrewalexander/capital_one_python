import json
import requests

class Merchant():

	baseUrl = "http://api.nessiebanking.com:80"
	urlWithEntity = baseUrl + "/merchants"
	apiKey = '330681dbf73436832cafac4f11622452'				# test API key

	# GET
	
	def getAll(self):
		url = '%s?key=%s' % (self.urlWithEntity, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	# returns json data as a list type
		return data

	def getAllByLocation(self, lat, lng, rad):
		url = '%s?lat=%s&lng=%s&rad=%s&key=%s' % (self.urlWithEntity, lat, lng, rad, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getOne(self, merchId):
		url = '%s/%s?key=%s' % (self.urlWithEntity, merchId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	# POST

	def createMerchant(self, merchant):
		url = '%s?key=%s' % (self.urlWithEntity, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.post(url, params=params, data=json.dumps(account), headers=headers)
		return response

	# PUT
	
	def updateMerchant(self, merchId, merchant):
		url = '%s/%s?key=%s' % (self.urlWithEntity, merchId, self.apiKey)
		headers = {'content-type': 'application/json'}
		params = {'key': self.apiKey}
		response = requests.put(url, params=params, data=json.dumps(account), headers=headers)
		return response.content
