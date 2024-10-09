# News Dashboard

An easy Django application, that fetches top news from 'https://news.ycombinator.com' using simple web-scraping with BO4

## Prerequisites

- Python 3.11.9
- pip (Python package installer)

## Setting Up the Environment

git clone https://github.com/Inckrisz/Portfolio.git
cd Portfolio/Python/news_dashboard

1. **Create a Python virtual environment** using `pyenv`:
   ```bash
   pyenv install local or global 3.11.9
   pyenv virtualenv 3.11.9 news_dashboard_env
   pyenv activate news_dashboard_env
   pip install -r requirements.txt
   ```bash

# Setup
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  ```bash

# Running the Application
   ```bash
  ## Django Development Server
  python manage.py runserver

  # Streamlit Application
  streamlit run streamlit_app/app.py

   ```bash
