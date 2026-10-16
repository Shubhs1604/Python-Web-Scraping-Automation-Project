from selenium import webdriver

# Create Chrome browser
driver = webdriver.Chrome()

# Open Flipkart
driver.get("https://www.flipkart.com")

print("Page opened successfully!")
print("Page title:", driver.title)
print("Current URL:", driver.current_url)

input("Press Enter to close the browser...")

# Close browser
driver.quit()