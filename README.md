# Rent Find Bot - by Kobi

## Overview
A Telegram bot that helps users find rental properties by scraping listings from Madlan.

## Project Structure

    Directory structure:
    └── kobia77-rent-find-bot.git/
        ├── bot.py
        ├── chromedriver/
        │   ├── LICENSE.chromedriver
        │   └── THIRD_PARTY_NOTICES.chromedriver
        ├── scrapers/
        │   ├── __init__.py
        │   ├── madlan_scraper.py
        │   ├── madlan_scraper_sl.py
        │   └── __pycache__/
        └── tools/
            ├── __init__.py
            ├── pagination.py
            ├── search.py
            ├── start.py
            └── __pycache__/


- **bot.py**: The main entry point for the Telegram bot, handling command and message interactions.
- **chromedriver/**: Contains the ChromeDriver and related licensing files required for Selenium-based web scraping.
- **scrapers/**: Includes modules for scraping rental listings from Madlan using both requests/BeautifulSoup and Selenium.
  - **madlan_scraper.py**: Scrapes rental data using requests and BeautifulSoup.
  - **madlan_scraper_sl.py**: Uses Selenium (with undetected_chromedriver) to scrape rental listings.
- **tools/**: Contains utility modules to support pagination, search logic, and bot start-up functions.
  - **pagination.py**: Manages pagination of search results and user interactions.
  - **search.py**: Implements search functionality by scraping and filtering rental listings.
  - **start.py**: Defines the start command that initializes the bot conversation.

## Features
- **Telegram Bot Integration:** Interacts with users via Telegram to gather rental search criteria.
- **Web Scraping:** Extracts rental listing data from the Madlan website using both traditional HTTP requests and Selenium.
- **Search & Filtering:** Searches for rental properties based on user-specified location and maximum price.
- **Pagination:** Provides listings in paginated form for easy user navigation.
- **User-Friendly Interface:** Guides users through the rental search process with clear prompts.

## Installation
1. **Clone the Repository**
2. **Install Required Packages**
    - python-telegram-bot
    - python-dotenv
    - requests
    - beautifulsoup4
    - undetected-chromedriver
    - selenium

## Usage
1. **Set Up Environment Variables:**
    Create a .env file in the project root with your Telegram bot token:
    ```  BOT_TOKEN=your_telegram_bot_token```
   
3. **Run the Bot:**
```  python bot.py```

    The bot will start and listen for incoming messages on Telegram. Use the /start command to begin your rental search.

   

