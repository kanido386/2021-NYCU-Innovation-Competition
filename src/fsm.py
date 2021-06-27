from flask.scaffold import F
from transitions.extensions import GraphMachine

from service.basic import send_text_message
from service.other import send_youtube_video
from service.blockchain import users, service_tokens

class TocMachine(GraphMachine):
  def __init__(self, **machine_configs):
    self.machine = GraphMachine(model=self, **machine_configs)


  def is_going_to_state1(self, event):
    text = event.message.text
    return text.lower() == "go to state1"


  def is_going_to_state2(self, event):
    text = event.message.text
    return text.lower() == "go to state2"


  def is_going_to_youtube(self, event):
    text = event.message.text
    return "聽" in text


  def is_going_to_try_blockchain(self, event):
    text = event.message.text
    return "give me" in text


  def on_enter_state1(self, event):
    print("I'm entering state1")

    reply_token = event.reply_token
    send_text_message(reply_token, "Trigger state1")
    self.go_back()


  # def on_exit_state1(self):
  #   print("Leaving state1")


  def on_enter_state2(self, event):
    print("I'm entering state2")

    reply_token = event.reply_token
    send_text_message(reply_token, "Trigger state2")
    self.go_back()


  # def on_exit_state2(self):
  #   print("Leaving state2")


  def on_enter_youtube(self, event):
    print("I'm entering youtube")

    id = event.source.user_id
    reply_token = event.reply_token
    query = event.message.text
    send_youtube_video(id, reply_token, query)
    self.go_back()


  def on_enter_try_blockchain(self, event):
    print("I'm entering state2")

    user_id = event.source.user_id
    reply_token = event.reply_token
    amount = int(event.message.text[7:])
    user_wallet_address = users.retrieve.wallet_address(user_id)
    service_tokens.mint(user_wallet_address, amount)
    send_text_message(reply_token, f"恭喜獲得 {amount} 枚健康幣！")
    self.go_back()