﻿#Code for finding and printing webpages
#Need to have installed with webdriver in path.  Instructions at http://selenium-python.readthedocs.io/installation.html
#Pre-load stuff
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import os
import urllib2
import pdfkit
driver = webdriver.Firefox()

#Working Directory
savedir = "C:\DM Experience_Chris Perkins\WOTC_Archive"
os.chdir(savedir)

#Get to Starting URL
url = "http://dnd.wizards.com/articles"
driver.get(url)
assert "All articles" in driver.title

#Remove Popup if there
time.sleep(2)
try:
    alert = driver.find_element_by_css_selector("a[class='fsrDeclineButton']")
    alert.click()
except:
    print('No Alert')

#Navigate to The Dungeon Master Experience
dropdown = driver.find_element_by_class_name('tag')
dropdown.send_keys('The Dungeon Master Experience', Keys.ENTER)

#Remove Popup if there
time.sleep(2)
try:
    alert = driver.find_element_by_css_selector("a[class='fsrDeclineButton']")
    alert.click()
except:
    print('No Alert')

#Accept Cookies Thing
cookiebutton = driver.find_element_by_class_name('agree-button')
cookiebutton.click()

#Open all See More Articles (Click 8 times)
totclicks = 8 #Sometimes 8, sometimes 9
morearticles = driver.find_element_by_css_selector("a[class$='more-button']") #Find More Articles Button
#Stupid For Loop doesn't work on WOTC lame website
morearticles.click()
time.sleep(1)
morearticles.click()
time.sleep(1)
morearticles.click()
time.sleep(1)
morearticles.click()
time.sleep(1)
morearticles.click()
time.sleep(1)
morearticles.click()
time.sleep(1)
morearticles.click()
time.sleep(1)
morearticles.click()
time.sleep(1)
morearticles.click()

all_links = driver.find_elements_by_link_text('Chris Perkins')
base_site = "http://dnd.wizards.com"
for link in all_links:
    #Non Selenium Solution
    #Extract URL Link Info
    soup = BeautifulSoup(link.get_attribute('outerHTML'),'lxml')
    slnk = soup.findAll('a')
    end_site = slnk[0].get('href')
    
    #Go to new URL and pull out HTML
    page = urllib2.urlopen(base_site + end_site)
    psoup = BeautifulSoup(page, 'lxml')
    pheader = psoup.find_all(id='page-header')
    particle = psoup.find_all(class_="main-content article")
    
    #Convert to Strings
    headerstr = unicode.join(u'\n', map(unicode, pheader))
    articlestr = unicode.join(u'\n', map(unicode, particle))
    cleanarticle = articlestr.replace(u'\u2019', '\'').replace(u'\xa0', u' ').replace(u'\u201c', '&quot').replace(u'\u201d','&quot').replace(u'\u2014','--').replace(u'\xc3\xa9','e').encode('ascii','ignore')
    
    #Put together with background color and save
    fullarticle = ['<body style="background-color:#E5DECE; font: 30px Arial;">' + 
        headerstr + cleanarticle + '</body>'] #Add color & font to texts
    name = end_site.split('/')[-1]
    pdfkit.from_string(fullarticle[0], name+'.pdf')


driver.close() #Close Selenium Driver.
