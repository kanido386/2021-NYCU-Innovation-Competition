import os
import datetime
import time
from multiprocessing import Process

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from service.basic import send_text_message
from service.firebase import get_user_list
from machine import create_machine
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, static_url_path="")

# Get channel_secret and channel_access_token from environment variable
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

# Unique FSM for each user
machines = {}


def loop_notify_users():
  while True:
    time.sleep(10)
    user_list = get_user_list()
    print('==============================')
    print(user_list)
    print('==============================')
    # Send push message
    # https://developers.line.biz/en/reference/messaging-api/#send-push-message
    now = datetime.datetime.now()
    for user_id in user_list:
      # 原來是時區的問題⋯⋯（13 -> 5）
      # print(now.hour)
      # print(now.hour == 13)
      # print(type(now.hour))
      if now.hour+8 == 13:
        try:
          print('I\'m here!')
          print('==============================')
          line_bot_api.push_message(user_id, TextSendMessage(text='Hello World!'))
          print('==============================')
        except LineBotApiError as e:
          print(e)


@app.route("/webhook", methods=["POST"])
def webhook_handler():
  signature = request.headers["X-Line-Signature"]
  # get request body as text
  body = request.get_data(as_text=True)
  app.logger.info(f"Request body: {body}")

  # parse webhook body
  try:
    events = parser.parse(body, signature)
  except InvalidSignatureError:
    abort(400)

  for event in events:
    if not isinstance(event, MessageEvent):
      continue
    # TODO:
    # if not isinstance(event.message, TextMessage):
    #   continue
    # if not isinstance(event.message.text, str):
    #   continue

    # Create a machine for new user
    user_id = event.source.user_id
    if user_id not in machines:
      machines[user_id] = create_machine()

    # Advance the FSM for each MessageEvent
    response = machines[event.source.user_id].advance(event)
    if response == False:
      # TODO: 使用者輸入沒設定的指令
      # send_text_message(event.reply_token, "Invalid command, try again")
      pass

    print(event)

    # # Echoing
    # send_text_message(event.reply_token, event.message.text)

  return "OK"


if __name__ == "__main__":
  port = os.environ.get("PORT", 8000)
  # https://stackoverflow.com/questions/55436443/how-to-thread-a-flask-app-and-function-with-a-while-loop-to-run-simultaneously
  Process(target=app.run, kwargs=dict(host='0.0.0.0', port=port)).start()
  Process(target=loop_notify_users).start()
  # app.run(host="0.0.0.0", port=port)