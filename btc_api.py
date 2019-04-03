import base64
import random
import string
import time

import requests
from OpenSSL import crypto


def get_random_string(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Your API KEY
API_KEY = 'YOUR_API_KEY'
# Path of your private key
PRIVATE_KEY = 'PATH_TO_API_KEY'

pri_key_file = open(PRIVATE_KEY, "r")
pri_key = pri_key_file.read()
pri_key_file.close()

if pri_key.startswith('-----BEGIN '):
    pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, pri_key)
else:
    pkey = crypto.load_pkcs12(pri_key).get_privatekey()


def generate_jwt():
    headers = '{"typ":"JWT","alg":"RS256"}'
    jwt_header = base64.b64encode(str.encode(headers)).decode(
        'utf-8').replace('=', '').replace('/+', '_-').replace('+', '-').replace('\n', '')

    payload = '{"iat":%s,"exp":%s,"sub":"api_key_jwt","iss":"external","jti":"%s"}' % (
        int(time.time()), int(time.time()) + 30, get_random_string(size=12))
    jwt_payload = base64.b64encode(str.encode(payload)).decode(
        'utf-8').replace('=', '').replace('/+', '_-').replace('+', '-').replace('\n', '')

    _jwt_sign = '%s.%s' % (jwt_header, jwt_payload)
    _jwt_sign = crypto.sign(pkey, _jwt_sign, 'sha256')
    jwt_sign = base64.b64encode(_jwt_sign).decode(
        'utf-8').replace('=', '').replace('/+', '_-').replace('+', '-').replace('\n', '')

    return '%s.%s.%s' % (jwt_header, jwt_payload, jwt_sign)


def get_token():
    url = 'https://api.btc-exchange.com/pauth/web/sessions/generate_jwt'
    headers = {'x-api-key': API_KEY}
    data = {'kid': API_KEY, 'jwt_token': generate_jwt()}
    response = requests.post(url=url, headers=headers, data=data)
    return response.json().get('token')


def call_api():
    url = 'https://api.btc-exchange.com/papi/web/members/me'
    headers = {'x-api-key': API_KEY, 'Authorization': 'Bearer %s' % (get_token())}
    response = requests.get(url=url, headers=headers)
    return response


call_api()
