import requests

class APIClient:

    def __init__(self, url, api_key, header) -> None:
        self.url = url
        self.api_key = api_key
        self.header = header

    def get_data(self):

        url = f"{self.url}"
        headers = f"{self.header}: {self.api_key}"
        response = requests.get(url, headers=headers) 

        if response.status_code == 200:
            print(response.json)
        else:
            response.raise_for_status()

