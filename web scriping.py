import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# === Static Web Scraping using BeautifulSoup === #
def scrape_static_content():
    url = 'http://books.toscrape.com/'  # Static website to scrape

    # Add headers to avoid IP blocking
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Fetch the HTML content
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting all book titles from the homepage
    books = soup.find_all('h3')

    print("Books Scraped from Static Website:")
    for book in books:
        title = book.a['title']  # 'a' tag inside 'h3' contains the title attribute
        print(title)

    print("\n" + "="*50 + "\n")

# === Dynamic Web Scraping using Selenium === #
def scrape_dynamic_content():
    # Set up the WebDriver (Chrome in this case)
    driver = webdriver.Chrome()

    # Open the dynamic website (infinite scroll example)
    url = 'http://quotes.toscrape.com/scroll'
    driver.get(url)

    # Scroll to load dynamic content
    time.sleep(2)  # Wait for the page to load
    for i in range(3):  # Adjust range for more scrolling
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(2, 4))  # Add random delay to mimic human interaction

    # Extract quotes after scrolling
    quotes = driver.find_elements(By.CLASS_NAME, 'quote')

    print("Quotes Scraped from Dynamic Website:")
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, 'text').text
        author = quote.find_element(By.CLASS_NAME, 'author').text
        print(f'"{text}" - {author}')

    # Close the WebDriver
    driver.quit()

# === Main Program === #
if __name__ == "__main__":
    # Scrape static content
    scrape_static_content()

    # Scrape dynamic content
    scrape_dynamic_content()
