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


def send_youtube_video(id, reply_token, query):
  youTubeApiKey = os.getenv("YOUTUBE_API_KEY", None)
  youtube = build('youtube', 'v3', developerKey=youTubeApiKey)
  query = query[2:]
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
                  title='Song 1',
                  text=Videos[0]['snippet']['title'][:60],
                  actions=[
                      MessageTemplateAction(
                          label='聽這首',
                          text=videoUrls[0]
                      )
                  ]
              ),
              CarouselColumn(
                  thumbnail_image_url=Videos[1]['snippet']['thumbnails']['high']['url'],
                  title='Song 2',
                  text=Videos[1]['snippet']['title'][:60],
                  actions=[
                      MessageTemplateAction(
                          label='聽這首',
                          text=videoUrls[1]
                      )
                  ]
              ),
              CarouselColumn(
                  thumbnail_image_url=Videos[2]['snippet']['thumbnails']['high']['url'],
                  title='Song 3',
                  text=Videos[2]['snippet']['title'][:60],
                  actions=[
                      MessageTemplateAction(
                          label='聽這首',
                          text=videoUrls[2]
                      )
                  ]
              )
          ]
      )
    )

  line_bot_api.push_message(id, message)

  return "OK"