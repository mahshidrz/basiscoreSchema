import requests


def produce_usedforid():
    url = "http://172.20.19.46/test_jafarzadeh.bc"

    payload = ""
    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    usedforid = response.text
    # print(usedforid)
    # print(response.text)
    return usedforid
