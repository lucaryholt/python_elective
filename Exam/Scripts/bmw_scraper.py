import requests as req

URL = 'https://www.dba.dk/biler/biler/maerke-bmw/'
page = req.get(URL)

print(page.content)
