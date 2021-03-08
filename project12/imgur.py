from selenium import webdriver as wd
import time as t
import requests as req
import sys
import os

browser=wd.Chrome()
browser.get('https://imgur.com')
searchBar=browser.find_element_by_class_name('Searchbar-textInput')
searchBar.send_keys(sys.argv[1])
submit=browser.find_element_by_class_name('Searchbar-submitInput')
submit.click()
t.sleep(2)
imgs=browser.find_elements_by_class_name('image-list-link')
c=0
os.makedirs('imgur')
os.chdir('imgur')
for i in imgs:
	link=i.get_attribute('href')+'.png'
	link=(link[:8]+'i.'+link[8:]).replace('gallery/','')
	print(link)
	img=req.get(link)
	img.raise_for_status()
	print(f'Downloading {link}...')
	imgFile=open(f'img{c}.png','wb')
	for j in img.iter_content(100000):
		imgFile.write(j)
	c+=1	
	imgFile.close()
	
browser.quit()	
