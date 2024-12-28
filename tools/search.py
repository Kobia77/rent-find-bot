from scrapers.madlan_scraper_sl import scrape_with_selenium

def perform_search(location, max_price):

    special_locations = {
        "תל אביב":"תל-אביב-יפו-ישראל",
        "יפו": "תל-אביב-יפו-ישראל",
        "ישראל": "ישראל"
    }

    # הסרת רווחים מיותרים
    formatted_location = location.strip().replace(" ", "-")

    # בדיקה האם המיקום נמצא במילון המיקומים המיוחדים
    if location in special_locations:
        base_url=f"https://www.madlan.co.il/for-rent/{special_locations[formatted_location]}"
    else:
        base_url=f"https://www.madlan.co.il/for-rent/{formatted_location}-ישראל"

    print(formatted_location)
    # Construct the search URL
    
    # if formatted_location=="לארשי":
    #     base_url = "https://www.madlan.co.il/for-rent/ישראל"
    #     print("if:",base_url)
    #     # search_url = f"{base_url}-{formatted_location}"
    # elif formatted_location=="ביבא לת" or formatted_location=="יפו":
        
    #     base_url = f"https://www.madlan.co.il/for-rent/תל-אביב-יפו-ישראל"
    #     print("elif:",base_url)
    # else:
    #     base_url = f"https://www.madlan.co.il/for-rent/{formatted_location}-ישראל"
    #     print("else:",base_url)   
    print("this is base url:",base_url)

    # Scrape data
    listings = scrape_with_selenium(base_url)

    # Filter results based on max price
    filtered_listings = [
        listing for listing in listings if int(listing["price"].replace("₪", "").replace(",", "").strip()) <= max_price
    ]
    print("********** filtered listings *************")

    print(filtered_listings)
    return filtered_listings
