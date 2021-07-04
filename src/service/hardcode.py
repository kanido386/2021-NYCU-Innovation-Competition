import os
import json

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn, PostbackTemplateAction, QuickReply, QuickReplyButton, MessageAction, DatetimePickerAction, CameraAction, CameraRollAction, FlexSendMessage
from linebot.models.actions import PostbackAction

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)


# def send_menu(user_id):
#   message = TemplateSendMessage(
#       alt_text='選單',
#       template=CarouselTemplate(
#           columns=[
#               CarouselColumn(
#                   thumbnail_image_url='https://cdn2.ettoday.net/images/2850/d2850538.jpg',
#                   title='記錄小幫手',
#                   text='幫您記錄飲食、運動、睡眠',
#                   actions=[
#                       # MessageTemplateAction(
#                       #     label='剛剛吃了什麼？',
#                       #     text='record meal'
#                       # ),
#                       # MessageTemplateAction(
#                       #     label='做了什麼運動？',
#                       #     text='record exercise'
#                       # ),
#                       # MessageTemplateAction(
#                       #     label='睡得怎麼樣呢？',
#                       #     text='record sleeping'
#                       # ),
#                       PostbackTemplateAction(
#                           label='剛剛吃了什麼？',
#                           text='幫我記錄一下食物',
#                           data='record meal'
#                       ),
#                       PostbackTemplateAction(
#                           label='做了什麼運動？',
#                           text='我剛剛有做運動喔',
#                           data='record exercise'
#                       ),
#                       PostbackTemplateAction(
#                           label='睡得怎麼樣呢？',
#                           text='記錄一下睡眠',
#                           data='record sleeping'
#                       ),
#                   ]
#               ),
#               CarouselColumn(
#                   thumbnail_image_url='https://cdn2.ettoday.net/images/2850/d2850538.jpg',
#                   title='心情隨身貼',
#                   text='跟我分享您的心情吧！',
#                   actions=[
#                       # MessageTemplateAction(
#                       #     label='現在心情怎麼樣？',
#                       #     text='share mood'
#                       # ),
#                       # MessageTemplateAction(
#                       #     label='有什麼想對我說的嗎？',
#                       #     text='share diary'
#                       # ),
#                       # MessageTemplateAction(
#                       #     label='娛樂專區',
#                       #     text='entertainment'
#                       # ),
#                       PostbackTemplateAction(
#                           label='現在心情怎麼樣？',
#                           text='跟你分享一下我現在的心情',
#                           data='share mood'
#                       ),
#                       PostbackTemplateAction(
#                           label='有什麼想對我說的嗎？',
#                           text='有事情想跟你說',
#                           data='share diary'
#                       ),
#                       PostbackTemplateAction(
#                           label='娛樂專區',
#                           text='來點娛樂',
#                           data='entertainment'
#                       ),
#                   ]
#               ),
#               CarouselColumn(
#                   thumbnail_image_url='https://cdn2.ettoday.net/images/2850/d2850538.jpg',
#                   title='健康助理',
#                   text='您的健康，我關心！',
#                   actions=[
#                       # MessageTemplateAction(
#                       #     label='身體哪裡不舒服呢？',
#                       #     text='encyclopedia'
#                       # ),
#                       URITemplateAction(
#                           label='身體哪裡不舒服呢？',
#                           uri='https://liff.line.me/1656147392-8PJxaVx3'
#                       ),
#                       PostbackTemplateAction(
#                           label='膚況分析',
#                           text='我皮膚上有怪東西欸 幫我看一下',
#                           data='skin'
#                       ),
#                       PostbackTemplateAction(
#                           label='今日健康報告',
#                           text='我想看我今天的健康狀況',
#                           data='report'
#                       ),
#                       # MessageTemplateAction(
#                       #     label='膚況分析',
#                       #     text='skin'
#                       # ),
#                       # MessageTemplateAction(
#                       #     label='今日健康報告',
#                       #     text='report'
#                       # ),
#                   ]
#               )
#           ]
#       )
#   )
#   line_bot_api.push_message(user_id, message)

