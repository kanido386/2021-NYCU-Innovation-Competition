import os

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)


def send_menu(user_id):
  message = TemplateSendMessage(
      alt_text='選單',
      template=CarouselTemplate(
          columns=[
              CarouselColumn(
                  thumbnail_image_url='https://cdn2.ettoday.net/images/2850/d2850538.jpg',
                  title='記錄小幫手',
                  text='幫您記錄飲食、運動、睡眠',
                  actions=[
                      MessageTemplateAction(
                          label='剛剛吃了什麼？',
                          text='record meal'
                      ),
                      MessageTemplateAction(
                          label='做了什麼運動？',
                          text='record exercise'
                      ),
                      MessageTemplateAction(
                          label='睡得怎麼樣呢？',
                          text='record sleeping'
                      )
                  ]
              ),
              CarouselColumn(
                  thumbnail_image_url='https://cdn2.ettoday.net/images/2850/d2850538.jpg',
                  title='心情隨身貼',
                  text='跟我分享您的心情吧！',
                  actions=[
                      MessageTemplateAction(
                          label='現在心情怎麼樣？',
                          text='share mood'
                      ),
                      MessageTemplateAction(
                          label='有什麼想對我說的嗎？',
                          text='share diary'
                      ),
                      MessageTemplateAction(
                          label='娛樂專區',
                          text='entertainment'
                      ),
                  ]
              ),
              CarouselColumn(
                  thumbnail_image_url='https://cdn2.ettoday.net/images/2850/d2850538.jpg',
                  title='健康助理',
                  text='您的健康，我關心！',
                  actions=[
                      MessageTemplateAction(
                          label='身體哪裡不舒服呢？',
                          text='encyclopedia'
                      ),
                      MessageTemplateAction(
                          label='膚況分析',
                          text='skin'
                      ),
                      MessageTemplateAction(
                          label='今日健康報告',
                          text='report'
                      ),
                  ]
              )
          ]
      )
  )
  line_bot_api.push_message(user_id, message)

  return "OK"