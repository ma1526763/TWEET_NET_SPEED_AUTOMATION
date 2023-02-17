from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Data

# create Data object d
d = Data()

def get_net_speed(driver):
    # access net speed website
    driver.get(d.net_speed_url)
    # click on the go button (start testing net speed)
    driver.find_element(By.CLASS_NAME, 'start-text').click()
    # wait until they respond required class is visible (max wait time is 120)
    WebDriverWait(driver, 120).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'js-sponsor-name')))

    # updating data class object d with required values
    d.download_speed = float(driver.find_element(By.CLASS_NAME, 'download-speed').text)
    d.upload_speed = float(driver.find_element(By.CLASS_NAME, 'upload-speed').text)
    d.isp_provider = driver.find_element(By.CLASS_NAME, 'js-data-isp').text
    d.sponsor_location = driver.find_element(By.CLASS_NAME, 'js-sponsor-name').text
    d.test_result_link = driver.current_url
    return d