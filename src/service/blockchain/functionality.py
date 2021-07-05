from . import users
from ..basic import push_text_message


def init_blockchain(user_id):
  address = users.retrieve.wallet_address(user_id)
  if address == None:
    amount = 30
    push_text_message(user_id, f'送您 {amount} 枚健康幣當作見面禮～\n快去 BITMAX Wallet 查收吧  \U0001f603')
    res = users.transfer.service_token(user_id, amount)
    print(res)