import requests
from lxml import html
import csv
import os

# Link to the target site for parsing
url = "https://people.onliner.by/"

# Creating a user agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    tree = html.fromstring(response.content)
    
    # XPath to retrieve all news items
    news_items_xpath = "//div[contains(@class, 'news-tidings__item')]"
    news_items = tree.xpath(news_items_xpath)
    
    data = []
    for item in news_items:
        # XPath for the title and link within each news item
        title = item.xpath(".//div[@class='news-tidings__subtitle']/a/span/text()")
        link = item.xpath(".//div[@class='news-tidings__subtitle']/a/@href")
        
        if title and link:
            data.append((title[0].strip(), link[0]))
    
    if not data:
        raise ValueError("Failed to retrieve data. The site structure may have changed.")
    
    # Getting the path to the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Compiling the full path to the articles.csv file
    csv_file_path = os.path.join(script_dir, 'articles.csv')
    
    # Writing data to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Link']) 
        writer.writerows(data)
    
    print(f"The data has been successfully saved to a file {csv_file_path}. Retrieved {len(data)} articles.")

except requests.RequestException as e:
    print(f"Error when sending a request: {e}")
except ValueError as e:
    print(f"Error during data processing: {e}")
except Exception as e:
    print(f"There was an unexpected error: {e}")