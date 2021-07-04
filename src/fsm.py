from os import getcwd
from transitions.extensions import GraphMachine
import datetime
import time
import random

from service.basic import send_text_message, push_text_message
from service.other import send_youtube_video, get_skin_detect_result, get_foods, get_calories
from service.blockchain import users, service_tokens
from service.firebase import write_message, read_message, upload_skin_image, send_image, get_skin_image_url, write_to_db, read_from_db
from service.hardcode import send_menu, send_entertainment_menu, quick_reply_mood_grade, quick_reply_sleeping, quick_reply_skin, push_health_report, quick_reply_food
from service.word_cloud import word_cloud

class TocMachine(GraphMachine):
  def __init__(self, **machine_configs):
    self.machine = GraphMachine(model=self, **machine_configs)


  # def is_going_to_menu(self, event):
  #   if event.type == 'postback':
  #     return "哈囉" in event.postback.data
  #   try:
  #     text = event.message.text # TODO:
  #   except:
  #     text = event.postback.data
  #   return "哈囉" in text


  def is_going_to_mood(self, event):
    if event.type == 'postback':
      return event.postback.data == "share mood"
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return text.lower() == "share mood"

  def is_going_to_mood_detailed(self, event):
    return True

  def is_going_to_mood_done(self, event):
    return True


  def is_going_to_meal(self, event):
    if event.type == 'postback':
      return event.postback.data == "record meal"
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return text.lower() == "record meal"

  def is_going_to_meal_search(self, event):
    return True

  def is_going_to_meal_report(self, event):
    # return event.type == 'postback'
    return True

  def is_going_to_meal_input(self, event):
    return True

  def is_going_to_meal_reward(self, event):
    return True


  def is_going_to_diary(self, event):
    if event.type == 'postback':
      return event.postback.data == "share diary"
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return text.lower() == "share diary"

  def is_going_to_diary_done(self, event):
    return True


  def is_going_to_exercise(self, event):
    if event.type == 'postback':
      return event.postback.data == "record exercise"
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return text.lower() == "record exercise"

  def is_going_to_exercise_done(self, event):
    return True


  def is_going_to_sleeping(self, event):
    if event.type == 'postback':
      return event.postback.data == "record sleeping"
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return text.lower() == "record sleeping"

  def is_going_to_sleeping_up(self, event):
    return True

  def is_going_to_sleeping_done(self, event):
    return True

  
  def is_going_to_skin(self, event):
    if event.type == 'postback':
      return event.postback.data == "skin"
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return text.lower() == "skin"

  def is_going_to_skin_process(self, event):
    return event.message.type == "image"

  def is_going_to_skin_done(self, event):
    return True


  def is_going_to_report(self, event):
    if event.type == 'postback':
      return event.postback.data == "report"
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return text.lower() == "report"


  def is_going_to_entertainment(self, event):
    if event.type == 'postback':
      return event.postback.data == "entertainment"
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return text.lower() == "entertainment"

  def is_going_to_exit(self, event):
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    user_id = event.source.user_id
    # push_text_message(user_id, "Back to the lobby!")
    return "Exit" in text


  def is_going_to_youtube(self, event):
    if event.type == 'postback':
      return event.postback.data == "youtube"
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return text.lower() == "youtube"

  def is_going_to_youtube_exit(self, event):
    # go to entertainment
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return "Exit" in text

  def is_going_to_youtube_ing(self, event):
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return "Listen to" in text

  def is_going_to_youtube_done(self, event):
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    return "Exit" in text
  
  
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

  # def on_enter_menu(self, event):
  #   print("I'm entering menu")

  #   user_id = event.source.user_id
  #   time.sleep(2)
  #   # TODO:
  #   send_menu(user_id, 1)
  #   self.go_back()


  def on_enter_mood(self, event):
    print("I'm entering mood")

    # reply_token = event.reply_token
    # send_text_message(reply_token, "1~10 你打幾分呢？")
    user_id = event.source.user_id
    time.sleep(1)
    quick_reply_mood_grade(user_id)


  def on_enter_mood_detailed(self, event):
    print("I'm entering mood_detailed")

    user_id = event.source.user_id
    reply_token = event.reply_token
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data

    now = datetime.datetime.now()
    today = f'{now.year}-{now.month}-{now.day}'

    try:
      score = int(text)
    except:
      # send_text_message(reply_token, "請輸入數字 1~10 哦～")
      # TODO: would have bug
      self.go_back(event)

    # 存心情分數
    mood_grade = read_from_db(user_id, 'mood_grade')
    # TODO: 用 =x30 
    mood_grade += f'=============================={score}'
    write_to_db(user_id, 'mood_grade', mood_grade)

    if score >= 1 and score <= 5:
      # save_to_db(user_id, 'mood', {today: score}, 'dict')
      # value = load_from_db(user_id, 'mood')
      # print('==============================')
      # print(value)
      # print(type(value))
      # print('==============================')
      send_text_message(reply_token, "What's happening?")
    elif score >= 6 and score <= 10:
      send_text_message(reply_token, "What makes you feel good?")
    else:
      send_text_message(reply_token, "Please enter the numbers 1~10")
      # TODO: would have bug
      self.go_back(event)


  def on_enter_mood_done(self, event):
    print("I'm entering mood_done")

    reply_token = event.reply_token

    # 存詳細
    user_id = event.source.user_id
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    mood_detail = read_from_db(user_id, 'mood_detail')
    # TODO: 用 =x30 
    mood_detail += f'=============================={text}'
    write_to_db(user_id, 'mood_detail', mood_detail)
    
    # TODO: 獲得健康幣
    send_text_message(reply_token, "Got it!")
    self.go_back(event)



  def on_enter_meal(self, event):
    print("I'm entering meal")

    reply_token = event.reply_token
    send_text_message(reply_token, "Please enter the name of the food")


  def on_enter_meal_search(self, event):
    print("I'm entering meal_search")

    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    # 從食物資料庫裡面找推薦食物清單
    # {"food": "草莓果醬", "option": 1}
    foods = get_foods(text)
    a, b, c, d, e, f, g, h, i, j = foods
    user_id = event.source.user_id
    quick_reply_food(user_id, a, b, c, d, e, f, g, h, i, j)
    # TODO:
    # self.yes(event)
    # if text == 'yes':
    #   self.yes(event)
    # else:
    #   self.no(event)

  def on_enter_meal_report(self, event):
    print("I'm entering meal_report")

    reply_token = event.reply_token
    # TODO: 存資料庫
    # 回報卡路里
    try:
      food = event.message.text # TODO:
    except:
      food = event.postback.data
    calories = get_calories(food)
    send_text_message(reply_token, f'Food calories: {calories} Kcal')
    self.go_back(event)


  def on_enter_meal_input(self, event):
    print("I'm entering meal_input")

    reply_token = event.reply_token
    send_text_message(reply_token, "Please enter food related information")

  # def is_going_to_read_message(self, event):
  #   text = event.message.text
  #   return text.lower() == "message"

  def on_enter_meal_reward(self, event):
    print("I'm entering meal_reward")

    reply_token = event.reply_token
    # TODO: 存資料庫
    # TODO: 獲得健康幣
    amount = 5
    # send_text_message(reply_token, f'感謝您的回饋，送您 {amount} 枚健康幣～')
    send_text_message(reply_token, f'Thanks for your feedback!')
    self.go_back(event)


  # def is_going_to_see_image(self, event):
  #   print(event)
  #   text = event.message.text
  #   return text.lower() == "see image"

  def on_enter_diary(self, event):
    print("I'm entering diary")

    reply_token = event.reply_token
    send_text_message(reply_token, "Share with me!")

  
  def on_enter_diary_done(self, event):
    print("I'm entering diary_done")

    reply_token = event.reply_token
    
    # 產生文字雲
    user_id = event.source.user_id
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    word_cloud(user_id, text)

    # 存資料庫
    diary = read_from_db(user_id, 'diary')
    # print('==============================')
    # print(diary)
    # print('==============================')
    # TODO: 用 =x30 
    diary += f'=============================={text}'
    write_to_db(user_id, 'diary', diary)
    


    # TODO: 獲得健康幣（或許可以根據字數來決定數量）
    amount = 5
    # send_text_message(reply_token, f'謝謝您的分享，送您 {amount} 枚健康幣～')
    send_text_message(reply_token, f'Thanks for your sharing!')
    self.go_back(event)



  def on_enter_exercise(self, event):
    print("I'm entering exercise")

    reply_token = event.reply_token
    send_text_message(reply_token, "Nice~ Tell me what exercise you just did")

  
  def on_enter_exercise_done(self, event):
    print("I'm entering exercise_done")

    reply_token = event.reply_token

    # 存資料庫
    user_id = event.source.user_id
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    exercise = read_from_db(user_id, 'exercise')
    # TODO: 用 =x30 
    exercise += f'=============================={text}'
    write_to_db(user_id, 'exercise', exercise)


    # TODO: 獲得健康幣
    amount = 5
    # send_text_message(reply_token, f'運動身體好，送您 {amount} 枚健康幣～')
    send_text_message(reply_token, f'Sports is good for health!')
    self.go_back(event)



  def on_enter_sleeping(self, event):
    print("I'm entering sleeping")

    reply_token = event.reply_token
    user_id = event.source.user_id
    # TODO:
    # push_text_message(user_id, "輸入格式：\n24小時制 hh:mm")
    # send_text_message(reply_token, "昨晚幾點睡呢？")
    quick_reply_sleeping(user_id, 'sleep')



  def on_enter_sleeping_up(self, event):
    print("I'm entering sleeping_up")

    # 存資料庫
    user_id = event.source.user_id
    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    text = event.postback.params['time']
    print('==============================')
    print(text)
    print('==============================')
    hour = int(text.split(':')[0])
    minute = int(text.split(':')[1])
    write_to_db(user_id, 'sleeping', (hour, minute))

    # reply_token = event.reply_token
    # send_text_message(reply_token, "今天幾點幾床？")
    quick_reply_sleeping(user_id, 'up')

  
  def on_enter_sleeping_done(self, event):
    print("I'm entering sleeping_done")

    reply_token = event.reply_token
    
    # 讀資料庫
    user_id = event.source.user_id
    hour_night, minute_night = read_from_db(user_id, 'sleeping')
    hour_night = hour_night - 24 if hour_night >= 18 else hour_night

    try:
      text = event.message.text # TODO:
    except:
      text = event.postback.data
    print('==============================')
    print(event.postback.params)
    print('==============================')
    text = event.postback.params['time']
    hour = int(text.split(':')[0])
    minute = int(text.split(':')[1])

    minute -= minute_night
    if minute < 0:
      minute += 60
      hour -= 1
    hour -= hour_night

    # 存資料庫    
    write_to_db(user_id, 'sleeping', (hour, minute))
    
    send_text_message(reply_token, f'You slept {hour} hours {minute} minutes.\nRemember, Sleep is also very important!')
    self.go_back(event)



  def on_enter_skin(self, event):
    print("I'm entering skin")

    # reply_token = event.reply_token
    # send_text_message(reply_token, "照片傳給我看吧！")
    user_id = event.source.user_id
    quick_reply_skin(user_id)

  # # def on_exit_state1(self):
  # #   print("Leaving state1")

  def on_enter_skin_process(self, event):
    print("I'm entering skin_process")

    user_id = event.source.user_id
    message_id = event.message.id
    file_name = str(event.timestamp) + ".jpg"
    upload_skin_image(user_id, message_id, file_name)

    reply_token = event.reply_token
    push_text_message(user_id, "Photo analyzing, please wait...")
    self.advance(event)

  
  def on_enter_skin_done(self, event):
    print("I'm entering skin_done")

    reply_token = event.reply_token

    # 回報預測結果
    user_id = event.source.user_id
    img_url = get_skin_image_url(user_id)
    probability, symptom, symptom_zh = get_skin_detect_result(img_url)
    # chance = [30, 60, 80]
    # accuracy = random.choice(chance)
    # result = '紅疹'
    probability = max(probability) * 100
    if probability < 70:
      send_text_message(reply_token, f'The photo may not be clear enough, please take another one!')
    else:
      remind ="""This inspection is powered by computer vision
（testing data accuracy is up to 97%）

Can distinguish:

1. actinic keratoses and intraepithelial carcinomae(Cancer)
2. basal cell carcinoma(Cancer)
3. benign keratosis-like lesions(Non-Cancerous)
4. dermatofibroma(Non-Cancerous)
5. melanocytic nevi(Non-Cancerous)
6. pyogenic granulomas and hemorrhage(Can lead to cancer)
7. melanoma(Cancer)

these 7 symptoms

Since it is not judged by a professional doctor.
If you have any questions,
Please further consult with medical institutions~"""
      push_text_message(user_id, remind)
      send_text_message(reply_token, f'I have {probability:.2f}% confidence that it might be: \n{symptom}')

    # 存資料庫
    write_to_db(user_id, 'skin_result', symptom)
    self.go_back(event)



  def on_enter_report(self, event):
    print("I'm entering report")

    reply_token = event.reply_token
    user_id = event.source.user_id
    # TODO: 健康狀況回報
