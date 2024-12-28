import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

def scrape_with_selenium(url):

    print("********** scraping *************")

    """
    Scrapes listings from the given URL using undetected_chromedriver.

    Args:
        url (str): URL to scrape data from.

    Returns:
        list: List of dictionaries containing listing data.
    """
    # Initialize the undetected Chrome WebDriver
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = uc.Chrome(options=options)

    try:
        driver.get(url)  # Open the website
        wait = WebDriverWait(driver, 15)  # Wait for elements to load
        
        # Scroll to simulate human behavior and ensure all listings load
        for _ in range(5):  # Adjust scroll iterations as needed
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(random.uniform(1, 2))

        # Wait until the listings are present
        listings = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-auto="listed-bulletin"]')))

        ads = []  # List to store listings data

        for listing in listings:
            try:
                # Extract listing details
                price = listing.find_element(By.CSS_SELECTOR, '[data-auto="property-price"]').text
                rooms = listing.find_element(By.CSS_SELECTOR, '[data-auto="property-rooms"]').text
                address = listing.find_element(By.CSS_SELECTOR, '[data-auto="property-address"]').text
                link = listing.find_element(By.TAG_NAME, 'a').get_attribute('href')

                # Add the ad data to the list
                ads.append({
                    "price": price.strip(),
                    "rooms": rooms.strip(),
                    "address": address.strip(),
                    "link": link.strip()
                })

            except Exception as e:
                print("********** im in error *************")

                
                # print(f"Error parsing listing: {e}")

        return ads

    finally:
        driver.quit()  # Ensure the driver is closed properly

# # Example usage
# if __name__ == "__main__":
#     url = "https://www.madlan.co.il/for-rent/ישראל"
#     try:
#         ads = scrape_with_selenium(url)
#         print(f"Found {len(ads)} listings:")
#         for ad in ads:
#             print(ad)
#     except Exception as e:
#         print(f"Failed to scrape: {e}")
