# import time
# from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
#
# c_path = R'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe'
# c_driver = webdriver.Chrome(executable_path=c_path)
# c_driver.implicitly_wait(10)
# a_obj = ActionChains
#
#
# file_path = r'https://www.facebook.com/'
# c_driver.get(file_path)
# c_driver.maximize_window()
#
# username = c_driver.find_element("xpath",'//input[@id="email"]')
# username.click()
# username.send_keys(9019823361)
#
# password = c_driver.find_element("xpath","//input[@id='pass']")
# password.click()
# password.send_keys("j@b12345")
# time.sleep(3)
# c_driver.find_element("xpath","//button[text()='Log in']").click()  #(logiN)
# time.sleep(3)

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
driver.find_element("xpath",'//a[@href="https://www.facebook.com/watch/"]').click()  #(watch)
time.sleep(8)
driver.find_element("xpath","//div[@aria-label='Edit notification settings']").click()  #(setting)
time.sleep(5)
driver.find_element("xpath", "(//input[@aria-label='Show notification dots'])[1]").click() #(noti start)
time.sleep(5)
driver.find_element("xpath", "(//span[normalize-space()='Custom notifications'])[1]").click() #(custom noti)
time.sleep(5)
driver.find_element("xpath","(//input[@aria-label='Opted out all badge types'])[1]").click() #(allow video noti)
time.sleep(4)
driver.find_element("xpath",'(//i[@class="x1b0d499 xep6ejk"])[14]').click() #(new video noti)
time.sleep(5)

driver.find_element("xpath","//span[text()='Manage pages you follow']").click() #(manage page)
time.sleep(5)

obj = ActionChains(driver)
cross = driver.find_element("xpath","(//div[@aria-label='Close' and @role='button'])[2]")  #(cross button)
obj.click(cross).perform()
time.sleep(3)


#c_driver.find_element("xpath","(//input[@placeholder='Search videos'])[1]").click() #(search bar)
#c_driver.find_element("xpath","(//input[@placeholder='Search videos'])[1]").send_keys('cat funny video')


driver.find_element("xpath", "(//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft'][normalize-space()='Live'])[1]").click()  #(live)
time.sleep(3)
driver.find_element("xpath", '(//span[text()="Shows"])[1]').click()  #(show)
# driver.find_element("xpath",'(//div[@role="presentation"])[2]').click()  #(start)
# #c_driver.find_element("xpath","(//i[@class='x1b0d499 xaj1gnb'])[2]").click()  #(pause)
# c_driver.find_element("xpath","(//input[@placeholder='Search videos'])[1]").click()  #(search)
#
#
driver.close()



#WebDriverWait(c_driver,20).until(EC.element_to_be_clickable((By.xpath,'(//div[@role="presentation"])[1]'))).click() #(start)
#time.sleep(2)
#a_obj = ActionChains(c_driver)
#start = c_driver.find_element("xpath","(//div[@data-pagelet='MainFeed'])[1]")
#a_obj.double_click(start).perform()
#time.sleep(3)

#a_obj = ActionChains(c_driver)
#start = c_driver.find_element("xpath","(//i[@class='x1b0d499 xaj1gnb'])[9]")
#a_obj.move_to_element(start).perform()

#c_driver.find_element("xpath","(//span[contains(text(),'Like')])[1]").click() #(like not work)
#c_driver.find_element("xpath","(//i[@class='x1b0d499 x1d69dk1'])[3]").click()  #(comment not work)


#c_driver.find_element("xpath", "(//input[@aria-label='Show notification dots'])[1]").click() #(noti pause)
#time.sleep(3)

#c_driver.find_element("xpath","(//i[@class='x1b0d499 x1d69dk1'])[11]").click() #(cross button)

#c_driver.find_element("xpath","(//i[@class='x1b0d499 xep6ejk'])[10]").click()   #(new video)



#(//i[@class='x1b0d499 xep6ejk'])[2] (setting)
#(//div[@class="__fb-light-mode x1qjc9v5 x9f619 x78zum5 xdt5ytf xl56j7k x1c4vz4f xg6iff7"]) (manage)