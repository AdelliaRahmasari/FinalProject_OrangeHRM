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

#Menu Leave
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span').click()
time.sleep(2)
#Menu Leave Entitlement
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li/ul/div[3]/li/a').click()
time.sleep(2)
#Employee Name
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/input").send_keys('Kiyara hu')
time.sleep(2)
#Leave type
select = Select(driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div/div[1]'))
select.select_by_visible_text('CAN-Vacation')
time.sleep(2)
#Leave period
period = Select(driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/div[1]'))
period.select_by_visible_text('2022-01-01 - 2022-12-31')
time.sleep(2)
#Entitlement
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[3]/div/div[2]/input").send_keys('20')
time.sleep(2)


driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]').click()
time.sleep(2)

driver.close()