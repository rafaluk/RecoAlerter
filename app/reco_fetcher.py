import requests
from bs4 import BeautifulSoup


class RecoFetcher:
    def __init__(self, source='mdm'):
        self._source = source
        self._reco_list = None

    def get_www(self):
        if self._source == 'mdm':
            address = 'https://www.mdm.pl/ui-pub/site/analizy_i_rynek/analizy_i_rekomendacje/komentarze_analitykow'
        raw_site = requests.get(address).text.encode("utf-8")
        parsed_site = BeautifulSoup(raw_site, features="html.parser")
        return parsed_site

    def get_values(self, parsed_site):
        recos = parsed_site.find_all('td', {'class': 'name-cell'})
        self._reco_list = [reco.get_text() for reco in recos]

        return self._reco_list

