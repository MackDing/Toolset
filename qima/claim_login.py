import requests

login_url = "https://ppsso.qima.com/claim-cloud/"
login_data = {"username": "mack.ding", "password": "123456"}

# 创建一个Session对象
s = requests.Session()

# 发送POST请求
response = s.post(login_url, data=login_data)

# 打印重定向后的cookies
print(s.cookies) 