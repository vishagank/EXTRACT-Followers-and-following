from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/guviofficial/")
driver.maximize_window()
wait = WebDriverWait(driver, 20)


# XPaths for Followers and Following
followers_xpath = "//a[contains(@href, '/followers')]/span"
following_xpath = "//a[contains(@href, '/following')]/span"

try:
    # extract the Followers count
    followers_element = wait.until(EC.visibility_of_element_located((By.XPATH, followers_xpath)))
    followers_count = followers_element.text
    print("Number of followers:", followers_count)

    #extract the Following count
    following_element = wait.until(EC.visibility_of_element_located((By.XPATH, following_xpath)))
    following_count = following_element.text
    print("Number of following:", following_count)

finally:
    driver.quit()
