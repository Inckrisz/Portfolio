from bs4 import BeautifulSoup
import requests
from django.core.management.base import BaseCommand
from headlines.models import Headline, Category

class Command(BaseCommand):


      


    def handle(self, *args, **kwargs):
        url = 'https://news.ycombinator.com/'  # Replace with the correct URL you want to scrape
        response = requests.get(url)

        if response.status_code == 200:
            print("SUCCESS")
            soup = BeautifulSoup(response.text, 'html.parser')

            tech_category, _ = Category.objects.get_or_create(name='Technology')
            sport_category, _ = Category.objects.delete('Sport')
            entertainment_category, _ = Category.objects.delete('Entertainment')
            science_category, _ = Category.objects.delete('Science')
            economy_category, _ = Category.objects.delete('Economy')

            # Find all 'span' tags with the class 'titleline'
            title_lines = soup.find_all('span', class_='titleline')

            print(f"Found {len(title_lines)} title lines")  # Debugging line
            for title_line in title_lines:
                # Extract the <a> tag inside the <span class='titleline'>
                link_tag = title_line.find('a')
                if link_tag:
                    title = link_tag.get_text(strip=True)  # Get the title text
                    link = link_tag.get('href')  # Get the href attribute

                    # Ensure link is not empty
                    if link:
                        print(f"Title: {title}, Link: {link}")  # Debugging line
                        # Save the headline and link to the database
                        Headline.objects.get_or_create(
                            title=title,
                            link=link,
                            category=tech_category
                        )
                    else:
                        print("No link found for this item.")  # Debugging line
                else:
                    print("No <a> tag found in this title line.")  # Debugging line

            self.stdout.write(self.style.SUCCESS('Successfully scraped and saved news headlines'))
        else:
            print(f"NOT SUCCESS, Status Code: {response.status_code}")

    
