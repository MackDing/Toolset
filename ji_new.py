import argparse
import os
import platform
import shutil
import time
from pathlib import Path
import sys
import json
sys.path.insert(1, '/project/train/src_repo/yolov5/')
import cv2
import torch
import torch.backends.cudnn as cudnn
from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, smart_inference_mode
from utils.augmentations import letterbox
import numpy as np
# ####### 参数设置
conf_thres = 0.5
iou_thres = 0.5
prob_thres = 0.5
#######

imgsz = 480
weights = "/project/train/models/exp/weights/best.pt"
device = '0'
stride = 32
names=['sand_mining_ship','sand_carrier','boat','buoy']
def init():
    # Initialize
    global imgsz, device, stride
    device = select_device('0')
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = DetectMultiBackend(weights, device=device, dnn=False)
    stride, pt, jit, engine = model.stride, model.pt, model.jit, model.engine
    imgsz = check_img_size(imgsz, s=stride)  # check img_size
    model.half()  # to FP16
    model.eval()
    # model.warmup(imgsz=(1, 3, 480, 480))  # warmup
    return model

def process_image(model, input_image=None, args=None, **kwargs):
    # Padded resize
    img0 = input_image
    img = letterbox(img0, new_shape=imgsz, stride=stride, auto=True)[0]

    # Convert
    img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
    img = np.ascontiguousarray(img)

    img = torch.from_numpy(img).to(device)
    img = img.half()
#     img = img.float()
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if len(img.shape) == 3:
        img = img[None]
    # pred = model(img, augment=False, val=True)[0]
    pred = model(img, augment=False, visualize=False)
    # Apply NMS
    pred = non_max_suppression(pred, conf_thres, iou_thres, agnostic=False)

    fake_result = {}

    fake_result["algorithm_data"] = {
       "is_alert": False,
       "target_count": 0,
       "target_info": []
   }
    fake_result["model_data"] = {"objects": []}
    # Process detections
    cnt = 0
    for i, det in enumerate(pred):  # detections per image
        gn = torch.tensor(img0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
        print(len(det))
        if det is not None and len(det):
            # Rescale boxes from img_size to im0 size
            # det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()
            det[:, :4] = scale_boxes(img.shape[2:], det[:, :4], img0.shape).round()
            for *xyxy, conf, cls in det:
                if conf < prob_thres:
                    continue
                fake_result["model_data"]['objects'].append({
                    "x":int(xyxy[0]),
                    "y":int(xyxy[1]),
                    "width":int(xyxy[2]-xyxy[0]),
                    "height":int(xyxy[3]-xyxy[1]),
                    "confidence":float(conf),
                    "name":names[int(cls)]
                })
                cnt+=1
                fake_result["algorithm_data"]["target_info"].append({
                    "x":int(xyxy[0]),
                    "y":int(xyxy[1]),
                    "width":int(xyxy[2]-xyxy[0]),
                    "height":int(xyxy[3]-xyxy[1]),
                    "confidence":float(conf),
                    "name":names[int(cls)]
                }
                )
    if cnt>0:
        fake_result ["algorithm_data"]["is_alert"] = True
        fake_result ["algorithm_data"]["target_count"] = cnt
    else:
        fake_result ["algorithm_data"]["target_info"]=[]
    return json.dumps(fake_result, indent = 4)

if __name__ == '__main__':
    from glob import glob
    # Test API
    image_names = glob('/home/data/878/*.jpg')
    predictor = init()
    s = 0
    for image_name in ['/project/train/src_repo/yolov5/data/images/bus.jpg']:
        print(image_name)
        img = cv2.imread(image_name)
        t1 = time.time()
        res = process_image(predictor, img)
        print(res)
        t2 = time.time()
        s += t2 - t1
        break
    print(1/(s/100))