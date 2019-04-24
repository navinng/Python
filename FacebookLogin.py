
from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
  
browser = webdriver.Chrome('D:\chromedriver')
browser.get("http://www.facebook.com")
  
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
  
username.send_keys("navinng87@gmail.com")
password.send_keys("Thanveer1!")

submit.click()
wait = WebDriverWait( browser, 5 )
  
try:
    page_loaded = wait.until_not(lambda browser: browser.current_url == login_page)
except TimeoutException:
    self.fail( "Loading timeout expired" )
  
self.assertEqual(browser.current_url,correct_page,msg = "Successful Login")