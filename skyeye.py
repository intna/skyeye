from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pyautogui
import pandas as pd

list  = [

    "//*[@id='page-container']/div[1]/div/div[3]/div[2]/div[1]/div[1]/input",               #输入公司名称
    "//*[@id='page-container']/div[1]/div/div[3]/div[2]/div[1]/button",                     #天眼一下
    "//*[@id='page-container']/div/div[2]/section/main/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/a/span/em",         #目标公司
    "//*[@id='page-root']/div[3]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/table",               #经营范围
    "//*[@id='page-root']/div[3]/div/div[1]/div[1]/div[3]/div[1]/div[4]/div[3]/div/div/div/span[2]",      #公司简介
    "//*[@id='page-root']/div[3]/div/div[1]/div[1]/div[3]/div[1]/div[4]",                #网址等
    "//*[@id='JS_Layout_Nav']/div/div/div/div/div[1]/div[5]/a",                                         #经营状况
    "//*[@id='JS_Layout_Nav']/div/div/div/div/div[2]/div/div[5]/a[3]/span[1]"                       #行政许可
]

fanweis = []
jianjies = []
data = pd.read_excel("pandas.xlsx", sheet_name=0, usecols=[0], squeeze=True)
#将源表中的热力公司名称拷贝到另一张表里，只需执行一次。
def fix():
    data = pd.read_excel("heat.xlsx", sheet_name=0, usecols=[0], squeeze=True) #读取原表
    data.to_excel('pandas.xlsx',sheet_name='heat',index=False) #写入现有的表


def eye(x):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)  # 不自动关闭浏览器
    option.add_argument('--window-size=1920,1080')
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)  # 添加option到chrome_option中
    driver.get("https://www.tianyancha.com/")
    WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,list[0])),message="页面不存在目标元素，寄！")
    driver.find_element(By.XPATH,list[0]).send_keys(data[x])
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, list[1])),message="页面不存在目标元素，寄！")
    time.sleep(3)
    button = driver.find_element(By.XPATH,list[1])
    driver.execute_script("(arguments[0]).click()",button)
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, list[2])),message="页面不存在目标元素，寄！")
    time.sleep(1)
    driver.find_element(By.XPATH,list[2]).click()
    windows = driver.window_handles  #获取打开的多个窗口句柄
    driver.switch_to.window(windows[-1])  #去最后一个界面
    time.sleep(2)
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, list[3])),message="页面不存在目标元素，寄！")
    fanwei = driver.find_element(By.XPATH,list[3]).text
    jianjie = driver.find_element(By.XPATH,list[5]).text
    fanweis.append(fanwei)
    jianjies.append(jianjie)
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, list[6])),message="页面不存在目标元素，寄！")
    hold = driver.find_element(By.XPATH,list[6])
    ActionChains(driver).context_click(hold).perform()
    time.sleep(1)
    # try:
    #    driver.find_element(By.XPATH,list[7]).click()
    #    time.sleep(2)
    #    path = "D:\chromedownload\\"
    #    file_name = data[x] + '.png'
    #    path = os.path.join(path, file_name)
    #    driver.get_screenshot_as_file(path)
    # except Exception:
    #     pass
    driver.quit()
if __name__ == '__main__':
   i = 0

   while i < 500:
    try:
        eye(i)
        print("已经获取了%d个"%(i+1))
        i = i+1
    except Exception:
        print(i + "出问题了")
        i = i + 1
        pass
   else:
       print("拷贝完了")

   dic = {"fanwei":fanweis,"jianjie":jianjies}
   df = pd.DataFrame(dic,index=data[0:500])
   # df1 = pd.DataFrame(df.values.T,columns=df.index,index=df.columns)
   df.to_excel('result.xlsx',sheet_name='result',index=True)





























