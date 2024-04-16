from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib.parse import urlencode


def search(keyword, config={}):
    options = Options()
    # # 设置使用无头浏览器
    options.add_argument("--headless")
    # 初始化浏览器
    driver = webdriver.Chrome(options=options)
    # 访问网页
    query = {
        "q": keyword,
        "oq": keyword
    }
    # print("https://www.bing.com/search?form=QBRE&%s&cc=US" % urlencode(query))
    # driver.get('https://baidu.com')
    # exit(0)
    driver.get("https://www.google.com.hk/search?%s&uule=w+CAIQICIaQXVzdGluLFRleGFzLFVuaXRlZCBTdGF0ZXM&hl=en&gl=us&sourceid=chrome&ie=UTF-8#ip=1" % urlencode(query))
    # 隐式等待 10s 通过设定的时长等待页面元素加载完成，再执行下面的代码，如果超过设定时间还未加载完成，则继续执行下面的代码
    driver.implicitly_wait(10)
    # 获取返回的结果集
    elements = driver.find_element(By.ID, "search").find_elements(By.CLASS_NAME, 'MjjYud')
    result = []
    for e in elements:
        row = {}
        try:
            p = e.find_element(By.CLASS_NAME, "VwiC3b")
            row["abstract"] = p.get_attribute("textContent")
        except Exception as e:
            continue
        # print(e.find_element(By.CLASS_NAME, "b_caption").text)
        a = e.find_element(By.TAG_NAME, "a")
        row["href"] = a.get_attribute("href")
        row["title"] = a.find_element(By.TAG_NAME, "h3").get_attribute("textContent")
        result.append(row)
    
    # 关闭浏览器
    driver.close()
    return result
