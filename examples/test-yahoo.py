from search_engine_tool import yahoo


def test_yahoo():
    try:
        data = yahoo.search("深圳天气")
        for d in data:
            print(d)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    test_yahoo()