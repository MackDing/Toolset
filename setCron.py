import re

def generate_cron_expression(year=0, month=0, week=0, day=0, hour=0, minute=0, second=0):
    cron_expression = f"{second} {minute} {hour} {day} {month} {week} {year}"
    return cron_expression

# 输入对应的年、月、周、天、时、分、秒
year = input("输入年份：")
month = input("输入月份：")
week = input("输入星期几（0-6，0表示周日）：")
day = input("输入日期：")
hour = input("输入小时：")
minute = input("输入分钟：")
second = input("输入秒数：")

# 验证输入是否只包含数字和特殊字符
pattern = r'^[0-9\s!@#$%^&*(),.?":{}|<>]+$'
valid_input = re.match(pattern, f"{year} {month} {week} {day} {hour} {minute} {second}")

if valid_input:
    # 生成Cron表达式
    cron_expression = generate_cron_expression(year, month, week, day, hour, minute, second)

    # 打印Cron表达式
    print("生成的Cron表达式为：", cron_expression)
else:
    print("输入包含非法字符，请只输入数字和特殊字符。")