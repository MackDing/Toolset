from PIL import Image
import os

# 图像文件夹路径
image_folder = r'D:\ExtremeVision\Github\Toolset\PDF_handle\jpg'

# 获取图像文件列表并按文件名中的数字排序
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

# 打开第一张图像以获取宽度和高度
first_image = Image.open(os.path.join(image_folder, image_files[0]))
width, height = first_image.size

# 创建一个新的长图
result_image = Image.new('RGB', (width, height * len(image_files)))

# 逐个粘贴图像到长图中
for i, image_file in enumerate(image_files):
    image = Image.open(os.path.join(image_folder, image_file))
    result_image.paste(image, (0, i * height))

# 保存拼接后的长图
result_image.save(r'D:\ExtremeVision\Github\Toolset\PDF_handle')

print('拼接完成')
