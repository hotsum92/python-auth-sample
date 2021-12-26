from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import CookieJar
import json

opener = build_opener(HTTPCookieProcessor(CookieJar()))

opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'),
    ('Content-Type', 'application/json')
]


auth_url = 'http://localhost:8000/api/authentication'

auth_data = {
    'data': {
        'attributes': {
            'email': 'sample@email.com',
            'password': 'p@ssw0rd'
        }
    }
}

res = opener.open(auth_url, json.dumps(auth_data).encode())

res.close()

get_url = 'http://localhost:8000/api/data'

res = opener.open(get_url)

print(json.dumps(res.read().decode('utf8')))

res.close()
