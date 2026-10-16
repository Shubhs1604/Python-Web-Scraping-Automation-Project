from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


# ==================================================
# 1. START CHROME
# ==================================================

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com")

print("Website opened")
print("Title:", driver.title)

time.sleep(3)


# ==================================================
# 2. FIND SEARCH BOX
# ==================================================

search_box = driver.find_element(By.NAME, "q")

print("Search box found!")


# ==================================================
# 3. SEARCH FOR LAPTOP
# ==================================================

search_box.send_keys("laptop")

print("Laptop entered")

search_box.send_keys(Keys.ENTER)

print("Enter pressed")

time.sleep(5)


# ==================================================
# 4. CHECK SEARCH PAGE
# ==================================================

print("Current URL:", driver.current_url)
print("Current title:", driver.title)


# ==================================================
# 5. FIND PRODUCTS
# ==================================================

products = driver.find_elements(
    By.CSS_SELECTOR,
    "div[data-id]"
)


# Remove Flipkart sticky element
products = [
    product
    for product in products
    if product.get_attribute("data-id") != "stickyElement"
]


print("Products found:", len(products))


# ==================================================
# 6. CREATE EMPTY LIST
# ==================================================

laptops = []


# ==================================================
# 7. SCRAPE EVERY PRODUCT
# ==================================================

for i, product in enumerate(products, start=1):

    print("\n========================================")
    print("PRODUCT NUMBER:", i)
    print("========================================")


    # ----------------------------------------------
    # PRODUCT ID
    # ----------------------------------------------

    product_id = product.get_attribute("data-id")

    print("Product ID:", product_id)


    # ----------------------------------------------
    # PRODUCT NAME
    # ----------------------------------------------

    name_elements = product.find_elements(
        By.CSS_SELECTOR,
        ".RG5Slk"
    )

    if name_elements:
        product_name = name_elements[0].text.strip()
    else:
        product_name = None

    print("Product Name:", product_name)


    # ----------------------------------------------
    # SELLING PRICE
    # ----------------------------------------------

    price_elements = product.find_elements(
        By.CSS_SELECTOR,
        ".hZ3P6w"
    )

    if price_elements:
        price = price_elements[0].text.strip()
    else:
        price = None

    print("Price:", price)


    # ----------------------------------------------
    # ORIGINAL PRICE
    # ----------------------------------------------

    original_price_elements = product.find_elements(
        By.CSS_SELECTOR,
        ".kRYCnD"
    )

    if original_price_elements:
        original_price = original_price_elements[0].text.strip()
    else:
        original_price = None

    print("Original Price:", original_price)


    # ----------------------------------------------
    # DISCOUNT
    # ----------------------------------------------

    discount_elements = product.find_elements(
        By.CSS_SELECTOR,
        ".HQe8jr"
    )

    if discount_elements:
        discount = discount_elements[0].text.strip()
    else:
        discount = None

    print("Discount:", discount)


    # ----------------------------------------------
    # RATING
    # ----------------------------------------------

    rating_elements = product.find_elements(
        By.CSS_SELECTOR,
        ".MKiFS6"
    )

    if rating_elements:
        rating = rating_elements[0].text.strip()
    else:
        rating = None

    print("Rating:", rating)


    # ----------------------------------------------
    # RATINGS AND REVIEWS
    # ----------------------------------------------

    review_elements = product.find_elements(
        By.CSS_SELECTOR,
        ".PvbNMB"
    )

    if review_elements:
        ratings_reviews = review_elements[0].text.strip()
    else:
        ratings_reviews = None

    print("Ratings & Reviews:", ratings_reviews)


    # ----------------------------------------------
    # FEATURES
    # ----------------------------------------------

    feature_elements = product.find_elements(
        By.CSS_SELECTOR,
        ".DTBslk"
    )

    features = []

    for feature in feature_elements:
        features.append(feature.text.strip())


    # ----------------------------------------------
    # CREATE EMPTY FEATURE VARIABLES
    # ----------------------------------------------

    processor = None
    ram = None
    operating_system = None
    storage = None
    display = None


    # ----------------------------------------------
    # IDENTIFY FEATURES
    # ----------------------------------------------

    for feature in features:

        if "Processor" in feature:
            processor = feature

        elif "RAM" in feature:
            ram = feature

        elif "Operating System" in feature:
            operating_system = feature

        elif "SSD" in feature or "HDD" in feature:
            storage = feature

        elif "Display" in feature:
            display = feature


    print("Processor:", processor)
    print("RAM:", ram)
    print("Operating System:", operating_system)
    print("Storage:", storage)
    print("Display:", display)


    # ----------------------------------------------
    # PRODUCT URL
    # ----------------------------------------------

    url_elements = product.find_elements(
        By.CSS_SELECTOR,
        "a.k7wcnx"
    )

    if url_elements:
        product_url = url_elements[0].get_attribute("href")
    else:
        product_url = None

    print("Product URL:", product_url)


    # ----------------------------------------------
    # CREATE DICTIONARY
    # ----------------------------------------------

    laptop = {
        "product_id": product_id,
        "product_name": product_name,
        "price": price,
        "original_price": original_price,
        "discount": discount,
        "rating": rating,
        "ratings_reviews": ratings_reviews,
        "processor": processor,
        "ram": ram,
        "operating_system": operating_system,
        "storage": storage,
        "display": display,
        "product_url": product_url
    }


    # ----------------------------------------------
    # ADD DICTIONARY TO LIST
    # ----------------------------------------------

    laptops.append(laptop)


# ==================================================
# 8. SCRAPING COMPLETED
# ==================================================

print("\n========================================")
print("SCRAPING COMPLETED")
print("========================================")

print("Total laptops collected:", len(laptops))


## ==================================================
# 9. CREATE PANDAS DATAFRAME
# ==================================================

df = pd.DataFrame(laptops)


# ==================================================
# 10. CLEAN PRICE
# ==================================================

df["price"] = (
    df["price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)


# ==================================================
# 11. CLEAN ORIGINAL PRICE
# ==================================================

df["original_price"] = (
    df["original_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["original_price"] = pd.to_numeric(
    df["original_price"],
    errors="coerce"
)


# ==================================================
# 12. CLEAN DISCOUNT
# ==================================================

df["discount"] = (
    df["discount"]
    .str.replace("% off", "", regex=False)
)

df["discount"] = pd.to_numeric(
    df["discount"],
    errors="coerce"
)


# ==================================================
# 13. CLEAN RATING
# ==================================================

df["rating"] = pd.to_numeric(
    df["rating"],
    errors="coerce"
)


# ==================================================
# 14. DISPLAY CLEANED DATA
# ==================================================

print("\n========================================")
print("CLEANED DATA")
print("========================================")

print(
    df[
        [
            "product_name",
            "price",
            "original_price",
            "discount",
            "rating"
        ]
    ].head(10)
)


# ==================================================
# 15. DISPLAY DATA TYPES
# ==================================================

print("\n========================================")
print("DATA TYPES")
print("========================================")

print(df.dtypes)


# ==================================================
# 16. SAVE DATA TO CSV
# ==================================================

file_name = "flipkart_laptops.csv"

df.to_csv(
    file_name,
    index=False
)

print("\n========================================")
print("CSV FILE CREATED")
print("========================================")

print("File:", file_name)
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("File Name:", file_name)


# ==================================================
# 17. KEEP BROWSER OPEN
# ==================================================

input("\nPress Enter to close browser...")


# ==================================================
# 18. CLOSE BROWSER
# ==================================================

driver.quit()

print("Browser closed")