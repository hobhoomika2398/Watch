import pytest

from Library.excel_lib import read_locators,read_data
from Library.config import Config
from POM.watch_module import WatchModule

# from selenium import webdriver




class TestWatchModule:
    @pytest.mark.parametrize("username,password",[("9019823361","j@b12345"),("987654321","bhumi@23")])
    def test_login(self,_driver,username,password):
        # self.driver = webdriver.Chrome(Config.CHROME_PATH)
        # self.driver.get(Config.URL)

        lp = WatchModule(_driver)
        lp.user_name(username)
        lp.pass_word(password)
        lp.log_in()
        lp.watch_1()
        lp.setting_1()
        lp.not1_start()
        lp.cus_not2()
        lp.allow_not3()
        lp.new1_not4()
        lp.man_pag()
        lp.cro_butt()
        lp.liv_btn()
        lp.show_btn()






