from selenium import webdriver
from selenium.webdriver.common.by import By


class Testaidp:
    #添加前置
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://172.16.3.97:1999/#/login")
        self.driver.implicitly_wait(3)
    #添加后置
    def teardown(self):
        pass
    def test_login(self):
        self.driver.find_element(By.ID,"details-button").click()
        self.driver.find_element(By.ID,"proceed-link").click()
   #     self.driver.find_element(By.CSS_SELECTOR,'#app input:nth-child(1)').send_keys("admin")
        self.driver.find_element_by_xpath('//*[@id="login_new"]/div[2]/div[2]/div/div[2]/form/div[1]/div/div/div/input').send_keys("policeman")
        self.driver.find_element_by_xpath('//*[@id="login_new"]/div[2]/div[2]/div/div[2]/form/div[2]/div/div/div/input').send_keys('sdyjs4567')
       