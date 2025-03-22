from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in the background
driver = webdriver.Chrome(options=options)

# Open eBay search results for Pokémon cards
search_url = "https://www.ebay.com/sch/i.html?_nkw=pokemon+cards"
driver.get(search_url)

# Wait for page to load
time.sleep(5)

data = []

# Scrape multiple pages (up to 5 pages)
for page in range(1, 6):  
    print(f"📄 Scraping Page {page}...")

    # Find all product listings
    items = driver.find_elements(By.XPATH, '//li[contains(@class, "s-item")]')
    print(f"🔍 Found {len(items)} items on Page {page}.")

    for item in items:
        try:
            title_element = item.find_elements(By.XPATH, './/div[contains(@class, "s-item__title")]')
            title = title_element[0].text.strip() if title_element else ""

            price_element = item.find_elements(By.XPATH, './/span[contains(@class, "s-item__price")]')
            price = price_element[0].text.strip() if price_element else ""

            link_element = item.find_elements(By.XPATH, './/a[contains(@class, "s-item__link")]')
            link = link_element[0].get_attribute("href") if link_element else ""

            if title and price:
                print(f"✔ {title} - {price}")
                data.append([title, price, link])

        except Exception as e:
            print("❌ Error extracting item:", e)

    # Click 'Next Page' button
    try:
        next_button = driver.find_element(By.XPATH, '//a[@aria-label="Next page"]')
        next_button.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for new page to load
    except:
        print("🚫 No more pages found!")
        break

# Close browser
driver.quit()

# Save data to CSV
df = pd.DataFrame(data, columns=["Title", "Price", "Link"])
df.to_csv("ebay_pokemon_cards.csv", index=False)
print("✅ Data saved to 'ebay_pokemon_cards.csv'")
