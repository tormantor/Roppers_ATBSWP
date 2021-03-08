import requests as req
import bs4,sys
link=sys.argv[1]
res=req.get(link)
res.raise_for_status
soup=bs4.BeautifulSoup(res.text,'html.parser')
linkTags=soup.select('a')
print(f'Total available links: {len(linkTags)}')
broken_links=[]
count=0
for i in linkTags:
	if 'href' in i.attrs.keys():
		try:
			link_child=i.attrs['href']
			if link_child.startswith('/') and len(link_child)>2:
				if not link_child[1]=='/':
					link_child=link+link_child
			elif link_child.startswith('#'):
				link_child=link+'/'+link_child
			if link_child.startswith('//'):
				link_child='https:'+link_child			
			res=req.get(link_child)
			count+=1
		except:
			broken_links.append(link_child)
		if res.status_code==404:
			broken_links.append(link_child)
print(f'Total working links: {count}')
print('Broken links: ')			
for i in broken_links:
	print(i)			
			
	
