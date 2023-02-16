from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pyautogui
import pandas as pd


bing = [
    "//*[@id='waitListDefault']/div[2]/a[1]",                  #加入等待列表
    "//*[@id='searchform2']/input[2]",              #搜索按钮
    "//*[@id='codex']/a",                           #聊天
    "//*[@id='searchbox']",                       #输入框
    "//*[@id='cib-action-bar-main']//div/div[2]/div[2]/div[2]/div/button/svg-icon//svg/path"                #发送




]

def bing_chat():
    # driver.execute_script("arguments[0].scrollIntoView();", target)
    option = webdriver.EdgeOptions()
    option.add_experimental_option("detach", True)  # 不自动关闭浏览器
    driver = webdriver.Edge(options=option)
    driver.get("https://www.bing.com/")
    time.sleep(8)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(1106,468,duration=1)
    pyautogui.click()
    time.sleep(3)
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, bing[2])),message="页面不存在目标元素，寄！")
    driver.find_element(By.XPATH,bing[2]).click()
    time.sleep(3)
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, bing[0])),message="页面不存在目标元素，寄！")
    join = driver.find_element(By.XPATH,bing[0])
    driver.execute_script("(arguments[0]).click()", join)
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, bing[3])),message="页面不存在目标元素，寄！")
    time.sleep(5)
    driver.find_element(By.XPATH,bing[3]).send_keys("请帮我写一个爬虫程序")
    time.sleep(3)
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, bing[4])),message="页面不存在目标元素，寄！")
    driver.find_element(By.XPATH,bing[4]).click()