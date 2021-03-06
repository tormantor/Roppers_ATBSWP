import sys
import time as t
from selenium import webdriver as wd
browser=wd.Chrome()
browser.get('https://mail.protonmail.com/login')
user=browser.find_element_by_id('username')
user.send_keys(sys.argv[1])
passc=browser.find_element_by_id('password')
passc.send_keys(sys.argv[2])
login=browser.find_element_by_id('login_btn')
login.click()
t.sleep(6)
compose=browser.find_element_by_class_name('sidebar-btn-compose')
compose.click()
t.sleep(2)
to=browser.find_element_by_class_name('autocompleteEmails-input')
to.send_keys(sys.argv[3])
sub=browser.find_element_by_xpath('/html/body/div[2]/form[1]/div/div[2]/div[5]/input')
sub.send_keys('Weekly Updates and Notifications')
browser.switch_to.frame(browser.find_element_by_tag_name('iframe'))
text=browser.find_element_by_xpath('/html/body/div[1]')
text.send_keys(sys.argv[4])
browser.switch_to.default_content()
send=browser.find_element_by_class_name('btnSendMessage-btn-action')
send.click()
browser.quit()
print(f'Mail sent successfully to {sys.argv[3]}.')
