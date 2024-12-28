import requests
from bs4 import BeautifulSoup

def scrape_madlan(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.madlan.co.il/for-rent/",
    "DNT": "1",  # Do Not Track header
    }

    response = requests.get(url, headers=headers)
    # print(response.text)
    # print(response.headers)

    print("Status Code:", response.status_code)
    # with open("output.html", "w", encoding="utf-8") as file:
    #     file.write(response.text)

    # if response.headers.get('Content-Encoding') == 'gzip':
    #     import gzip
    #     from io import BytesIO
    #     response_content = gzip.decompress(BytesIO(response.content).read())
    # else:
    #     response_content = response.content

    soup = BeautifulSoup(response.content, "html.parser")

    ads = []  # רשימה לשמירת המודעות

    listings = soup.find_all("div", {"data-auto": "listed-bulletin"})
    print("Listings found:", len(listings)) 

    for listing in listings:
        try:
            # image_tag = listing.find("img")
            # image_url = image_tag["src"] if image_tag else "No image found\n"
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
                # "image":image_url,
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


