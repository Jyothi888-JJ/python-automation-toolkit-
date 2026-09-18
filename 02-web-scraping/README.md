# Web Scraping News & Blog Headings

This project demonstrates a simple **Python web scraping script** that fetches a webpage and extracts its main **H1, H2, and H3 headings**.

## What This Script Does

1. Sends a request to a website using Python `requests`.
2. Fetches the webpage HTML content.
3. Uses **BeautifulSoup** to parse the HTML.
4. Extracts `h1`, `h2`, and `h3` heading tags.
5. Prints the headings to the terminal.

## Technologies Used

* Python
* Requests
* BeautifulSoup
* HTML

## How It Works

```text
Python Script
     ↓
Send Request to Website
     ↓
Fetch HTML Content
     ↓
BeautifulSoup Parses HTML
     ↓
Find H1, H2, H3 Headings
     ↓
Print Headings
```

## Setup

### 1. Install the required libraries

```bash
pip install requests beautifulsoup4
```

### 2. Run the script

```bash
python news_headings.py
```

## Example Output

```text
India Today News
Latest News
India News
World News
Technology News
Sports News
```

The exact headings will change depending on the current content of the website.

## Purpose

This project demonstrates basic **Python automation and web scraping**, including making HTTP requests, parsing HTML, and extracting useful information from webpages.
