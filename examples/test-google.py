from search_engine_tool import google


def test_google():
    try:
        data = google.search("深圳天气")
        for d in data:
            print(d)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    test_google()