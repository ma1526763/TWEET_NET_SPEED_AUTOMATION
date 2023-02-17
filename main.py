from selenium_driver import Selenium_Driver
from net_speed import get_net_speed
from send_tweet import send_tweet

# get driver from Selenium Driver Class
driver = Selenium_Driver().driver
# get net speed with data object d
d = get_net_speed(driver)

# tweet net speed complaint to isp provider if speed does not match as promised.
if d.download_speed < d.promising_download_speed:
    # create tweet content
    tweet_content = f"Dear {d.internet_provider_twitter_username}, Why is my speed {d.download_speed}Down/{d.upload_speed}Up " \
                    f"(mbps) when I pay for {d.promising_download_speed}Down/{d.promising_upload_speed}Up (mbps)?\n " \
                    f"ISP PROVIDER: {d.isp_provider}\nSPONSER_LOCATION: {d.sponsor_location}\nTEST SPEED: {d.test_result_link}" \
                    f"\nPROMISED SPEED URL: {d.promised_speed_url}"
    # print(tweet_content)
    # send tweet
    send_tweet(driver, tweet_content)