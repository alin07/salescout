import requests
import logging
import http.client
import json
# from bs4 import BeautifulSoup

http.client.HTTPConnection.debuglevel = 1
file_name = './uniqlo.json'
def save_data():
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    url = 'https://www.uniqlo.com/us/api/commerce/v5/en/products?path=22210,,,&flagCodes=discount&offset=0&limit=36&httpFailure=true'

    headers = {
        'User-Agent': 'Mozilla/5.0',
    }

    response = requests.get(url, headers=headers)
    # json_resp = response.json()
    with open(file_name, 'a') as out:
        out.write(str(response))


def retrieve_data():
    file = open(file_name)
    x = file.read()
    y = json.loads(x)
    print(type(y))
    print(type(x))
    file.close()

retrieve_data()