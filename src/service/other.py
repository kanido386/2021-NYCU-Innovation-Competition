import os
import time
import Algorithmia

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn

# import bs4
# import requests
# import numpy as np
# from bs4 import BeautifulSoup
from googleapiclient.discovery import build


access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)


def get_foods(food):
  client = Algorithmia.client('sim/bKiRMjrs+PMrFeKsadmIujb1')
  algo = client.algo('kanido386/food_calories/0.2.1')
  algo.set_options(timeout=20, stdout=False)

  try:
    a = {
      "food": food, "option": 2
    }
    foods = algo.pipe(a).result
  except:
    return ['1', '2', '3', '4', '5']

  return foods



def get_calories(food):
  client = Algorithmia.client('sim/bKiRMjrs+PMrFeKsadmIujb1')
  algo = client.algo('kanido386/food_calories/0.2.1')
  algo.set_options(timeout=20, stdout=False)

  try:
    a = {
      "food": food, "option": 1
    }
    calories = algo.pipe(a).result
  except:
    return 100

  return calories



def get_skin_detect_result(img_url):
  client = Algorithmia.client('sim/bKiRMjrs+PMrFeKsadmIujb1')
  algo = client.algo('kanido386/skin_detect/0.2.0')
  algo.set_options(timeout=20, stdout=False)
  
  try:
    probability, symptom_en, symptom = algo.pipe(img_url).result    
  except:
    return 0, 'dummy'

  return probability, symptom_en, symptom



def send_youtube_video(user_id, reply_token, query):
  youTubeApiKey = os.getenv("YOUTUBE_API_KEY", None)
  youtube = build('youtube', 'v3', developerKey=youTubeApiKey)
  query = query[10:]
  request = youtube.search().list(part='snippet', q=query, type='video')
  response = request.execute()
  # The video that is most relevant to the search query
  # firstVideo = response['items'][0]
  Videos = response['items'][0:3]
  # videoId = firstVideo['id']['videoId']
  videoIds = [Videos[i]['id']['videoId'] for i in range(3)]
  # videoUrl = f'https://www.youtube.com/watch?v={videoId}'
  videoUrls = [f'https://www.youtube.com/watch?v={videoId}' for videoId in videoIds]
  # send_text_message(reply_token, videoUrl)

  # TODO: very messy (just for testing)
  # print(Videos[0]['snippet']['title'])
  # print(Videos[0]['snippet']['thumbnails']['high']['url'])

  message = TemplateSendMessage(
      alt_text='Carousel template',
      template=CarouselTemplate(
          # TODO: 可以改用 append 的方式
          columns=[
              CarouselColumn(
                  thumbnail_image_url=Videos[0]['snippet']['thumbnails']['high']['url'],
                  title='This one?',
                  text=Videos[0]['snippet']['title'][:60],
                  actions=[
                      MessageTemplateAction(
                          label='Listen to this',
                          text=videoUrls[0]
                      )
                  ]
              ),
              CarouselColumn(
                  thumbnail_image_url=Videos[1]['snippet']['thumbnails']['high']['url'],
                  title='This one?',
                  text=Videos[1]['snippet']['title'][:60],
                  actions=[
                      MessageTemplateAction(
                          label='Listen to this',
                          text=videoUrls[1]
                      )
                  ]
              ),
              CarouselColumn(
                  thumbnail_image_url=Videos[2]['snippet']['thumbnails']['high']['url'],
                  title='Or this one?',
                  text=Videos[2]['snippet']['title'][:60],
                  actions=[
                      MessageTemplateAction(
                          label='Listen to this',
                          text=videoUrls[2]
                      )
                  ]
              )
          ]
      )
    )

  line_bot_api.push_message(user_id, TextSendMessage(text="Wow, so many videos!"))
  time.sleep(1)
  line_bot_api.push_message(user_id, message)

  return "OK"