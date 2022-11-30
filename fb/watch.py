from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--disable-notification")

chrome_option.add_argument("--disable-infobars")

chrome_option.add_argument("start-maximized")

chrome_option.add_argument("--disable-extensions")

chrome_option.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 2})

chrome_option.add_argument("use-fake-ui-for-media-stream")

path = R'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path,chrome_options=chrome_option)
driver.implicitly_wait(30)

driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element_by_name("email").send_keys("9019823361")
driver.find_element_by_id("pass").send_keys("j@b12345")
time.sleep(2)
driver.find_element_by_name("login").click()
time.sleep(3)