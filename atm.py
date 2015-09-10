import json
import requests

class Atm():

	urlWithEntity = 'http://api.nessiebanking.com:80/atms'
	baseUrl = 'http://api.nessiebanking.com:80'
	apiKey = '330681dbf73436832cafac4f11622452'				# test API key

	# GET
	
	def getAll(self):
		url = '%s?key=%s' % (self.urlWithEntity, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	
		return data

	def getAllByLocation(self, lat, lng, rad):
		url = ('%s?lat=%s&lng=%s&rad=%s&key=%s') % (self.urlWithEntity, lat, lng, rad, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))	
		return data

	def getOne(self, id):
		url = '%s/%s?key=%s' % (self.urlWithEntity, id, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

# Test Data
# atm = Atm()
# print atm.getAll()
# print atm.getAllByLocation(38.882163, -77.1113105, 1)
# print atm.getOne('555bed94a520e036e52b1d7b')