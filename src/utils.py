import os
# import bs4
# import requests
# import numpy as np
# from bs4 import BeautifulSoup

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)


def send_text_message(reply_token, text):
  line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

  return "OK"