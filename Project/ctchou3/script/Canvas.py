from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
# # For older ChromeDriver under version 79.0.3945.16
# option.add_experimental_option("excludeSwitches", ["enable-automation"])
# option.add_experimental_option('useAutomationExtension', False)
# # For ChromeDriver version 79.0.3945.16 or over
# option.add_argument('--disable-blink-features=AutomationControlled')
# option.add_argument('headless')

print("input email")
email = input()
print("input password")
password = input()

# driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=option)
driver = webdriver.Chrome(ChromeDriverManager(
    chrome_type=ChromeType.GOOGLE).install())

driver.get("https://canvas.illinois.edu/")


outlook_email = driver.find_element_by_xpath(
    "/html/body/main/form/div[1]/input")
outlook_email.send_keys(email)
time.sleep(3)

password_input = driver.find_element_by_xpath(
    "/html/body/main/form/div[2]/input")

password_input.send_keys(password)
sign_in = driver.find_element_by_xpath(
    "/html/body/main/form/div[3]/input")
sign_in.click()
time.sleep(3)

canvas_divs = driver.find_elements_by_xpath("//div[@class='Day-styles__root planner-day']")
for div in canvas_divs:
    print(div.text)