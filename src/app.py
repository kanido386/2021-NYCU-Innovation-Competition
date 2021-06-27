import os

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from service.basic import send_text_message
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
    if not isinstance(event.message, TextMessage):
      continue
    if not isinstance(event.message.text, str):
      continue

    # Create a machine for new user
    if event.source.user_id not in machines:
      machines[event.source.user_id] = create_machine()

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
  app.run(host="0.0.0.0", port=port)