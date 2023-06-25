import sys
import time
from selenium import webdriver


def user_chat(recipient_name):
    chat_new = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    chat_new.click()
    user_chat = browser.find_element_by_xpath('//div[@class="_3u328 copyable-text-selectable-text')
    user_chat.send_keys(recipient_name)
    time.sleep(2)
    try:
        user = browser.find_element_by_xpath('//span[@title="{}"]', format(recipient_name))
        user.click()
    except Exception as e:
        print(f"User {recipient_name} is not in the contacts")


if __name__ == '__main__':
    my_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome('chromedriver.exe', options=my_options)
    browser.get('https://web.whatsapp.com')
    time.sleep(20)
    
    recipient_list = ['Sathish', 'Appa']
    for recipient_name in recipient_list:
        try:
            user_chat(recipient_name)
            
            send_message = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            send_message.send_keys("Hi jagan Here ... This is an automated message Python Selenium")
            time.sleep(10)
            
            send_message = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
            send_message.click()
        except Exception as e:
            print(e)
