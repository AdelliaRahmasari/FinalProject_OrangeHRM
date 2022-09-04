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

#Menu Admin
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
time.sleep(2)
#Add+
driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
time.sleep(2)
#User Role
ddelement = Select(driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'))
ddelement.select_by_index('0')
time.sleep(2)
#Employee Name
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys('Peter Mac Anderson')
time.sleep(2)
#Status
select = Select(driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]'))
select.select_by_visible_text('Enable')
time.sleep(2)
#Username
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys('Peter')
time.sleep(2)
#Password
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys('Peter789')
time.sleep(2)
#Confirm Password
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys('Peter789')
time.sleep(2)

respon_welcome = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/span').text

assert respon_welcome== "Your password mut contain a lower-case letter, an upper-case letter, a digit and a special character. Try a different password"

driver.close()