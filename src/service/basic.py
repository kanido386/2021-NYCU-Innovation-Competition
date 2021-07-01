import os

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)


def push_text_message(user_id, text):
  line_bot_api.push_message(user_id, TextSendMessage(text=text))
  return "OK"


def send_text_message(reply_token, text):
  line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
  return "OK"


def send_image_url(reply_token, img_url):
  message = ImageSendMessage(
    original_content_url=img_url,
    preview_image_url=img_url
  )
  line_bot_api.reply_message(reply_token, message)

  return "OK"


def push_image_url(user_id, img_url):
  message = ImageSendMessage(
    original_content_url=img_url,
    preview_image_url=img_url
  )
  line_bot_api.push_message(user_id, message)

  return "OK"