import json
import requests

class Atm():

	baseUrl = 'http://api.reimaginebanking.com:80'
	urlWithEntity = baseUrl + '/atms'
	apiKey = 'ff1fbfb0f1bfaefb769e25299805ddf1'				# test API key

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