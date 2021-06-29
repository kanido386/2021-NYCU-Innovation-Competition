from transitions.extensions import GraphMachine
import datetime

from service.basic import send_text_message, push_text_message
from service.other import send_youtube_video
from service.blockchain import users, service_tokens
from service.firebase import save_to_db, load_from_db, write_message, read_message, upload_image, send_image
from service.hardcode import send_menu

class TocMachine(GraphMachine):
  def __init__(self, **machine_configs):
    self.machine = GraphMachine(model=self, **machine_configs)


  def is_going_to_menu(self, event):
    text = event.message.text
    return "哈囉" in text


  def is_going_to_mood(self, event):
    text = event.message.text
    return text.lower() == "share mood"

  
  def is_going_to_mood_detailed(self, event):
    return True
  
  
  # def is_going_to_state1(self, event):
  #   text = event.message.text
  #   return text.lower() == "go to state1"


  # def is_going_to_state2(self, event):
  #   text = event.message.text
  #   return text.lower() == "go to state2"


  # def is_going_to_youtube(self, event):
  #   text = event.message.text
  #   return "聽" in text


  # def is_going_to_try_blockchain(self, event):
  #   text = event.message.text
  #   return "Give me" in text

  # def is_going_to_write_message(self, event):
  #   text = event.message.text
  #   return "Message" in text and len(text) > 7

  # def is_going_to_read_message(self, event):
  #   text = event.message.text
  #   return text.lower() == "message"

  # def is_going_to_image(self, event):
  #   print(event)
  #   return event.message.type == "image"

  # def is_going_to_see_image(self, event):
  #   print(event)
  #   text = event.message.text
  #   return text.lower() == "see image"

  # ==================================================

  def on_enter_menu(self, event):
    print("I'm entering menu")

    user_id = event.source.user_id
    send_menu(user_id)
    self.go_back()


  def on_enter_mood(self, event):
    print("I'm entering mood")

    reply_token = event.reply_token
    send_text_message(reply_token, "1~10 你打幾分呢？")


  def on_enter_mood_detailed(self, event):
    print("I'm entering mood_detailed")

    user_id = event.source.user_id
    reply_token = event.reply_token
    text = event.message.text

    now = datetime.datetime.now()
    today = f'{now.year}-{now.month}-{now.day}'

    try:
      score = int(text)
    except:
      send_text_message(reply_token, "請輸入數字 1~10 哦～")
      self.go_back()

    if score >= 1 and score <= 5:
      # save_to_db(user_id, 'mood', )
      value = load_from_db(user_id, 'mood')
      print('==============================')
      print(value)
      print(type(value))
      print('==============================')
      send_text_message(reply_token, "怎麼了？")
    elif score >= 6 and score <= 10:
      send_text_message(reply_token, "是什麼讓您心情好？")
    else:
      send_text_message(reply_token, "請輸入數字 1~10 哦～")
      self.go_back()

  # def on_enter_state1(self, event):
  #   print("I'm entering state1")

  #   reply_token = event.reply_token
  #   send_text_message(reply_token, "Trigger state1")
  #   self.go_back()


  # # def on_exit_state1(self):
  # #   print("Leaving state1")


  # def on_enter_state2(self, event):
  #   print("I'm entering state2")

  #   reply_token = event.reply_token
  #   send_text_message(reply_token, "Trigger state2")
  #   self.go_back()


  # # def on_exit_state2(self):
  # #   print("Leaving state2")


  # def on_enter_youtube(self, event):
  #   print("I'm entering youtube")

  #   id = event.source.user_id
  #   reply_token = event.reply_token
  #   query = event.message.text
  #   send_youtube_video(id, reply_token, query)
  #   self.go_back()


  # def on_enter_try_blockchain(self, event):
  #   print("I'm entering try_blockchain")

  #   user_id = event.source.user_id
  #   reply_token = event.reply_token
  #   amount = int(event.message.text[7:])
  #   user_wallet_address = users.retrieve.wallet_address(user_id)
  #   service_tokens.mint(user_wallet_address, amount)
  #   send_text_message(reply_token, f"恭喜獲得 {amount} 枚健康幣！")
  #   self.go_back()


  # def on_enter_write_message(self, event):
  #   print("I'm entering write_message")

  #   user_id = event.source.user_id
  #   message = event.message.text[8:]
  #   write_message(user_id, message)
  #   reply_token = event.reply_token
  #   send_text_message(reply_token, "訊息存起來囉！")
  #   self.go_back()


  # def on_enter_read_message(self, event):
  #   print("I'm entering read_message")

  #   user_id = event.source.user_id
  #   message = read_message(user_id)
  #   reply_token = event.reply_token
  #   send_text_message(reply_token, f"這是剛剛存起來的訊息：\n\n{message}")
  #   self.go_back()


  # def on_enter_image(self, event):
  #   print("I'm entering image")

  #   user_id = event.source.user_id
  #   message_id = event.message.id
  #   file_name = str(event.timestamp) + ".jpg"
  #   upload_image(user_id, message_id, file_name)

  #   reply_token = event.reply_token
  #   send_text_message(reply_token, "照片已上傳。")
  #   self.go_back()


  # def on_enter_see_image(self, event):
  #   print("I'm entering see_image")

  #   user_id = event.source.user_id
  #   reply_token = event.reply_token
  #   send_image(user_id, reply_token)
    
  #   self.go_back()
