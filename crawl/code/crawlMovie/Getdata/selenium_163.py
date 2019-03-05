# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
drive = webdriver.Chrome()
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
drive.get("http://mail.163.com/")
time.sleep(3)
element = WebDriverWait(drive,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@id='x-URS-iframe1551770628531.8323']"))) #等待直到出现填写账号密码iframe

drive.switch_to.frame("x-URS-iframe1551770628531.8323") #切换标签
inputText = drive.find_element(By.XPATH,"//*[@id='account-box']//div[2]//input") # 定位到账号框
inputText.send_keys("hepengme@163.com ")
password=drive.find_element(By.XPATH,"//*[@id='login-form']//div//div[3]//div[2]//input[2]")
password.send_keys("hp101537")

password.send_keys(Keys.ENTER) #模拟回车键

time.sleep(5)
drive.quit()
