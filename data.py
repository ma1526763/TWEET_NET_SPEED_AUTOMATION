import os
class Data:
    def __init__(self):
        self.net_speed_url = "https://www.speedtest.net/"
        self.twitter_url = 'https://twitter.com/'
        self.promising_download_speed = 150
        self.promising_upload_speed = 50
        self.promised_speed_url = "https://www.zong.com.pk/devices/zong-4g-wifi-mf25#:~:text=With%20speeds%20of%20up%20to%20150%20MB%20on%20the%20go"
        self.internet_provider_twitter_username = '@Zongers'
        self.twitter_login_number = os.environ['PHONE_NUMBER']
        self.twitter_login_password = os.environ['PASSWORD']
        self.test_result_link = ""
        self.download_speed = 0
        self.upload_speed = 0
        self.isp_provider = ""
        self.sponsor_location = ""
