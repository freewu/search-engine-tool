import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib.parse import urlencode


def run():
    # print("aaa")
    # exit(0)
    # 配置选项
    options = Options()
    # # 设置使用无头浏览器
    options.add_argument("--headless")
    # # 禁用gpu加速
    # options.add_argument("--disable-gpu")
    # # 禁止浏览器被监控提示
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # # 不自动关闭浏览器
    # options.add_experimental_option('detach', True)
    # # 设置请求头user-agent
    # options.add_argument("--user-agent=''")
    # # 设置窗口最大化
    options.add_argument('--start-maximized')
    # # 设置窗口大小
    # options.add_argument('--window-size=200,200')
    # # 无痕模式
    # options.add_argument('--incognito')
    # # 隐藏滚动条
    # options.add_argument('--hide-scrollbars')
    # # 禁用js
    # options.add_argument('--disable-javascript')
    # # 不加载图片（拦截图片）
    # options.add_argument('--blink-settings=imagesEnabled=false')
    # 初始化浏览器
    driver = webdriver.Chrome(options=options)
    # 访问网页
    # `https://search.yahoo.com/search?p=${encodeURIComponent(query)}&ei=UTF-8&fr=fp-tts`
    keyword = "诺基亚"
    query = {
        "q": keyword,
        "oq": keyword
    }
    # `https://www.google.com.hk/search?q=%s&uule=w+CAIQICIaQXVzdGluLFRleGFzLFVuaXRlZCBTdGF0ZXM&hl=en&gl=us&sourceid=chrome&ie=UTF-8%22#ip=1`
    print("https://www.google.com.hk/search?%s&uule=w+CAIQICIaQXVzdGluLFRleGFzLFVuaXRlZCBTdGF0ZXM&hl=en&gl=us&sourceid=chrome&ie=UTF-8#ip=1" % urlencode(query))
    # driver.get('https://baidu.com')
    # exit(0)
    driver.get("https://www.google.com.hk/search?%s&uule=w+CAIQICIaQXVzdGluLFRleGFzLFVuaXRlZCBTdGF0ZXM&hl=en&gl=us&sourceid=chrome&ie=UTF-8#ip=1" % urlencode(query))
    # 隐式等待 10s 通过设定的时长等待页面元素加载完成，再执行下面的代码，如果超过设定时间还未加载完成，则继续执行下面的代码
    driver.implicitly_wait(10)
    # time.sleep(1)
    # 打印标题
    # print(driver.title)
    driver.save_screenshot("./google.png")
    
    elements = driver.find_element(By.ID, "search").find_elements(By.CLASS_NAME, 'MjjYud')
    print(len(elements))
    #exit();
    # print(elements)
    for e in elements:
        # print("text:" + e.get_attribute("innerHTML"))
        # p = e.find_element(By.CLASS_NAME, "fc-refblack")
        # 处理 vedio 行
        try:
            p = e.find_element(By.CLASS_NAME, "VwiC3b")
            # print("text:" + p.get_attribute("innerHTML"))
            print("text:" + p.get_attribute("textContent"))
        except Exception as e:
            continue
        # print(e.find_element(By.CLASS_NAME, "b_caption").text)
        a = e.find_element(By.TAG_NAME, "a")
        print("href:" + a.get_attribute("href"))
        print("title:" + a.find_element(By.TAG_NAME, "h3").get_attribute("textContent"))
        # print(a.text)

    # const liElements = Array.from(
    #   document.querySelector("#search > div > div").childNodes
    # );
    # const firstFiveLiElements = liElements.slice(0, 5);
    # return firstFiveLiElements.map((li) => {
    #   const linkElement = li.querySelector("a");
    #   const href = linkElement.getAttribute("href");
    #   const title = linkElement.querySelector("a > h3").textContent;
    #   const abstract = Array.from(
    #     li.querySelectorAll("div > div > div > div > div > div > span")
    #   )
    #     .map((e) => e.textContent)
    #     .join("");
    #   return { href, title, abstract };
    # 关闭浏览器
    driver.close()


if __name__ == '__main__':
    run()
