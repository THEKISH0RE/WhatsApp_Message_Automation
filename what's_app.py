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
        self.driver = webdriver.Chrome(service=self.service)
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
'https://explore.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes'

bot = WhatsAppBot('C:\\Users\\ELCOT\\Desktop\\phone number.xlsx', 'C:\\Users\\ELCOT\\Desktop\\what\'s_app_auto\\chromedriver_win32\\chromedriver')
bot.send_messages()
bot.close_browser()
