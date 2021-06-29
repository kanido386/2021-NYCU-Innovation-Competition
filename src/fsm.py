from transitions.extensions import GraphMachine
import datetime
import time
import random

from service.basic import send_text_message, push_text_message
from service.other import send_youtube_video
from service.blockchain import users, service_tokens
from service.firebase import write_message, read_message, upload_skin_image, send_image
from service.hardcode import send_menu, send_entertainment_menu

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

  def is_going_to_mood_done(self, event):
    return True


  def is_going_to_meal(self, event):
    text = event.message.text
    return text.lower() == "record meal"

  def is_going_to_meal_search(self, event):
    return True

  def is_going_to_meal_report(self, event):
    return True

  def is_going_to_meal_input(self, event):
    return True

  def is_going_to_meal_reward(self, event):
    return True


  def is_going_to_diary(self, event):
    text = event.message.text
    return text.lower() == "share diary"

  def is_going_to_diary_done(self, event):
    return True


  def is_going_to_exercise(self, event):
    text = event.message.text
    return text.lower() == "record exercise"

  def is_going_to_exercise_done(self, event):
    return True


  def is_going_to_sleeping(self, event):
    text = event.message.text
    return text.lower() == "record sleeping"

  def is_going_to_sleeping_up(self, event):
    return True

  def is_going_to_sleeping_done(self, event):
    return True

  
  def is_going_to_skin(self, event):
    text = event.message.text
    return text.lower() == "skin"

  def is_going_to_skin_process(self, event):
    return event.message.type == "image"

  def is_going_to_skin_done(self, event):
    return True


  def is_going_to_report(self, event):
    text = event.message.text
    return text.lower() == "report"


  def is_going_to_entertainment(self, event):
    text = event.message.text
    return text.lower() == "entertainment"

  def is_going_to_exit(self, event):
    text = event.message.text
    return "離開" in text


  def is_going_to_youtube(self, event):
    text = event.message.text
    return text.lower() == "youtube"

  def is_going_to_youtube_ing(self, event):
    text = event.message.text
    return "聽" in text

  def is_going_to_youtube_done(self, event):
    text = event.message.text
    return "離開" in text
  
  
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
    time.sleep(3)
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
      # TODO: would have bug
      self.go_back(event)

    # TODO: 存心情分數
    if score >= 1 and score <= 5:
      # save_to_db(user_id, 'mood', {today: score}, 'dict')
      # value = load_from_db(user_id, 'mood')
      # print('==============================')
      # print(value)
      # print(type(value))
      # print('==============================')
      send_text_message(reply_token, "怎麼了？")
    elif score >= 6 and score <= 10:
      send_text_message(reply_token, "是什麼讓您心情好？")
    else:
      send_text_message(reply_token, "請輸入數字 1~10 哦～")
      # TODO: would have bug
      self.go_back(event)


  def on_enter_mood_done(self, event):
    print("I'm entering mood_done")

    reply_token = event.reply_token
    # TODO: 存詳細＆獲得健康幣
    send_text_message(reply_token, "了解了！")
    self.go_back(event)



  def on_enter_meal(self, event):
    print("I'm entering meal")

    reply_token = event.reply_token
    send_text_message(reply_token, "請輸入食物名稱")


  def on_enter_meal_search(self, event):
    print("I'm entering meal_search")

    text = event.message.text
    # TODO: 從食物資料庫裡面找食物
    if text == 'yes':
      self.yes(event)
    else:
      self.no(event)

  def on_enter_meal_report(self, event):
    print("I'm entering meal_report")

    reply_token = event.reply_token
    # TODO: 存資料庫
    # TODO: 回報卡路里
    calories = 100
    send_text_message(reply_token, f'食物熱量 {calories} 大卡')
    self.go_back(event)


  def on_enter_meal_input(self, event):
    print("I'm entering meal_input")

    reply_token = event.reply_token
    send_text_message(reply_token, "請您輸入食物相關資訊")


  def on_enter_meal_reward(self, event):
    print("I'm entering meal_reward")

    reply_token = event.reply_token
    # TODO: 存資料庫
    # TODO: 獲得健康幣
    amount = 5
    send_text_message(reply_token, f'感謝您的回饋，送您 {amount} 枚健康幣～')
    self.go_back(event)



  def on_enter_diary(self, event):
    print("I'm entering diary")

    reply_token = event.reply_token
    send_text_message(reply_token, "和我分享吧！")

  
  def on_enter_diary_done(self, event):
    print("I'm entering diary_done")

    reply_token = event.reply_token
    # TODO: 產生文字雲
    # TODO: 存資料庫
    # TODO: 獲得健康幣（或許可以根據字數來決定數量）
    amount = 5
    send_text_message(reply_token, f'謝謝您的分享，送您 {amount} 枚健康幣～')
    self.go_back(event)



  def on_enter_exercise(self, event):
    print("I'm entering exercise")

    reply_token = event.reply_token
    send_text_message(reply_token, "告訴我您剛剛做了什麼運動吧！")

  
  def on_enter_exercise_done(self, event):
    print("I'm entering exercise_done")

    reply_token = event.reply_token
    # TODO: 存資料庫
    # TODO: 獲得健康幣
    amount = 5
    send_text_message(reply_token, f'運動身體好，送您 {amount} 枚健康幣～')
    self.go_back(event)



  def on_enter_sleeping(self, event):
    print("I'm entering sleeping")

    reply_token = event.reply_token
    send_text_message(reply_token, "昨晚幾點睡呢？")


  def on_enter_sleeping_up(self, event):
    print("I'm entering sleeping_up")

    reply_token = event.reply_token
    # TODO: 存資料庫
    send_text_message(reply_token, "今天幾點幾床？")

  
  def on_enter_sleeping_done(self, event):
    print("I'm entering sleeping_done")

    reply_token = event.reply_token
    # TODO: 存資料庫
    hour = 7
    minute = 30
    send_text_message(reply_token, f'您一共睡了 {hour} 小時 {minute} 分鐘。\n記得，睡眠也很重要哦！')
    self.go_back(event)



  def on_enter_skin(self, event):
    print("I'm entering skin")

    reply_token = event.reply_token
    send_text_message(reply_token, "上傳圖片給我看看吧！")


  def on_enter_skin_process(self, event):
    print("I'm entering skin_process")

    user_id = event.source.user_id
    message_id = event.message.id
    file_name = str(event.timestamp) + ".jpg"
    upload_skin_image(user_id, message_id, file_name)

    reply_token = event.reply_token
    push_text_message(user_id, "照片處理中，請稍候⋯⋯")
    # TODO: 處理照片
    time.sleep(5)
    self.advance(event)

  
  def on_enter_skin_done(self, event):
    print("I'm entering skin_done")

    reply_token = event.reply_token
    # TODO: 回報預測結果
    chance = [30, 60, 80]
    accuracy = random.choice(chance)
    result = '紅疹'
    if accuracy < 60:
      send_text_message(reply_token, f'照片可能不夠清楚，請再重拍一張！')
    else:
      send_text_message(reply_token, f'我們有 {accuracy}% 的信心，這可能是【{result}】')
    # TODO: 存資料庫
    self.go_back(event)



  def on_enter_report(self, event):
    print("I'm entering report")

    reply_token = event.reply_token
    # TODO: 健康狀況回報
    send_text_message(reply_token, "2021.06.29 Tue.\n\n【報告內容】\n\n祝您天天健康！")
    self.go_back(event)



  def on_enter_entertainment(self, event):
    print("I'm entering entertainment")

    user_id = event.source.user_id
    time.sleep(1)
    send_entertainment_menu(user_id)


  
  def on_enter_youtube(self, event):
    print("I'm entering youtube")

    reply_token = event.reply_token
    send_text_message(reply_token, "使用示範：\n\n想聽盧廣仲的魚仔？\n請輸入「聽 盧廣仲 魚仔」")


  def on_enter_youtube_ing(self, event):
    print("I'm entering youtube_ing")

    user_id = event.source.user_id
    reply_token = event.reply_token
    query = event.message.text
    send_youtube_video(user_id, reply_token, query)
    self.go_back(event)


  def on_enter_youtube_done(self, event):
    print("I'm entering youtube_done")

    reply_token = event.reply_token
    send_text_message(reply_token, "聽歌不錯吧？")
    self.go_back(event)

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
