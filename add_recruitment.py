from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') 
time.sleep(5) 

#LOGIN
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys('Admin')
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(2)

#Menu Recruitment
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').click()
time.sleep(2)
#Add+
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
time.sleep(2)
#First Name
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").send_keys('Haul')
time.sleep(2)
#Middle Name
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input").send_keys('Robert')
time.sleep(2)
#Last Name
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input").send_keys('Cill')
time.sleep(2)
#Email
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input").send_keys('haulrobertcill@gmail.com')
time.sleep(2)
#Contact Number
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input").send_keys('083526722867')
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]').click()
time.sleep(2)

driver.close()