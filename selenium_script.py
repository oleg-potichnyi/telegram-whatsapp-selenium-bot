from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
import time
import os


def run_selenium() -> list[str]:
    chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe")

    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get("https://quotes.toscrape.com/login")
        time.sleep(2)
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("admin")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        time.sleep(2)

        driver.get("https://quotes.toscrape.com/")
        time.sleep(2)

        quotes_elements = driver.find_elements(By.CLASS_NAME, "quote")
        quotes = []
        for q in quotes_elements:
            text = q.find_element(By.CLASS_NAME, "text").text
            author = q.find_element(By.CLASS_NAME, "author").text
            quotes.append(f"{text} — {author}")

        selected_quotes = random.sample(quotes, 3)

        return selected_quotes

    finally:
        driver.quit()
