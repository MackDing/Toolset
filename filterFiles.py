import os

# 指定目录路径
directory = r"F:\Dataset\2023\August\漏油0818\misdeclaration_of_oil-leakage0814151618"

# 遍历目录中的文件
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        if "_in" in filename:
            # 保留含有'_in'的文件
            print(f"保留文件: {filename}")
        elif "_out" in filename:
            # 删除含有'_out'的文件
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"删除文件: {filename}")