#   return "OK"


def send_menu(user_id, option):
  columns=[
      CarouselColumn(
          thumbnail_image_url='https://i.imgur.com/0KZKuFH.png',
          imageSize='contain',
          title='Record Taker',
          text='Help you record meal, exercise and sleep',
          actions=[
              # MessageTemplateAction(
              #     label='剛剛吃了什麼？',
              #     text='record meal'
              # ),
              # MessageTemplateAction(
              #     label='做了什麼運動？',
              #     text='record exercise'
              # ),
              # MessageTemplateAction(
              #     label='睡得怎麼樣呢？',
              #     text='record sleeping'
              # ),
              PostbackTemplateAction(
                  label='What did you eat?',
                  text='Help me record the meal',
                  data='record meal'
              ),
              PostbackTemplateAction(
                  label='Record exercise',
                  text='I just did exercise!',
                  data='record exercise'
              ),
              PostbackTemplateAction(
                  label='How is your sleep?',
                  text='Help me record my sleep',
                  data='record sleeping'
              ),
          ]
      ),
      CarouselColumn(
          thumbnail_image_url='https://i.imgur.com/JSw3v2z.png',
          title='Cheer-up Buddy',
          text='Share your feelings with me!',
          actions=[
              # MessageTemplateAction(
              #     label='現在心情怎麼樣？',
              #     text='share mood'
              # ),
              # MessageTemplateAction(
              #     label='有什麼想對我說的嗎？',
              #     text='share diary'
              # ),
              # MessageTemplateAction(
              #     label='娛樂專區',
              #     text='entertainment'
              # ),
              PostbackTemplateAction(
                  label='How\'s your feeling?',
                  text='I want to share with you my current mood',
                  data='share mood'
              ),
              PostbackTemplateAction(
                  label='Share something',
                  text='I want to tell you something',
                  data='share diary'
              ),
              PostbackTemplateAction(
                  label='Entertainment area',
                  text='Need entertainment!',
                  data='entertainment'
              ),
          ]
      ),
      CarouselColumn(
          thumbnail_image_url='https://i.imgur.com/T8IHOZu.png',
          title='Health Assistant',
          text='I care about your health!',
          actions=[
              # MessageTemplateAction(
              #     label='身體哪裡不舒服呢？',
              #     text='encyclopedia'
              # ),
              URITemplateAction(
                  label='Not feeling good?',
                  uri='https://liff.line.me/1656147392-8PJxaVx3'
              ),
              PostbackTemplateAction(
                  label='Skin analysis',
                  text='I have something weird on my skin, please help me see it',
                  data='skin'
              ),
              PostbackTemplateAction(
                  label='Health report',
                  text='I want to see my health condition today',
                  data='report'
              ),
              # MessageTemplateAction(
              #     label='膚況分析',
              #     text='skin'
              # ),
              # MessageTemplateAction(
              #     label='今日健康報告',
              #     text='report'
              # ),
          ]
      )
  ]
  message = TemplateSendMessage(
      alt_text='Menu',
      template=CarouselTemplate(
          columns=[columns[option]]
      )
  )
  line_bot_api.push_message(user_id, message)

  return "OK"




def send_entertainment_menu(user_id):
    message = TemplateSendMessage(
        alt_text='Menu',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/zsdGcIH.png',
                    title='Entertainment area',
                    text='（Enter [Exit] to return to the menu）',
                    actions=[
                        # MessageTemplateAction(
                        #     label='聽音樂',
                        #     text='youtube'
                        # ),
                        # MessageTemplateAction(
                        #     label='\U0001f431 我的寵物 \U0001f436',
                        #     text='pet'
                        # ),
                        PostbackTemplateAction(
                            label='Listen to music',
                            text='I want to listen to songs',
                            data='youtube'
                        ),
                        PostbackTemplateAction(
                            label='\U0001f431 My pet \U0001f436',
                            text='Pet pet',
                            data='pet'
                        ),
                        # TODO:
                        # MessageTemplateAction(
                        #     label='給我好笑的',
                        #     text='joke'
                        # ),
                        # TODO: 有bug 玩完遊戲以後不能點聽音樂⋯⋯
                        URITemplateAction(
                            label='Play a game',
                            uri='https://liff.line.me/1656147392-7bZOXoOQ'
                        )
                    ]
                ),              
            ]
        )
    )
    line_bot_api.push_message(user_id, message)

    return "OK"


