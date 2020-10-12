import requests as req
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Programmer&where=New-York'
page = req.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='Resultscontainer')

job_elems = soup.find_all('section', class_='card-content') #IKKE SECTION!!!!!!

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_="title")
    print(title_elem.text)
