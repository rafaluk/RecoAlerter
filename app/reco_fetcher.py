import requests
from bs4 import BeautifulSoup


class RecoFetcher:
    def __init__(self, source='mdm'):
        self._source = source
        self._reco_list = []

    def get_www(self):
        if self._source == 'mdm':
            address = 'https://www.mdm.pl/ui-pub/site/analizy_i_rynek/analizy_i_rekomendacje/komentarze_analitykow'
        else:
            address = ''
        raw_site = requests.get(address).text.encode("utf-8")
        parsed_site = BeautifulSoup(raw_site, features="html.parser")
        return parsed_site

    def get_reco_list(self, parsed_site):
        reco_table = parsed_site.find_all('table', {'class': 'table content-komunikat-specjalny action-table'})[0]
        reco_rows = list(reco_table.find_all('tr'))
        iterrows = iter(reco_rows)
        next(iterrows)
        for row in iterrows:
            tds = list(row.find_all('td'))
            concat = str('[' + tds[1].get_text() + '] ' + tds[0].get_text() + ' (' + tds[2].get_text() + ')')
            if concat not in self._reco_list:
                self._reco_list.append(concat)
        return self._reco_list

