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


# def load_from_db(user_id, key):
#   user_doc_ref = db.collection('users').document(user_id)
#   user_doc = user_doc_ref.get().to_dict()
#   value = user_doc[key]
#   return value


# def save_to_db(user_id, key, value, option):
#   user_doc_ref = db.collection('users').document(user_id)
#   user_doc = user_doc_ref.get().to_dict()
#   if option == 'dict':
#     # TODO: very messy
#     try:
#       new_flag = True
#       the_dict = user_doc[key]
#       for a, b in the_dict.items():
#         if a == value:
#           the_dict[a].append(value)
#           new_flag == False
      
#     except:
#       user_doc[key] = {}
#       user_doc_ref.set(user_doc)
#     # user_doc[key] = value
#     # user_doc_ref.set(user_doc)


def write_message(user_id, message):
  user_doc_ref = db.collection('users').document(user_id)
  user_doc = user_doc_ref.get().to_dict()
  user_doc['message'] = message
  user_doc_ref.set(user_doc)


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
  user_doc = user_doc_ref.get().to_dict()
  user_doc['image'] = saving_path
  user_doc_ref.set(user_doc)


def send_image(user_id, reply_token):
  user_doc_ref = db.collection('users').document(user_id)
  user_doc = user_doc_ref.get().to_dict()
  image = user_doc['image']
  blob = bucket.blob(image)
  # generate url for img
  img_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
  send_image_url(reply_token, img_url)


def get_user_list():
  # Get all documents in a collection
  # https://firebase.google.com/docs/firestore/query-data/get-data?authuser=0#get_all_documents_in_a_collection
  user_list = []
  docs = db.collection('users').stream()
  for doc in docs:
    user_list.append(doc.id)
  return user_list