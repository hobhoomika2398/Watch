import pytest
from selenium import webdriver
from Library.config import Config
import time
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options




@pytest.fixture(params=["Chrome", "Firefox"])
def _driver(request):
     global driver
     if request.param == "Chrome":

        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--disable-notification")

        chrome_option.add_argument("--disable-infobars")

        chrome_option.add_argument("start-maximized")

        chrome_option.add_argument("--disable-extensions")

        chrome_option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

        chrome_option.add_argument("use-fake-ui-for-media-stream")
        driver = webdriver.Chrome(executable_path=Config.CHROME_PATH,options=chrome_option)


     elif request.param =="Firefox" :
         option=Options()
         option.binary_location=r"C:\Program Files\Mozilla Firefox\firefox.exe"
         driver =webdriver.Firefox(executable_path=r'C:\gd\geckodriver.exe')


     driver.get(Config.URL)
     driver.maximize_window()
     yield driver

     driver.close()



















    # elif browser.lower() == "firefox":
    #     # firefox_path = r'C:\Users\HP\PycharmProjects\pythonProject\selenium_HTD\drivers\geckodriver.exe'
    #     driver = webdriver.Firefox(executable_path=Config.FIREFOX_PATH)
    #
    # else:
    #     # edge_path = r'C:\Users\HP\PycharmProjects\pythonProject\selenium_HTD\drivers\msedgedriver.exe'
    #     driver = webdriver.Edge(executable_path=Config.MSEDGE_PATH)
    #
    # driver.get(Config.URL)
    # driver.maximize_window()
    # yield driver
    # driver.close()