import os

import requests
import random
import string
import time

from .utils.signature_generator import SignatureGenerator
get_signature = SignatureGenerator.generate


def GET_v1_users_userId(userId):
    server_url = os.environ['SERVER_URL']
    service_api_key = os.environ['SERVICE_API_KEY']
    service_api_secret = os.environ['SERVICE_API_SECRET']

    nonce = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
    timestamp = int(round(time.time() * 1000))


    path = f'/v1/users/{userId}'

    headers = {
        'service-api-key': service_api_key,
        'nonce': nonce,
        'timestamp': str(timestamp)
    }


    signature = get_signature('GET', path, nonce, timestamp, service_api_secret)
    headers['signature'] = signature

    res = requests.get(server_url + path, headers=headers)
    return res.json()
