import json
import requests
import config


class Branch():
    def __init__(self):
        self.base_url = config.base_url
        self.url_with_entity = self.base_url + '/branches'
        self.api_key = config.api_key

    def get_all(self):
        """
        Get all branches

        Returns:
            dict of status code (200) and list of branches
        """
        url = '%s?key=%s' % (self.url_with_entity, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'branches': response.json()
        }

    def get_one(self, branch_id):
        """
        Get one branch

        Args:
            branch_id: ID of the branch to get description for
        Returns:
            dict of status code (200) and branch description
        """
        url = '%s/%s?key=%s' % (self.url_with_entity, branch_id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'branch': response.json()
        }
