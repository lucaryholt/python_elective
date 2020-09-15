import requests, os, subprocess, sys

argv = sys.argv

if len(argv) < 2:
    print('You must specify url to scrape.')
    sys.exit()

url = argv[1]
tempDir = 'data'

#Make dir and cd to dir
try:
    os.mkdir(tempDir)
except FileExistsError:
    print('Directory ' + tempDir + ' already exists.')
os.chdir(tempDir)

response = requests.get(url, allow_redirects=True)
open('data.html', 'wb').write(response.content)
