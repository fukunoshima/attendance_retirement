from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
import schedule
import jpholiday
import datetime
import random

# --------------------------------------------------
website = ''
user_id = ''
password= ''
attendance_time = "08:30"
retirement_time = "18:00"
randum_max = 30 # minutes
bool_randum= True
# --------------------------------------------------

def today_holiday():
    Today = datetime.date.today()
    if Today.weekday() >= 5 or jpholiday.is_holiday(Today):
        return 0
    else:
        return 1
    
wait_max = randum_max*60
def random_wait():
    if bool_randum:
        randum_num = random.random()*wait_max
        time.sleep(int(randum_num))

def attend():

    if today_holiday() == 0:
        return

    random_wait()

    #browser=webdriver.Chrome() # use chrome
    browser=webdriver.Firefox() # use firefox
    
    browser.get(website)
    
    
    username = browser.find_element_by_name('login_id')
    username.send_keys(user_id)
    
    username = browser.find_element_by_name('password')
    username.send_keys(password)
    
    elem = browser.find_element_by_class_name('module_button').find_element_by_class_name('module_button-01')
    elem.click()

    elem = browser.find_element_by_class_name('attendance')
    elem.click()
    time.sleep(3)
    Alert(browser).accept()

    elem = browser.find_element_by_class_name('gh_logout')
    elem.click()
    time.sleep(3)
    browser.quit()


def retire():

    if today_holiday() == 0:
        return

    random_wait()

    #browser=webdriver.Chrome() # use chrome
    browser=webdriver.Firefox() # use chrome
    
    browser.get(website)
    
    username = browser.find_element_by_name('login_id')
    username.send_keys(user_id)
    
    username = browser.find_element_by_name('password')
    username.send_keys(password)
    
    elem = browser.find_element_by_class_name('module_button').find_element_by_class_name('module_button-01')
    elem.click()

    elem = browser.find_element_by_class_name('retirement')
    elem.click()
    time.sleep(3)
    Alert(browser).accept()
    
    elem = browser.find_element_by_class_name('gh_logout')
    elem.click()
    time.sleep(3)
    browser.quit()


schedule.every().day.at(attendance_time).do(attend)
schedule.every().day.at(retirement_time).do(retire)

while True:
    schedule.run_pending()
    time.sleep(20)




        