def quick_reply_mood_grade(user_id):
  message = TextSendMessage(
    text='1~10 How do you score your mood?',
    quick_reply=QuickReply(
        items=[
            # QuickReplyButton(
            #     action=PostbackAction(label="label1", data="data1")
            # ),
            QuickReplyButton(
                action=MessageAction(label="1", text="1")
            ),
            QuickReplyButton(
                action=MessageAction(label="2", text="2")
            ),
            QuickReplyButton(
                action=MessageAction(label="3", text="3")
            ),
            QuickReplyButton(
                action=MessageAction(label="4", text="4")
            ),
            QuickReplyButton(
                action=MessageAction(label="5", text="5")
            ),
            QuickReplyButton(
                action=MessageAction(label="6", text="6")
            ),
            QuickReplyButton(
                action=MessageAction(label="7", text="7")
            ),
            QuickReplyButton(
                action=MessageAction(label="8", text="8")
            ),
            QuickReplyButton(
                action=MessageAction(label="9", text="9")
            ),
            QuickReplyButton(
                action=MessageAction(label="10",text="10")
            ),
      ]))
  line_bot_api.push_message(user_id, message)

  return "OK"



def quick_reply_food(user_id, option1, option2, option3, option4, option5, option6, option7, option8, option9, option10):
  message = TextSendMessage(
    text='Which food is closest to your food?',
    quick_reply=QuickReply(
        items=[
            # QuickReplyButton(
            #     action=PostbackAction(label="label1", data="data1")
            # ),
            QuickReplyButton(
                action=MessageAction(label=f"{option1}", text=f"{option1}")
            ),
            QuickReplyButton(
                action=MessageAction(label=f"{option2}", text=f"{option2}")
            ),
            QuickReplyButton(
                action=MessageAction(label=f"{option3}", text=f"{option3}")
            ),
            QuickReplyButton(
                action=MessageAction(label=f"{option4}", text=f"{option4}")
            ),
            QuickReplyButton(
                action=MessageAction(label=f"{option5}", text=f"{option5}")
            ),
            QuickReplyButton(
                action=MessageAction(label=f"{option6}", text=f"{option6}")
            ),
            QuickReplyButton(
                action=MessageAction(label=f"{option7}", text=f"{option7}")
            ),
            QuickReplyButton(
                action=MessageAction(label=f"{option8}", text=f"{option8}")
            ),
            QuickReplyButton(
                action=MessageAction(label=f"{option9}", text=f"{option9}")
            ),
            QuickReplyButton(
                action=MessageAction(label=f"{option10}", text=f"{option10}")
            ),
      ]))
  line_bot_api.push_message(user_id, message)

  return "OK"



def quick_reply_sleeping(user_id, mode):
  text = 'What time did you go to bed last night?' if mode == 'sleep' else 'What time did you get up today?'
  label = 'Choose bed time' if mode == 'sleep' else 'Choose wake up time'
  message = TextSendMessage(
    text=text,
    quick_reply=QuickReply(
        items=[
            QuickReplyButton(
                action=DatetimePickerAction(label=label,
                                            data="sleep",
                                            mode="time")
            ),
            
      ]))
  line_bot_api.push_message(user_id, message)

  return "OK"


def quick_reply_skin(user_id):
  message = TextSendMessage(
    text='Show me the photo!',
    quick_reply=QuickReply(
        items=[
            QuickReplyButton(
                action=CameraAction(label="Take a picture")
            ),
            QuickReplyButton(
                action=CameraRollAction(label="Choose from gallery")
            ),
            
      ]))
  line_bot_api.push_message(user_id, message)

  return "OK"







