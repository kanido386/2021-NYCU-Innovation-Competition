import os

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn

# import bs4
# import requests
# import numpy as np
# from bs4 import BeautifulSoup
from googleapiclient.discovery import build


access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)


def send_text_message(reply_token, text):
  line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
  return "OK"


def send_youtube_video(reply_token, query):
  youTubeApiKey = os.getenv("YOUTUBE_API_KEY", None)
  youtube = build('youtube', 'v3', developerKey=youTubeApiKey)
  query = query[2:]
  request = youtube.search().list(part='snippet', q=query, type='video')
  response = request.execute()
  # The video that is most relevant to the search query
  firstVideo = response['items'][0]
  videoId = firstVideo['id']['videoId']
  videoUrl = f'https://www.youtube.com/watch?v={videoId}'
  send_text_message(reply_token, videoUrl)
  return "OK"