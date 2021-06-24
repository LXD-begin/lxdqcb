from commen import method
from testdata import data
from selenium import webdriver

driver = webdriver.Chrome()  # 与火狐浏览器建立连接
driver.implicitly_wait(10)  # 添加隐式等待
#取测试数据
for shuju in data.data1:
   url = data.data1['url']
   username = data.data1['name']
   password = data.data1['password']
   key = data.data1['key']
resulrt = method.searcg(driver=driver,username=username,password=password,key=key,url=url)
print(resulrt)