from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as expected_conditions
import time
import winsound

username = 'xyz@gmail.com'
password = 'xyz'

refresh_seconds = 60  # seconds
beep_time = 20000   # milliseconds; 1 second = 1000 ms

driver = webdriver.Chrome('./chromedriver')
driver.get('https://cgifederal.secure.force.com/')
input_username = driver.find_element_by_id('loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:username')
input_username.clear()
input_username.send_keys(username)
input_password = driver.find_element_by_id('loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password')
input_password.clear()
input_password.send_keys(password)
input_checkbox = driver.find_element_by_name('loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:j_id167')
if(input_checkbox.is_selected() == False):
    input_checkbox.click()
# captcha_image = driver.find_element_by_id('loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:theId')
# src = captcha_image.get_attribute('src')
# base64 = str(src).split(',')[1]
#
# print(base64)
print("[info] Waiting for user to login...")
wait = ui.WebDriverWait(driver, 1000)
wait.until(expected_conditions.url_matches('https://cgifederal.secure.force.com/applicanthome'))
print("[info] User login detected. Assuming user is in home page...")
print("[info] Please keep your mouse pointer out of the screen as an initial snapshot will be taken now... You have 5 seconds to clear out..")
driver.maximize_window()
time.sleep(5)
print("[info] Taking initial snapshot...")
initial_snapshot = driver.get_screenshot_as_base64()
print('[info] Got initial snapshot at %s' % time.strftime("%H:%M:%S", time.localtime()))
print('[info] This program will refresh and take a new snapshot every %s seconds to compare with initial snapshot' % refresh_seconds)
while True:
    time.sleep(refresh_seconds)
    driver.refresh()
    new_snapshot = driver.get_screenshot_as_base64()
    print('[info] new snapshot taken %s' % time.strftime("%H:%M:%S", time.localtime()))
    if new_snapshot != initial_snapshot:
        print('[info] old and new snapshots does not match')
        for x in range(20):
            winsound.Beep(2500, 1000)
            time.sleep(1)
    else:
        print('[info] old and new snapshots are matching')

# print(driver.current_url)
# print(driver.title)

# document.getElementsByClassName("leftPanelText")