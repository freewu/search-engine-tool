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
    query = {"p": keyword}
    # print("https://www.bing.com/search?form=QBRE&%s&cc=US" % urlencode(query))
    # driver.get('https://baidu.com')
    # exit(0)
    driver.get("https://search.yahoo.com/search?%s&ei=UTF-8&fr=fp-tts" % urlencode(query))
    # 隐式等待 10s 通过设定的时长等待页面元素加载完成，再执行下面的代码，如果超过设定时间还未加载完成，则继续执行下面的代码
    driver.implicitly_wait(10)
    # 获取返回的结果集
    elements = driver.find_elements(By.CLASS_NAME, "algo")
    result = []
    for e in elements:
        row = {}
        # p = e.find_element(By.CLASS_NAME, "b_caption").find_element(By.TAG_NAME, "p")
        # # print("text:" + p.get_attribute("textContent"))
        # row["abstract"] = p.get_attribute("textContent")
        # a = e.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
        # # print("href:" + a.get_attribute("href"))
        # row["href"] = a.get_attribute("href")
        # # print("title:" + a.get_attribute("textContent"))
        # row["title"] = a.get_attribute("textContent")
        try:
            p = e.find_element(By.CLASS_NAME, "compText")
            row["abstract"] = p.get_attribute("textContent")
        except Exception as e:
            continue
        # print(e.find_element(By.CLASS_NAME, "b_caption").text)
        a = e.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a")
        row["href"] = a.get_attribute("href")
        row["title"] = a.get_attribute("aria-label")
        result.append(row)
    
    # 关闭浏览器
    driver.close()
    return result
