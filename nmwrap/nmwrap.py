import requests
from pycoingecko import CoinGeckoAPI

class NWaccount():
    """"""
    def __init__(self, api_key):
        session = requests.Session()
        self.session = session
        self.key=api_key
    def account(self):
        response = requests.get("https://api.nimiq.watch/account/" + self.key)
        info = response.json()
        return info