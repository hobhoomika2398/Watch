from selenium import webdriver
import re
import time
import pytest
from selenium.webdriver.chrome.options import Options
from Library.config import Config
from Library.excel_lib import read_locators,read_data


class WatchModule:

    locator= read_locators(Config.WATCH_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def user_name(self, username):
        # if isinstance(username, float):
        #     username = int(username)
        locator = self.locator["enter_username"]
        self.driver.find_element(*locator).send_keys(username)
        time.sleep(3)

    def pass_word(self, password):
        locator = self.locator["enter_password"]
        self.driver.find_element(*locator).send_keys(password)
        time.sleep(3)

    def log_in(self):
        locator = self.locator["login_1"]

        self.driver.find_element(*locator).click()
        time.sleep(3)

    def watch_1(self):
        locator = self.locator["watch"]

        self.driver.find_element(*locator).click()
        time.sleep(5)

    def setting_1(self):
        locator = self.locator["setting"]

        self.driver.find_element(*locator).click()
        time.sleep(5)

    def not1_start(self):
        locator = self.locator["not_start"]

        self.driver.find_element(*locator).click()
        time.sleep(5)

    def cus_not2(self):
        locator = self.locator["custom _not"]

        self.driver.find_element(*locator).click()
        time.sleep(5)

    def allow_not3(self):
        locator = self.locator["allow_video_not"]

        self.driver.find_element(*locator).click()
        time.sleep(5)

    def new1_not4(self):
        locator = self.locator["new_video_not"]

        self.driver.find_element(*locator).click()
        time.sleep(8)

    def man_pag(self):
        locator = self.locator["manage_page"]

        self.driver.find_element(*locator).click()
        time.sleep(5)

    def cro_butt(self):
        locator = self.locator["cross_button"]

        self.driver.find_element(*locator).click()
        time.sleep(5)

    def liv_btn(self):
        locator = self.locator["live_icon"]

        self.driver.find_element(*locator).click()
        time.sleep(5)

    def show_btn(self):
        locator = self.locator["show_icon"]

        self.driver.find_element(*locator).click()
        time.sleep(5)







