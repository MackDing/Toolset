#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Author: Mack
# @Time: 2023/4/12 11:55 
# @File: toolset.py
# @Software: PyCharm


# # with open
# import re
#
#
# contents = '''
# （1）person：人员，标注人员
# （2）none_sleeve：无袖（类似背心）
# （3）short_sleeve：短袖
# （4）seven_long_sleeve：七分袖（包含长袖撸起来的情况）
# （5）long_sleeve：长袖
# （6）shorts：短裤
# （7）seven_shorts：七分裤（包含长裤撸起来的情况）
# （8）trousers：长裤
# （9）skirt：短裙
# （10）longuette：长裙
# '''
# # print(content.split())
# # pattern = r'[(a-zA-Z)]+'
# pattern = r'[^[A-Za-z]+$]+'
#
# # re.split
# words = re.split(pattern, contents)
# print(words)
#
# # pandas as pd
# # print(pd.Series(words).value_counts()[:20])
import re
import json

contents = '''
（1）person：人员，标注人员
（2）none_sleeve：无袖（类似背心）
（3）short_sleeve：短袖
（4）seven_long_sleeve：七分袖（包含长袖撸起来的情况）
（5）long_sleeve：长袖
（6）shorts：短裤
（7）seven_shorts：七分裤（包含长裤撸起来的情况）
（8）trousers：长裤
（9）skirt：短裙
（10）longuette：长裙
'''

# 使用正则表达式提取内容
pattern = r'（(\d+)）([\w_]+)：(.+)'
matches = re.findall(pattern, contents)

# 将提取的内容转换为字典列表
result = []
for match in matches:
    item = {
        "index": int(match[0]),
        "name": match[1],
        "description": match[2].strip()
    }
    result.append(item)

# 将结果转换为JSON格式并打u
result_json = json.dumps(result, ensure_ascii=False, indent=4)
# print(result_json)

# 将结果转换为字典并打印    remain
result_dict = {item["name"]: item["description"] for item in result}
print(result_dict)
