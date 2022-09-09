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
#Apply
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a').click()
time.sleep(2)
#Leave type
select = Select(driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'))
select.select_by_visible_text('CAN-Bereavement')
time.sleep(2)
#Form Date
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys('2022-09-02')
time.sleep(2)
#To Date
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/input").send_keys('2022-09-07')
time.sleep(2)
#Partial Days
ddelement = Select(driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div/div[1]'))
ddelement.select_by_visible_text('All Days')
time.sleep(2)
#Duration
duration = Select(driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/div[1]'))
duration.select_by_visible_text('Half Day-Morning')
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/button').click()
time.sleep(2)

driver.close()