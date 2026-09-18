import requests
from bs4 import BeautifulSoup

url = "https://www.indiatoday.in/"
response = requests.get(url)

# Parse HTML content and extract heading tags
soup = BeautifulSoup(response.content, "html.parser")
headings = soup.find_all(["h1", "h2", "h3"])

for heading in headings:
    print(heading.text.strip())
