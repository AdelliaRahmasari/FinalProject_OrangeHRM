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

#Menu Time
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span').click()
time.sleep(2)
#Employee Name
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys('Peter Mac Anderson')
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button').click()
time.sleep(2)

respon_welcome = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/form/div[2]/div/div[1]/p').text

assert respon_welcome== "No Timesheets Found"

driver.close()