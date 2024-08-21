#ESTE SOLO CREA EL EXCEL CON LAS COLUMNAS (ALEX)


from bs4 import BeautifulSoup as soup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Configure the browser with a user-agent and wait time
def configure_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"')
    browser = webdriver.Chrome(options=options)
    return browser


# Extract data from a property
def extract_property_data(page_soup):
    try:
        # Explicit wait for key elements
        title = WebDriverWait(page_soup, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h4.publication-title'))).text.strip()
        price = WebDriverWait(page_soup, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.publication-price'))).text.strip()
        # ... (extract other data using appropriate selectors)

        return [title, price, location, description, bedrooms, bathrooms]

    except Exception as e:
        print(f"Error extracting data: {e}")
        print('Título', 'Precio', 'Ubicación', 'Ubicación', 'Dormitorios', 'Baños')
        return ["N/A"] * 6  # Return list of "N/A" for missing data


# Main scraping function
def scrape_properties(url, num_pages=5):
    browser = configure_browser()
    profile = pd.DataFrame(columns=[
        'Título', 'Precio', 'Ubicación', 'Descripción', 'Dormitorios', 'Baños'
    ])

    for page in range(1, num_pages + 1):
        page_url = f"{url}&pg={page}"
        print(f"Scraping {page_url}")

        try:
            browser.get(page_url)
            # Wait some time for dynamic content to load (adjust as needed)
            time.sleep(2)

            page_soup = soup(browser.page_source, 'html.parser')

            property_cards = page_soup.find_all('div', {'class': 'publication-item'})  # Update selector if needed
            for card in property_cards:
                property_url = "https://www.toctoc.com" + card.a['href']
                browser.get(property_url)
                page_soup = soup(browser.page_source, 'html.parser')

                property_data = extract_property_data(page_soup)
                profile = profile.append(pd.Series(property_data, index=profile.columns), ignore_index=True)

        except Exception as e:
            print(f"Error scraping page {page_url}: {e}")

    browser.quit()
    return profile


# Save data to Excel file
def save_to_excel(dataframe, filename='propiedades.xlsx'):
    try:
        with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
            dataframe.to_excel(writer, index=False)
        print(f"Datos guardados en {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


# Scraping parameters
url = "https://www.toctoc.com/venta/departamento/metropolitana/santiago?o=menu_compradepto"
data = scrape_properties(url, num_pages=5)
save_to_excel(data)