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




class transfer:

    # # Transfer a delegated service token (user wallet)
    # Request to transfer the delegated service token in the given user wallet to another wallet.
    # https://docs-blockchain.line.biz/api-guide/category-users?id=v1-users-userid-service-tokens-contractid-transfer-post
    @staticmethod
    def service_token(user_id, amount):
        server_url = os.environ['SERVER_URL']
        service_api_key = os.environ['SERVICE_API_KEY']
        service_api_secret = os.environ['SERVICE_API_SECRET']
        # TODO:
        contract_id = os.environ['LBP_CONTRACT_ID_LBCC']
        owner_address = os.environ['LBP_OWNER_WALLET_ADDRESS']
        owner_secret = os.environ['LBP_OWNER_WALLET_SECRET']

        nonce = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
        timestamp = int(round(time.time() * 1000))


        path = f'/v1/users/{user_id}/service-tokens/{contract_id}/transfer'

        request_body = {
            'ownerAddress': f'{owner_address}',
            'ownerSecret': f'{owner_secret}',
            # TODO:
            'amount': f'{amount * 1000000}'
        }

        headers = {
            'service-api-key': service_api_key,
            'nonce': nonce,
            'timestamp': str(timestamp),
            'Content-Type': 'application/json'
        }


        signature = get_signature('POST', path, nonce, timestamp, service_api_secret, body=request_body)
        headers['signature'] = signature

        res = requests.post(server_url + path, headers=headers, json=request_body)
        return res.json()