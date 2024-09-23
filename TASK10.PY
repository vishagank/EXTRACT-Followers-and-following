from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/guviofficial/")
driver.maximize_window()
wait = WebDriverWait(driver, 20)

username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("Vishal")

# Enter password
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("*****")

# login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

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
