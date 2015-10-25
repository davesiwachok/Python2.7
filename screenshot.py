from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.github.com/')
driver.save_screenshot('github.png')
driver.quit()
#Requires selenium 
#Opens Browser
#Goes to website
#Saves screenshot as .png file in same directory as this file
#Closes browser
