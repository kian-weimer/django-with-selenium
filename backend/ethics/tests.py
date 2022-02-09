from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Create your tests here.
class PlayerFormTest(LiveServerTestCase):

  def testform(self):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/bin/chromedriver', chrome_options=chrome_options)
    #Choose your url to visit
    driver.get('https://uiowa.edu/')
    #find the elements you need to submit form
    player_name = driver.find_element_by_id('main-content')

    #check result; page source looks at entire html document
    assert 'Iowa' in driver.page_source

  def testform2(self):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/bin/chromedriver', chrome_options=chrome_options)
    #Choose your url to visit
    driver.get('https://uiowa.edu/')
    #find the elements you need to submit form
    player_name = driver.find_element_by_id('main-content')

    #check result; page source looks at entire html document
    assert 'FAILUREasdfsdgasgub' in driver.page_source