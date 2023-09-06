import os
import shutil
import re

dir = r'F:\Dataset\2023\Self-research\front_cam'

algo_code = ['1343货车载客', '2226骑摩托车不戴头盔', '1238摩托车载人', '6061骑电三轮车不戴头盔', '2090三轮车载客', '1087摩托车加装雨棚']

pattern = re.compile('_6061_')
# print(os.listdir(dir))
# make dir
# for i in algo_code:
#     for file_name in os.listdir(dir):
#         if not os.path.isdir(f'{dir}/{i}'):
#             os.mkdir(f'{dir}/{i}')
#
# for file in os.listdir(dir):
# ext = os.path.splitext(file)[1]
# ext = ext[1:]
# print(os.path.join(file))
# print(file)
# if pattern in file:
#     shutil.move(file, r'F:\Dataset\2023\Self-research\front_cam\6061骑电三轮车不戴头盔')
# source_path = f'{dir}/{file}'
# target_path = f'{dir}/{ext}/{file}'
# shutil.move(source_path, target_path)

import cv2

i = "0"
base_path = r'F:\Dataset\2023\Self-research\front_cam'
imglist = os.listdir(base_path)
for img_path in imglist:
    print(img_path)
    print(img_path.find("1238") + 1)
    # if (img_path.find("2226") + 1):
    #     i = "27"
    # elif (img_path.find("6061") + 1):
    #     i = "1"
    # elif (img_path.find("1238") + 1):
    #     i = "2"
    # elif (img_path.find("_1087_") + 1):
    #     i = "3"
    # elif (img_path.find("_1343_") + 1):
    #     i = "4"
    # elif (img_path.find("_2090_") + 1):
    #     i = "5"
    # elif (img_path.find("_2226_") + 1):
    #     i = "6"
    # if not os.path.exists(os.path.join(base_path, i)):
    #     os.makedirs(os.path.join(base_path, i))
    # img = cv2.imread(os.path.join(base_path, img_path))
    # f = "{}/{}".format("data/image/jaffe_48", i)
    # cv2.imwrite("{}/{}.jpg".format(f, img_path.split(".jpg")[0]), img)
