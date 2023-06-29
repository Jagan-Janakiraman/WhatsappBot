import time
from selenium import webdriver

# Function to send a message to a user in WhatsApp
def open_chat(recipient_name):
    user_chat = browser.find_element_by_xpath('//div[@class="_3u328 copyable-text-selectable-text')
    user_chat.send_keys(recipient_name)

# Set up the Chrome WebDriver
my_options = webdriver.ChromeOptions()
browser = webdriver.Chrome('chromedriver.exe', options=my_options)

# Open WhatsApp Web
browser.get('https://web.whatsapp.com')
time.sleep(20)

# List of names to send messages to
name_list = ['Appa']

# Iterate over each name in the list
for recipient_name in name_list:
    try:
        # Find the user in the chat list and click on it
        user = browser.find_element_by_xpath('//span[@title="{}"]'.format(recipient_name))
        user.click()

        # Enter the message in the input box
        box_message = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        box_message.send_keys("Hi jagan Here ... using the WhatsApp bot")

        # Click the send button
        box_message = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        box_message.click()
        
    except Exception as e:
        print(e)
