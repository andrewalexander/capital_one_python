import json
import requests


class Branch():
    base_url = 'http://api.reimaginebanking.com:80'
    url_with_entity = base_url + '/branches'
    api_key = '3eab5d0a550c080eab8b72ccbcbde8'

    # GET

    def get_all(self):
        url = '%s?key=%s' % (self.url_with_entity, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data

    def get_one(self, branch_id):
        url = '%s/%s?key=%s' % (self.url_with_entity, branch_id, self.api_key)
        response = requests.get(url)
        data = json.loads(str(json.dumps(response.text)))
        return data


br = Branch()
# branch_id = br.get_all()[0]["_id"]
# print br.get_all()		# 401 unauthorized