def push_health_report(user_id):
  # https://www.line-community.me/en/question/5d405945851f743fd7cd97c6
  flex_message_json_string = """
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_5_carousel.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "How Much More",
            "wrap": true,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Calories : ",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              },
              {
                "type": "text",
                "text": "500",
                "wrap": true,
                "weight": "bold",
                "size": "md",
                "flex": 0
              },
              {
                "type": "text",
                "text": "kcal",
                "wrap": true,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ],
            "spacing": "md"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Protein : ",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              },
              {
                "type": "text",
                "text": "20",
                "wrap": true,
                "weight": "bold",
                "size": "md",
                "flex": 0
              },
              {
                "type": "text",
                "text": "g",
                "wrap": true,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ],
            "spacing": "md"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Carbonhydrate : ",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              },
              {
                "type": "text",
                "text": "60",
                "wrap": true,
                "weight": "bold",
                "size": "md",
                "flex": 0
              },
              {
                "type": "text",
                "text": "g",
                "wrap": true,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ],
            "spacing": "md"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Fat : ",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              },
              {
                "type": "text",
                "text": "20",
                "wrap": true,
                "weight": "bold",
                "size": "md",
                "flex": 0
              },
              {
                "type": "text",
                "text": "g",
                "wrap": true,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ],
            "spacing": "md"
          },
          {
            "type": "separator",
            "margin": "xxl",
            "color": "#808080"
          },
          {
            "type": "text",
            "text": "The Past Week Avg.",
            "wrap": true,
            "weight": "bold",
            "size": "xl",
            "offsetTop": "sm",
            "align": "start"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Calories : ",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              },
              {
                "type": "text",
                "text": "2000",
                "wrap": true,
                "weight": "bold",
                "size": "md",
                "flex": 0
              },
              {
                "type": "text",
                "text": "kcal",
                "wrap": true,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ],
            "spacing": "md",
            "paddingTop": "sm"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Protein : ",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              },
              {
                "type": "text",
                "text": "50",
                "wrap": true,
                "weight": "bold",
                "size": "md",
                "flex": 0
              },
              {
                "type": "text",
                "text": "g",
                "wrap": true,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ],
            "spacing": "md"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Carbonhydrate : ",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              },
              {
                "type": "text",
                "text": "100",
                "wrap": true,
                "weight": "bold",
                "size": "md",
                "flex": 0
              },
              {
                "type": "text",
                "text": "g",
                "wrap": true,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ],
            "spacing": "md"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "Fat : ",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              },
              {
                "type": "text",
                "text": "40",
                "wrap": true,
                "weight": "bold",
                "size": "md",
                "flex": 0
              },
              {
                "type": "text",
                "text": "g",
                "wrap": true,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ],
            "spacing": "md"
          },
          {
            "type": "separator",
            "margin": "xxl",
            "color": "#808080"
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_6_carousel.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "Frequent symptoms in the past month",
            "wrap": true,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "－",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              },
              {
                "type": "text",
                "text": "Headache",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              }
            ],
            "spacing": "md"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "－",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              },
              {
                "type": "text",
                "text": "Stomachache",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              }
            ],
            "spacing": "md"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "－",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              },
              {
                "type": "text",
                "text": "Allergy",
                "wrap": true,
                "weight": "bold",
                "size": "lg",
                "flex": 0
              }
            ],
            "spacing": "md"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#45baae",
            "action": {
              "type": "uri",
              "label": "Check out DeepQ for more",
              "uri": "https://dzs.deepq.com/"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_6_carousel.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "Mood in the past week",
            "wrap": true,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "6",
                "wrap": true,
                "weight": "bold",
                "size": "5xl",
                "flex": 0,
                "margin": "none",
                "offsetTop": "lg",
                "offsetBottom": "lg"
              }
            ],
            "spacing": "md",
            "justifyContent": "center"
          },
          {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "margin": "none",
            "size": "full"
          }
        ]
      }
    }
  ]
}
"""
  flex_message_json_dict = json.loads(flex_message_json_string)
  message = FlexSendMessage(
      alt_text="Health report",
      contents=flex_message_json_dict
  )
  line_bot_api.push_message(user_id, message)
