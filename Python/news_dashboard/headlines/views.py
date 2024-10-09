from django.shortcuts import render
from headlines.models import Headline, Category
# Create your views here.

def get_news_by_category(category_name):
  category = Category.objects.filter(name=category_name).first()
  return Headline.objects.filter(category=category) if category else Headline.objects.none()