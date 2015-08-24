import json
import requests

class Atm():

	urlWithEntity = 'http://api.reimaginebanking.com:80/atms'
	baseUrl = 'http://api.reimaginebanking.com:80'
	apiKey = '3eab5d0a550c080eab8b72ccbcbde8f8'				# test API key

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