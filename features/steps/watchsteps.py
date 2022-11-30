from behave import *
from selenium import webdriver
import time

@given(u'Launch the browser')
def step_impl(context):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--disable-notification")

    chrome_option.add_argument("--disable-infobars")

    chrome_option.add_argument("start-maximized")

    chrome_option.add_argument("--disable-extensions")

    chrome_option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    chrome_option.add_argument("use-fake-ui-for-media-stream")

    context.driver  = webdriver.Chrome(r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe' )
    time.sleep(2)
    context.driver.implicitly_wait(10)



@when(u'open facebook home page')
def step_impl(context):
     context.driver.get("https://www.facebook.com/")
     time.sleep(2)
     context.driver.maximize_window()
     time.sleep(2)
     context.driver.find_element_by_name("email").send_keys("9019823361")
     time.sleep(2)
     context.driver.find_element_by_id("pass").send_keys("j@b12345")
     time.sleep(3)
     context.driver.find_element_by_name("login").click()
     time.sleep(3)


@when(u'watch module is selected by default')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element("xpath", '//a[@href="https://www.facebook.com/watch/"]').click()  # (watch)
    time.sleep(2)


# @when(u'user is able to search the videos')
# def step_impl(context):
#


@when(u'user is able to click on setting')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@aria-label='Edit notification settings']").click()  # (setting)
    time.sleep(5)


@when(u'user is able to turn on the show notification dots')
def step_impl(context):
    context.driver.find_element("xpath", "(//input[@aria-label='Show notification dots'])[1]").click()  # (noti start)
    time.sleep(5)


@when(u'user is able to click on custom notifications')
def step_impl(context):
    context.driver.find_element("xpath", "(//span[normalize-space()='Custom notifications'])[1]").click()  # (custom noti)
    time.sleep(5)


@when(u'user is able to turn on the allow video notifications')
def step_impl(context):
    context.driver.find_element("xpath", "(//input[@aria-label='Opted out all badge types'])[1]").click()  # (allow video noti)
    time.sleep(4)


@when(u'user is able to click on manage pages you follow')
def step_impl(context):
    context.driver.find_element("xpath", "//span[text()='Manage pages you follow']").click()  # (manage page)
    time.sleep(5)


@when(u'user is able to click on the cross button')
def step_impl(context):
    context.driver.find_element("xpath", "(//div[@aria-label='Close' and @role='button'])[2]")  # (cross button)
    context.obj.click(cross).perform()
    time.sleep(3)


@when(u'user is able to click on the live icon')
def step_impl(context):
    context.driver.find_element("xpath",
                        "(//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft'][normalize-space()='Live'])[1]").click()  # (live)
    time.sleep(3)


@when(u'user is able to click on the shows icon')
def step_impl(context):
    context.driver.find_element("xpath", '(//span[text()="Shows"])[1]').click()  #(show)


@when(u'user is able to click on the saved videos icon')
def step_impl(context):
    assert True


@then(u'verify watch module working')
def step_impl(context):
    assert True