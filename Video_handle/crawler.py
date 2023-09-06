#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Author: Mack
# @Time: 2023/1/9 14:38 
# @File: crawler.py
# @Software: PyCharm


import requests, pprint, json, os, subprocess, time
from jsonpath import JSONPath


def get_videoUrl():
    startDate = '2023-01-09'  # 初始日期
    endDate = '2023-01-09'  # 结束日期

    headers = {
        'Cookie': 'ILLEGALSERVER=ejyW6FhNwdFf3ChoyEmWownZ5ORqk0-o16UNAnUN'
    }

    url = f"http://114.215.114.191:7077/api/illegal-country/illegal/data/original/list?pageNum=1&pageSize=100000&params%5BbeginTime%5D={startDate}&params%5BendTime%5D={endDate}"

    try:
        response = requests.request("GET", url, headers=headers)
        jsonResponse = json.loads(response.text)
        # pprint.pprint(jsonResponse)
        # print(type(response.text))
        list1 = JSONPath("$.rows..videoUrl").parse(jsonResponse)
        print(list1)

    except Exception as e:

        print(e, "Cookie Invalid")

# 下周视频
def download(url):
    with requests.get(url, stream=True) as r:
        print('开始下载。。。')
        with open(str(time.strftime('%Y-%m-%d_%H%M%S',time.localtime(int(round(time.time() * 1000))/1000)))+'_vehicle.mp4', 'wb')as f:
            for i in r.iter_content(chunk_size=1024):
                f.write(i)
    print('下载结束')

# 带进度下周视频
# def download_level2(url):
#     with requests.get(url, stream=True) as r:
#         print('开始下载。。。')
#         content_size = int(r.headers['content-length'])
#         with open('v.mp4', 'wb') as f:
#             n = 1
#             for i in r.iter_content(chunk_size=1024):
#                 loaded = n * 1024.0 / content_size
#                 print(loaded)
#                 f.write(i)
#                 print('已下载{0:%}'.format(loaded))
#                 n += 1
#     print('下载结束')


# res = list1.items()

# for i in res():
#     print(i)
# print(res)

if __name__ == '__main__':
    get_videoUrl()
    download('http://122.112.255.69:7077/qc/chezai/device/download/data/0000uyU59HemKf08IbZs10GgyIaGX0.mp4')