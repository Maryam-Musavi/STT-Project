"""
Web Scraping Basics - Step 1: Learning BeautifulSoap
خواندن متن و نوسینده از یک وبسایت مشخص
"""

import requests
from bs4 import BeautifulSoup


def fetch_html(url: str) -> str:
    """
    دریافت کدهای خام از صفحه اینترنت
    """
    # 1. Send Request
    response = requests.get(url, timeout=10)

    # 2. Return text if successful
    if response.status_code == 200:
        return response.text
    return ""

def extract_quotes_data(html: str) -> str:
    """
    پیدا کردن و جدا کردن متن ها و نام نویسنده ها با BeautifulSoap
    """

    # 1. ایجاد آبجکت پردازشگر HTML
    soup = BeautifulSoup(html, "html.parser")

    # 2. پیدا کردن تمام جعبه های نقل قول
    quote_boxes = soup.find_all("div", class_="quote")

    extract_items = []

    # 3. استخراج اطلاعات از درون هر جعبه
    for box in quote_boxes:
        # پیدا کردن تگ متنی نقل قول
        text_elemnt = box.find("span", class_="text")
        # پیدا کردن تگ نام نویسنده
        author_element = box.find("Small", class_="author")

        quote_text = text_elemnt.text.strip() if text_elemnt else "بدون متن"
        author_name = author_element.text.strip() if author_element else "ناشناس"

        extracted_items.append({
            "quote": quote_text,
            "author": author_name
        })

    return extracted_items

def main():
    print("=" * 55)
    print("مینی پروژه کاپ کیک: استخراج داده های وبلاگ با پایتون")
    print("=" * 55)

    target_url = "http://quotes.toscrape.com"

    print("⏳ در حال خواندن صفحه...")
    raw_html = fetch_html(target_url)


    if not raw_html:
        print("صفحه دانلود نشد! ارتباط اینترنت را بررسی کنید❌")
        return

#پردازش استخراج
quotes_list = extract_quotes_data(raw_html)

# نمایش 3 مورد اول برای بررسی
print(f" تعداد")



