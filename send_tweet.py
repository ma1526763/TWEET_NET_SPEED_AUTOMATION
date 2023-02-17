from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
import random
import time

# Create Data object d
data = Data()

# log out from twitter after 20 seconds
def logout_twitter(driver):
    time.sleep(20)

    # click on username to logout
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div/div[2]').click()
    time.sleep(random.choice([2, 3]))
    # click logout
    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div[1]/div/span').click()
    time.sleep(random.choice([3, 4]))
    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span').click()

# twitter login with credentials
def login_twitter(driver):
    # access twitter url
    driver.get(data.twitter_url)
    # wait until login button is available
    WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Log in')))
    # click login
    driver.find_element(By.LINK_TEXT, 'Log in').click()
    WebDriverWait(driver, 40).until(expected_conditions.presence_of_element_located((By.NAME, 'text')))
    # add username/phone number/email
    driver.find_element(By.NAME, 'text').send_keys(data.twitter_login_number + Keys.ENTER)
    WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
    # add your password
    password_entry = driver.find_element(By.NAME, 'password')
    password_entry.send_keys(data.twitter_login_password)
    time.sleep(random.choice([2, 4, 5, 6]))
    # click login
    password_entry.send_keys(Keys.ENTER)

def send_tweet(driver, tweet):
    # login with credentials
    login_twitter(driver)
    # wait until website is load after login
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'public-DraftStyleDefault-block')))
    # click on Twitter box
    type_message = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
    type_message.click()
    # start typing tweet
    for word in tweet.split():
        type_message.send_keys(word + " ")
        time.sleep(random.choice([0.1, 0.2]))
    time.sleep(5)
    # once you're done click Tweet to make a tweet
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
    # logout Twitter
    logout_twitter(driver)
