import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_dashboard.settings')

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')  # Adjust the path accordingly



import django
django.setup()

from headlines.models import Category, Headline
import streamlit as st

def fetch_news(category_name):
  category = Category.objects.filter(name=category_name).first()
  return Headline.objects.filter(category=category)

st.title("Trending News Dashboard")

categories = Category.objects.all()
category_choice = st.selectbox("Choose a category", [c.name for c in categories] )

if st.button('Fetch News'):
  news = fetch_news(category_choice)
  for headline in news:
    st.markdown(f'### [{headline.title}]({headline.link})')
    st.write('---')

if st.button('Refresh'):
  os.system("python manage.py scrape_news")