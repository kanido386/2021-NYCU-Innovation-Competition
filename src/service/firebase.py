import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

import os
import datetime

from .basic import send_image_url

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn

# 引用私密金鑰
cred = credentials.Certificate("firebase-adminsdk.json")

# 初始化 firebase，注意不能重複初始化
# TODO: 改網址
firebase_admin.initialize_app(credential= cred, options={"storageBucket": "tesfjaksf.appspot.com"})

# 初始化 firestore & storage
db = firestore.client()
bucket = storage.bucket()

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)


def write_message(user_id, message):
  user_doc_ref = db.collection('users').document(user_id)
  user_doc_ref.set({
    'message': message
  })


def read_message(user_id):
  user_doc_ref = db.collection('users').document(user_id)
  user_doc = user_doc_ref.get().to_dict()
  message = user_doc['message']
  return message


def upload_image(user_id, message_id, file_name):
  message_content = line_bot_api.get_message_content(message_id)
  temp_file_path = user_id
  with open(temp_file_path, 'wb') as fd:
    for chunk in message_content.iter_content():
      fd.write(chunk)
  
  saving_path = f'{user_id}/{file_name}'
  blob = bucket.blob(saving_path)

  with open(temp_file_path, 'rb') as photo:
    blob.upload_from_file(photo)

  os.remove(temp_file_path)
  
  user_doc_ref = db.collection('users').document(user_id)
  user_doc_ref.set({
    'image': saving_path
  })


def send_image(user_id, reply_token):
  user_doc_ref = db.collection('users').document(user_id)
  user_doc = user_doc_ref.get().to_dict()
  image = user_doc['image']
  blob = bucket.blob(image)
  # generate url for img
  img_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
  send_image_url(reply_token, img_url)