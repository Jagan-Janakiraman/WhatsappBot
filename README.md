#WhatsApp Bot
This is a Python script that automates sending messages on WhatsApp using Selenium and Chrome WebDriver. It allows you to send messages to multiple recipients by providing their names in a list.

Prerequisites
    Python 3.x
    Selenium library (pip install selenium)
    Chrome WebDriver

Getting Started
    Clone the repository or download the script to your local machine.

    Install the required dependencies by running the following command:
    """
    pip install selenium
    """
    Download the Chrome WebDriver compatible with your Chrome browser version and place it in the same directory as the script. You can download the Chrome WebDriver from here.

    Open the script file and update the name_list variable with the names of the recipients you want to send messages to.

    Run the script using the following command:
    simply run the file

    1) Scan the QR code displayed in the browser to log in to your WhatsApp account.

    2) The script will wait for 20 seconds for the WhatsApp web page to load. After that, it will start sending messages to the recipients in the name_list.

    Customization
    1) You can modify the message content by updating the text in the box_message.send_keys() line.

    2) If you want to send messages to additional recipients, add their names to the name_list variable.

    3) Adjust the delay time (in seconds) using the time.sleep() function according to your needs.

    Notes
        Make sure you have a stable internet connection and keep the script running until it finishes sending all the messages.

        This script uses Selenium and Chrome WebDriver to automate the process. It emulates human behavior but may not work if the structure of the WhatsApp web page changes.

        Use this script responsibly and in accordance with WhatsApp's terms of service.

        Feel free to customize and enhance the script to fit your specific requirements.