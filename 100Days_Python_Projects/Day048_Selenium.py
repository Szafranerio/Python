from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(options=chrome_options)
#
# url ='https://www.python.org'
# driver.get(url)
#
# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.tag_name)
##
# button = driver.find_element(By.ID, value='submit')
# print(button.size)
#
# list_of_dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# for date in list_of_dates:
#    date = date.text
#    print(date)
#
#
# list_of_events = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
# for event in list_of_events:
#    event = event.text
#    print(event)
#
# events = {}
#
# for n in range(len(list_of_dates)):
#    events[n] = {
#        'time': list_of_dates[n].text,
#        'name': list_of_events[n].text,
#    }
#
# print(events)

# Wikipedia
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(options=chrome_options)
#
# url ='http://secure-retreat-92358.herokuapp.com'
# driver.get(url)
#
#
#
# name = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
# name.send_keys('Bartek')
#
# surname = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
# surname.send_keys('Szafran')
#
# mail = driver.find_element(By.XPATH, value='/html/body/form/input[3]')
# mail.send_keys('bartekszafran@icloud.com')
#
# enter = driver.find_element(By.XPATH, value='/html/body/form/button')
# enter.send_keys(Keys.ENTER)


# Coockie Monester Bot
