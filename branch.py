import json
import requests

class Branch():

	baseUrl = 'http://api.reimaginebanking.com:80'
	urlWithEntity = baseUrl + '/branches'
	apiKey = '3eab5d0a550c080eab8b72ccbcbde8'

	# GET
	
	def getAll(self):
		url = '%s?key=%s' % (self.urlWithEntity, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

	def getOne(self, branchId):
		url = '%s/%s?key=%s' % (self.urlWithEntity, branchId, self.apiKey)
		response = requests.get(url)
		data = json.loads(str(json.dumps(response.text)))
		return data

br = Branch()
print br.getAll()