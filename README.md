# 项目说明
```
https://github.com/bravekingzhang/search-engine-tool 项目的python版本

原项目使用 node + puppeteer 
python版本使用 selenium
```

# 安装
```bash
pip install search-engine-tool
```

# 使用
```python
from search_engine_tool import bing

def test_bing():
    try:
        data = bing.search("深圳天气")
        for d in data:
            print(d)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    test_bing()
```
# 返回格式 
```python
[
    {
        "abstract": "Web目前天氣. PM2:04. 84° F. RealFeel® 93°. RealFeel Shade™ 89°. 空氣品質 不佳. 風 西南偏西 6英里/小时. 風速 6英里/小时. 陰 更多詳情.",
        "href": "https://www.accuweather.com/zh/cn/shenzhen/58194/weather-forecast/58194",
        "title": "深圳, 廣東省, 中國 三日天氣預報 | AccuWeather"
    },
    ...
]
```

# 支持搜索引擎
```
Bing
Google (需要调用方自身能够访问)
Yahoo
```

# todo 
```
1 处理人机验证
2 

```

