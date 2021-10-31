from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def findClass(email, password):
    option = webdriver.ChromeOptions()
    # # For older ChromeDriver under version 79.0.3945.16
    # option.add_experimental_option("excludeSwitches", ["enable-automation"])
    # option.add_experimental_option('useAutomationExtension', False)
    # # For ChromeDriver version 79.0.3945.16 or over
    # option.add_argument('--disable-blink-features=AutomationControlled')
    # option.add_argument('headless')

    # print("input email")
    # email = input()
    # print("input password")
    # password = input()

    # driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=option)
    driver = webdriver.Chrome(ChromeDriverManager(
        chrome_type=ChromeType.GOOGLE).install())

    driver.get("https://student.myillini.illinois.edu")

    window_before = driver.window_handles[0]

    outlook_email = driver.find_element_by_xpath(
        "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]")
    outlook_email.send_keys(email)
    next = driver.find_element_by_xpath(
        "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input")
    next.click()
    time.sleep(3)

    password_input = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[2]/input")

    password_input.send_keys(password)
    sign_in = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[4]/span")
    sign_in.click()
    time.sleep(3)

    courseblocks = driver.find_elements_by_xpath("//div[@class='course block']")
    list = []
    for course in courseblocks:
        currentlist = course.text.splitlines()
        if len(currentlist) < 4:
            break
        else:
            list.append(currentlist)
    for item in list:
        item[2] = item[2][12:]
        if len(item[3]) < 4:
            item.insert(3,item[3])
            item[4] = "No Time Information Available"
        else:
            date_and_time = max(item[3].find(" M"),item[3].find(" TU"),item[3].find(" W"),item[3].find(" TH"),item[3].find(" F"))
            location = item[3][0:date_and_time].strip()
            item.insert(3, location)
            item[4] = item[4][date_and_time:].strip()
        print(item)

    list.insert(0,['Name', 'Number', 'Instructor', 'Location', 'Time', "Final Exam"])
    return list
def findClasss():
    print("HI")
    return [1,2,3,4]