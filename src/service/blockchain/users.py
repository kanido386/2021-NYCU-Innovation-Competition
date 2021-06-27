import os

import requests
import random
import string
import time

from .utils.signature_generator import SignatureGenerator
signatureGenerator = SignatureGenerator()
get_signature = signatureGenerator.generate





class retrieve:

    # # Retrieve user information
    # Retrieve the information of the given user.
    # https://docs-blockchain.line.biz/api-guide/category-users?id=v1-users-userid-get
    @staticmethod
    def wallet_address(user_id):
        server_url = os.environ['SERVER_URL']
        service_api_key = os.environ['SERVICE_API_KEY']
        service_api_secret = os.environ['SERVICE_API_SECRET']

        nonce = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
        timestamp = int(round(time.time() * 1000))


        path = f'/v1/users/{user_id}'

        headers = {
            'service-api-key': service_api_key,
            'nonce': nonce,
            'timestamp': str(timestamp)
        }


        signature = get_signature('GET', path, nonce, timestamp, service_api_secret)
        headers['signature'] = signature

        res = requests.get(server_url + path, headers=headers)
        wallet_address = res.json()['responseData']['walletAddress']
        return wallet_address