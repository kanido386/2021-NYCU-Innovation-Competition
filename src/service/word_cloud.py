import jieba
from wordcloud import WordCloud
from .firebase import send_wordcloud, upload_wordcloud


def word_cloud(user_id, text):

  # Tokenize
  token = ' '.join(jieba.cut(text))

  # WordCloud
  wc = WordCloud(
    max_words=30,
    font_path='NotoSansCJKjp-Bold.otf',
    max_font_size=40,
    background_color='white',
    random_state=42,
    relative_scaling=0
  )
  cloud = wc.generate(token)

  output_file = f'{user_id}.png'
  cloud.to_file(output_file)

  upload_wordcloud(user_id, output_file)
  send_wordcloud(user_id)