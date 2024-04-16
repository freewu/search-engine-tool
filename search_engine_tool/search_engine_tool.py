from engine import bing


def searchEngineTool(keyword, engine, config={}):
    if engine == "bing":
        return bing.search(keyword, config)
    else:
        raise Exception(f"engine `{engine}` no support!!!")
