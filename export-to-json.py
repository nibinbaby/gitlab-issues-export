import urllib.parse
import requests
import json

per_page = 100
page = 1
data = []

headers = {'PRIVATE-TOKEN': '<access-token>'} # replace with your gitlab access token
api = 'https://<yourserver>.foundingminds.com/api/v4/projects/<projectid>/issues?scope=all&' # replace the url with your base url of gitlab and projectid

url = api + urllib.parse.urlencode({'page': page, 'per_page': per_page})
res_headers = requests.get(url, headers=headers).headers
json_data = requests.get(url, headers=headers).json()

page = 0
while page <= int(res_headers['X-Total-Pages']):
  page+=1
  print(page)
  print(res_headers['X-Total-Pages'])
  for j in json_data:
    data.append(j)
  url = api + urllib.parse.urlencode({'page': page, 'per_page': per_page})
  json_data = requests.get(url, headers=headers).json()


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'a') as fp:
        json.dump(data, fp)

writeToJSONFile('./','file-name',data)
