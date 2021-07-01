import os

import jieba
from wordcloud import WordCloud
from .firebase import send_wordcloud, upload_wordcloud


def word_cloud(user_id, text):

  # Tokenize
  token = ' '.join(jieba.cut(text))

  # d = os.getcwd()
  # font_path = d + 'src/service/NotoSansCJKjp-Bold.otf'
  # print(font_path)

  # WordCloud
  wc = WordCloud(
    max_words=50,
    # font_path=font_path,
    font_path='NotoSansCJKjp-Bold.otf',
    max_font_size=50,
    background_color='white',
    random_state=42,
    relative_scaling=0.5
  )
  cloud = wc.generate(token)

  output_file = f'{user_id}.png'
  cloud.to_file(output_file)

  upload_wordcloud(user_id, output_file)
  send_wordcloud(user_id)