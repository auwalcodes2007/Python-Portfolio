import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all(name="article", class_="product_pod")

    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author"])
        for book in books:
            title = book.h3.a["title"]
            writer.writerow([title, "N/A"])
    print("Scraping complete, check books.csv")
except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")
