from selenium.common.exceptions import NoSuchElementException as noElem
from selenium import webdriver as wd
import time as t
def check_by_class_name(className):
	try:
		browser.find_element_by_class_name(className)
		return True
	except noElem:
		return False 	
keys=wd.common.keys.Keys
browser=wd.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
html=browser.find_element_by_tag_name('html')
steps=[keys.UP,keys.RIGHT,keys.DOWN,keys.LEFT]
for i in range(500):
	if check_by_class_name('game-over'):
		print('Game over.')
		break
	print(f'Move {i+1}')
	html.send_keys(steps[i%4])
browser.quit()	
