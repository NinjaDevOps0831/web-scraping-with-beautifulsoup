from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


BASE_URL = "https://www.goodreads.com"


# Making Page URLs
page_urls = []

for i in range(1, 101):
  page_urls.append(BASE_URL + "/list/tag/romance?page=" + str(i))
  print("Page URL Appended: " + BASE_URL+"/list/tag/romance?page=" + str(i))


# Making Category URLs
category_urls = []

for page_url in page_urls:
  page = urlopen(page_url)
  html_bytes = page.read()
  html = html_bytes.decode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  links = soup.find_all("a", { "class" : "listTitle"})

  for link in links:
    category_urls.append(BASE_URL + link["href"])
    print("Category URL Appended: " + BASE_URL + link["href"])


# Save Book Data by Category URL
books = []

for category_url in category_urls
  page = urlopen(category_url)
  html_bytes = page.read()
  html = html_bytes.decode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  els = soup.find_all("tr")

  for el in els:
    book = {
      "title": el.find("a", { "class" : "bookTitle" }).get_text(),
      "url": BASE_URL + el.find("a", { "class" : "bookTitle" })["href"],
      "auth": {
        "name": el.find("a", { "class" : "authorName" }).get_text(),
        "url": el.find("a", { "class" : "authorName" })["href"]
      },
      "rating": el.find("span", { "class" : "minirating" }).get_text()
    }

    books.append(book)
    print("Book Appended: " book.title)


# Save Data to Json
with open ("data.json", "w") as fp:
  json.dump(books, fp)