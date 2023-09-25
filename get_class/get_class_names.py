import csv
import json
import sys
import logging
import traceback
# import cv2
import os
import pprint
import xml.etree.ElementTree as ET
from tqdm import tqdm
from pathlib import Path


class LabelCheck(object):
    def __init__(self, x_dir):
        self.xml_dir = x_dir

    @staticmethod
    def check_voc_label(xml_path):
        l_labels = {}
        if os.path.exists(xml_path):
            in_file = open(xml_path, encoding='utf-8')
            parser = ET.XMLParser(encoding='utf-8')
            tree = ET.parse(in_file, parser=parser)
            root = tree.getroot()
            size = root.find('size')
            for obj in root.iter('object'):
                if ET.iselement(obj.find('bndbox')):
                    cls = obj.find('name').text
                    if cls in l_labels.keys():
                        l_labels[cls] += 1
                    else:
                        l_labels[cls] = 1
            for obj in root.iter('polygon'):
                if ET.iselement(obj.find('class')):
                    cls = obj.find('class').text
                    if cls in l_labels.keys():
                        l_labels[cls] += 1
                    else:
                        l_labels[cls] = 1
                else:
                    print(root.find("filename").text)
        return l_labels

    def check_labels_in_folder(self):
        total_labels = {}
        for xml_path in tqdm(Path(self.xml_dir).rglob('*.xml')):
            l_labels = self.check_voc_label(xml_path)
            for key in l_labels:
                if key in total_labels.keys():
                    total_labels[key] += l_labels[key]
                else:
                    total_labels[key] = l_labels[key]
        return total_labels

    def all_label(self):
        l_labels = self.check_labels_in_folder()
        total_count = 0
        for key, value in l_labels.items():
            total_count += value
        return l_labels, total_count


if __name__ == '__main__':
    # 从文件夹中获取所有的标签
    xml_path = r"\\192.168.1.97\data\inbox\2023\9月\田方杰\青岛自贸区政务大厅项目\done\窗口纠纷识别（目标检测）\V1\testa"
    labels, count = LabelCheck(xml_path).all_label()
    print(list((labels.keys())))
