# Ethan Martin
# Final Project

# Import modules
import pandas as pd
from bs4 import BeautifulSoup
import requests

URL = 'https://www.spotrac.com/nfl/positional/breakdown/2019/'
source = requests.get(URL)
soup = BeautifulSoup(source.content, 'html.parser')

columns = ['Team', 'Total_Players', 'QB$', 'RB/FB$', 'WR$', 'TE$', 'OL$', 'DL$', 'LB$', 'DB$', 'K/P/LS$', 'Total$_Spent']
df = pd.DataFrame(columns=columns)

table = soup.find('table', attrs= {'class':'responsive datatable cap'}).tbody
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '')for td in tds]
    df = df.append(pd.Series(row, index=columns), ignore_index=True)

df.to_csv('PositionalData2019.csv', index=False)

