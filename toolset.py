import re, json, pprint

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

# 将结果转换为JSON格式
result_json = json.dumps(result, ensure_ascii=False, indent=4)
# print(result_json)

# 将结果转换为字典并打印    
result_dict = {item["name"]: item["description"] for item in result}
pprint.pprint(result_dict)
