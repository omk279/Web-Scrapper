from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import mysql.connector
import re

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="croma_scraper"
)
cursor = conn.cursor()

driver = webdriver.Chrome()
driver.get("https://www.croma.com/televisions-accessories/led-tvs/c/392")

wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

for _ in range(6):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

cards = driver.find_elements(By.XPATH, "//a[contains(@href,'/p/')]")
print("CARDS FOUND:", len(cards))

rank = 1

for card in cards:
    try:
        product_url = card.get_attribute("href")
        name = card.text.strip()
        if not product_url or len(name) < 5:
            continue
    except:
        continue

    brand = name.split(" ")[0]

    container_text = card.find_element(By.XPATH, "./ancestor::div").text

    prices = re.findall(r"₹\s*([\d,]+)", container_text)
    price = max([int(p.replace(",", "")) for p in prices]) if prices else None

    rating_match = re.search(r"([\d.]+)\s*★", container_text)
    rating = float(rating_match.group(1)) if rating_match else None

    size_match = re.search(r"(\d{2})\s*inch", name)
    screen_size = int(size_match.group(1)) if size_match else None

    discount_match = re.search(r"(\d+)%\s*off", container_text.lower())
    discount = int(discount_match.group(1)) if discount_match else None

    try:
        image = card.find_element(By.XPATH, ".//img").get_attribute("src")
    except:
        image = None

    cursor.execute("""
        INSERT INTO tvs 
        (product_name, brand, price, rating, screen_size, discount, catalog_rank, image_url, product_url)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
        price=VALUES(price),
        rating=VALUES(rating),
        discount=VALUES(discount),
        catalog_rank=VALUES(catalog_rank),
        updated_at=CURRENT_TIMESTAMP
    """, (
        name, brand, price, rating, screen_size, discount, rank, image, product_url
    ))

    conn.commit()
    rank += 1

driver.quit()
cursor.close()
conn.close()

print("DONE")
