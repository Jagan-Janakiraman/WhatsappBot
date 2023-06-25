import time
from selenium import webdriver

# Fn to send a message to user
def user_chat(name_user):
    # change the xpath by coping the xpath form inspect tab of that compotent if its not working
    user_chat = browser.find_element_by_xpath('//div[@class="_3u328 copyable-text-selectable-text')
    user_chat.send_keys(name_user)

# Seting up the Chrome WebDriver
my_options = webdriver.ChromeOptions()
browser = webdriver.Chrome('chromedriver.exe', options=my_options)

# Opening WhatsApp Web in chrome browser
browser.get('https://web.whatsapp.com')
time.sleep(20)

# List of names to send messages to
name_list = ['Appa']

# Iterate over each name in the list
for name_user in name_list:
    try:
        # Find the user in the chat list and click on it
        user = browser.find_element_by_xpath('//span[@title="{}"]'.format(name_user))
        user.click()

        # Enter the message in the input box
        # change the xpath by coping the xpath form inspect tab of that compotent if its not working
        box_message = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        box_message.send_keys("Hi jagan Here ... using the WhatsApp bot")
        time.sleep(10)

        # Click the send button
        # change the xpath by coping the xpath form inspect tab of that compotent if its not working
        box_message = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        box_message.click()
        time.sleep(20)

    except Exception as e:
        print(e)
# closing the browser
browser.close()
