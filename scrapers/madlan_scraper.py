import requests
from bs4 import BeautifulSoup

def scrape_madlan(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.madlan.co.il/",
    }
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    # with open("output.html", "w", encoding="utf-8") as file:
    #     file.write(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    
    ads = []  # רשימה לשמירת המודעות

    listings = soup.find_all("div", {"data-auto": "listed-bulletin"})
    print("Listings found:", len(listings)) 

    for listing in listings:
        try:
            price = listing.find("div", {"data-auto": "property-price"}).text.strip()
            rooms = listing.find("div", {"data-auto": "property-rooms"}).text.strip()
            floor = listing.find("div", {"data-auto": "property-floor"}).text.strip()
            size = listing.find("div", {"data-auto": "property-size"}).text.strip()
            address = listing.find("div", {"data-auto": "property-address"}).text.strip()
            # שליפת קישור למודעה
            link_tag = listing.find("a")
            link = "https://www.madlan.co.il" + link_tag["href"] if link_tag else None

            # שמירת המודעה למילון
            ad = {
                "price": price,
                "rooms": rooms,
                "floor": floor,
                "size": size,
                "address": address,
                "link": link
            }
            ads.append(ad)
        except AttributeError:
            continue
            

    return ads


