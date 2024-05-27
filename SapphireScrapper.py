from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

# Open the main page
base_url = 'https://pk.sapphireonline.pk/'
driver.get('https://pk.sapphireonline.pk/collections/unstitched-eid-2-24')

# Scroll down until all items are loaded
def scroll(driver, timeout):
    scroll_pause_time = timeout
    last_height = driver.execute_script("return document.body.scrollHeight")
    i = 0
    while i < 3:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        i += 1

# Call the scroll function
scroll(driver, 5)  # Adjust the timeout as needed

# Extract product links
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.prettify())

img_links = [img['src'] for img in soup.find_all('img', class_='t4s-product-main-img')]
# print(img_links)
# product_links = [a['href'] for a in soup.find_all('a', class_='grid-view-item__link')]
# print(product_links)
filtered_links = list(filter(lambda x: "base64" not in x, img_links))
print(filtered_links)

# # Now visit each product page and extract image paths, title, and price
# for link in product_links:
#     driver.get(base_url + link)
#     # Extract details using Beautiful Soup
#     product_soup = BeautifulSoup(driver.page_source, 'html.parser')
#     # Find the image tag
#     img_tag = product_soup.find('img', alt='slider-img')
    
#     if img_tag:
#         image_url = img_tag['src']
#         print(f"Image URL: {base_url + image_url}")
#     else:
#         print("Image not found on this page.")
#     time.sleep(5)

# # Close the browser
# driver.quit()
