
import time
#打开网页函数
def open_page(driver,url):
    driver.get(url)  # 打开erp网站

#登录函数
def login(driver,username,password):
    driver.find_element_by_id('username').send_keys(username)  # 获取用户名元素，然后输入用户名
    driver.find_element_by_id('password').send_keys(password)  # 获取密码元素，然后输入密码
    driver.find_element_by_id('btnSubmit').click()  # 获取点击登录元素，然后点击登录

#搜索函数
def searcg(driver,url,username,password,key):
    open_page(driver,url)
    login(driver,username,password)

    driver.find_element_by_xpath("//span[text()='零售出库']").click()

    id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')
    id_iframe = id + '-frame'
    print(id, id_iframe)
    driver.switch_to.frame(id_iframe)

    driver.find_element_by_id("searchNumber").send_keys(key)
    driver.find_element_by_xpath("//span[text()='查询']").click()
    time.sleep(1)
    text1 = driver.find_element_by_xpath("//div[contains(text(),'448')]").text
    return text1


