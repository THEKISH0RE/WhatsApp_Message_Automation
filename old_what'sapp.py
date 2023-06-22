import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class WhatsAppBot:
    def __init__(self, excel_file_path, chrome_driver_path):
        self.df = pd.read_excel(excel_file_path, header=None, names=['Phone Number'])
        self.phone_numbers = self.df['Phone Number'].tolist()
        self.numbers = self.phone_numbers
        self.chrome_path = chrome_driver_path
        self.service = Service(self.chrome_path)

        # set up the options
        options = webdriver.ChromeOptions()

        # set the headers
        options.add_argument("authority: web.whatsapp.com")
        options.add_argument("accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")
        options.add_argument("accept-language: en-US,en;q=0.9")
        options.add_argument("cache-control: max-age=0")
        options.add_argument("cookie: wa_beta_version=production%2F1681958583%2F2.2317.10")
        options.add_argument("dnt: 1")
        options.add_argument('sec-ch-ua: "Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"')
        options.add_argument("sec-ch-ua-mobile: ?0")
        options.add_argument('sec-ch-ua-platform: "Windows"')
        options.add_argument("sec-fetch-dest: document")
        options.add_argument("sec-fetch-mode: navigate")
        options.add_argument("sec-fetch-site: same-origin")
        options.add_argument("sec-fetch-user: ?1")
        options.add_argument("upgrade-insecure-requests: 1")
        options.add_argument("user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
        options.add_argument("--compressed")

        self.driver = webdriver.Chrome(service=self.service, options=options)
        self.driver.get('https://web.whatsapp.com/')
        self.message = "This is automated message for testing"

    def send_messages(self):
        input('Press Enter once you have logged in to WhatsApp web and scanned the QR code...')
        for number in self.numbers:
            url = f'https://web.whatsapp.com/send?phone=' + f'{number}' + '&text=' + self.message
            self.driver.get(url)
            time.sleep(random.randint(10,20))
            send_wait = WebDriverWait(self.driver, 500)
            input_send = send_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')))
            input_send.click()
            time.sleep(random.randint(0,5))

    def close_browser(self):
        self.driver.quit()

bot = WhatsAppBot('C:\\Users\\ELCOT\\Desktop\\phone number.xlsx', 'C:\\Users\\ELCOT\\Desktop\\what\'s_app_auto\\chromedriver_win32\\chromedriver')
bot.send_messages()
bot.close_browser()
