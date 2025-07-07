from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from playwright.sync_api import sync_playwright

load_dotenv()
CDP_URL = os.getenv("SBR_WEBDRIVER")

def scrape_website(website):
    print("Connecting to Bright Data Scraping Browser...")
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(CDP_URL)
        context = browser.contexts[0]
        page = context.new_page()
        print("Navigating to:", website)
        page.goto(website, timeout=60000)
        html = page.content()
        browser.close()
        return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    return "\n".join(
        line.strip() for line in soup.get_text(separator="\n").splitlines() if line.strip()
    )

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
