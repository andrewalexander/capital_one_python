import requests
import config


class Atm:
    """
    ATM class - get ATM locations
    """

    def __init__(self):
        self.base_url = config.base_url
        self.url_with_entity = self.base_url + '/atms'
        self.api_key = config.api_key

    def _paginate_results(self, response):
        """
        Helper function for dealing with pages of results

        Args:
            response: the response body from a request that is paginated
        Returns:
            concatenated list of all pages' data
        """
        data = response['data']

        while response['data']:
            # get the next URL
            paging_url = response['paging']['next']
            url = '%s%s' % (self.base_url, paging_url)

            # get the next page
            response = requests.get(url).json()

            # add to our big list
            for val in response['data']:
                data.append(val)

        return data

    def get_all(self):
        """
        Get all ATM information

        NOTE:
            This endpoint deals with many paged results and can result
            in 60+ individual API calls to Nessie.

        Returns:
            dict with status code (200) and list of ATMs
        """
        url = '%s?key=%s' % (self.url_with_entity, self.api_key)
        response = requests.get(url)

        full_atm_list = self._paginate_results(response.json())

        return {
            'code': response.status_code,
            'atms': full_atm_list
        }

    def get_all_by_location(self, lat, lng, rad):
        """
        Get all ATMs within a certain radius for a given latitude/longitude

        Args:
            lat: Latitude of location
            lng: Longitude of location
            rad: Radius (in miles) around (lat, lng) to fetch results for
        Returns:
            dict with status code (200) and list of ATMs around given location
        """
        url = ('%s?lat=%s&lng=%s&rad=%s&key=%s') % (self.url_with_entity, lat, lng, rad, self.api_key)
        response = requests.get(url)

        full_atm_list = self._paginate_results(response.json())

        return {
            'code': response.status_code,
            'atms': full_atm_list
        }

    def get_one(self, id):
        """
        Get a single ATM description

        Args:
            id: ATM ID to get description for
        Returns:
            dict with status code (200) and single ATM description
        """
        url = '%s/%s?key=%s' % (self.url_with_entity, id, self.api_key)
        response = requests.get(url)

        return {
            'code': response.status_code,
            'atm': response.json()
        }

if __name__ == '__main__':
    atm = Atm()
    atm.get_all()
