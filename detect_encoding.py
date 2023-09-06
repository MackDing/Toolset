
# -*- coding: utf-8 -*-
import cchardet as chardet

# 定义要检查的文件名列表
file_names = [
    r'D:\ExtremeVision\DeskTop\商汤测试数据\test\all\test_图1.jpg',
    r'D:\ExtremeVision\DeskTop\商汤测试数据\test\all\听力.mp3',
    r'D:\ExtremeVision\DeskTop\商汤测试数据\test\all\行间去重.txt'
]

def detect_encoding(file_name):
    with open(file_name, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']


for file_name in file_names:
    encoding = detect_encoding(file_name)
    print(f"The encoding of {file_name} is: {encoding}")


