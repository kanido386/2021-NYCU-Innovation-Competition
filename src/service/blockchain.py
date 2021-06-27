import os

import requests
import random
import string
import time

from .utils.signature_generator import SignatureGenerator
signatureGenerator = SignatureGenerator()
get_signature = signatureGenerator.generate


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



def POST_v1_service_tokens_contractId_mint(user_wallet_address, amount):
    server_url = os.environ['SERVER_URL']
    service_api_key = os.environ['SERVICE_API_KEY']
    service_api_secret = os.environ['SERVICE_API_SECRET']
    # TODO:
    contract_id = os.environ['LBP_CONTRACT_ID_LBCC']
    owner_address = os.environ['LBP_OWNER_WALLET_ADDRESS']
    owner_secret = os.environ['LBP_OWNER_WALLET_SECRET']


    nonce = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
    timestamp = int(round(time.time() * 1000))


    path = f'/v1/service-tokens/{contract_id}/mint'

    request_body = {
        'ownerAddress': f'{owner_address}',
        'ownerSecret': f'{owner_secret}',
        'toAddress': f'{user_wallet_address}',
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