#     year = datetime.datetime.now().year
#     month = datetime.datetime.now().month
#     day = datetime.datetime.now().day
#     diaries = '\n'.join(read_from_db(user_id, 'diary').split('==============================')[1:])
#     exercises = '\n'.join(read_from_db(user_id, 'exercise').split('==============================')[1:])
#     mood_grades = ' - '.join(read_from_db(user_id, 'mood_grade').split('==============================')[1:])
#     mood_details = '\n'.join(read_from_db(user_id, 'mood_detail').split('==============================')[1:])
#     skin_result = read_from_db(user_id, 'skin_result')
#     sleeping = read_from_db(user_id, 'sleeping')
#     report = f"""{year}/{month}/{day}/\n\n=====\n
# 小日記：\n\n{diaries}\n\n=====\n\n做了哪些運動：\n\n{exercises}\n\n=====\n\n心情分數：\n\n{mood_grades}\n\n心情隨筆：\n\n{mood_details}\n\n=====\n
# 膚況：\n\n{skin_result}\n\n=====\n\n睡眠時間：\n\n{sleeping[0]} 小時 {sleeping[1]} 分鐘\n\n=====\n\n祝您天天健康！"""
#     send_text_message(reply_token, report)
    # TODO: flex message
    push_health_report(user_id)
    self.go_back(event)



  def on_enter_entertainment(self, event):
    print("I'm entering entertainment")

    user_id = event.source.user_id
    time.sleep(1)
    send_entertainment_menu(user_id)


  
  def on_enter_youtube(self, event):
    print("I'm entering youtube")

    reply_token = event.reply_token
    send_text_message(reply_token, "Example:\n\nWant to listen to Bruno Mars' Grenade?\nJust Enter \"Listen to Bruno Mars Grenade\"\n\nIf you want to exit, please input \"Exit\"")
    self.advance(event)


  def on_enter_youtube_ing(self, event):
    print("I'm entering youtube_ing")

    user_id = event.source.user_id
    reply_token = event.reply_token
    query = event.message.text
    send_youtube_video(user_id, reply_token, query)


  def on_enter_youtube_done(self, event):
    print("I'm entering youtube_done")

    reply_token = event.reply_token
    send_text_message(reply_token, "Listening to songs is great right?")
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
