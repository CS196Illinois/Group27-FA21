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

driver.get("https://learn.illinois.edu/")

window_before = driver.window_handles[0]
id_login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/section[2]/aside/section[1]/div/div/div[1]/a[1]")
id_login.click()
uiuc = driver.find_element_by_xpath("/html/body/div/main/div/form/fieldset/div/p[3]/input")
uiuc.click()
select = driver.find_element_by_xpath("/html/body/div/main/div/form/input[1]")
select.click()


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

deadline = driver.find_element_by_xpath("/html/body/div[2]/div[4]/section/aside/section[1]/div/div/div[1]/div[1]/div/div[1]/div/button")
deadline.click()
six_month = driver.find_element_by_xpath("/html/body/div[2]/div[4]/section/aside/section[1]/div/div/div[1]/div[1]/div/div[1]/div/div/a[6]")
six_month.click()
show = driver.find_element_by_xpath("/html/body/div[2]/div[4]/section/aside/section[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/button")
show.click()
max_show = driver.find_element_by_xpath("/html/body/div[2]/div[4]/section/aside/section[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/a[3]")
max_show.click()
assignments = driver.find_element_by_xpath("//div[@class='border-bottom pb-2']")
print(assignments.text)