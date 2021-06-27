import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

# 引用私密金鑰
cred = credentials.Certificate("firebase-adminsdk.json")

# 初始化 firebase，注意不能重複初始化
# TODO: 改網址
firebase_admin.initialize_app(credential= cred, options={"storageBucket": "tesfjaksf.appspot.com"})

# 初始化 firestore & storage
db = firestore.client()
bucket = storage.bucket()


def write_message(user_id, message):
  user_doc = db.collection('users').document(user_id)
  user_doc.set({
    'message': message
  })


def read_message(user_id):
  user_doc = db.collection('users').document(user_id)
  message = user_doc['message']
  return message