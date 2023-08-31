import cv2
import numpy as np

def check_auto_color_balance(image):
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    lab_planes = cv2.split(lab_image)
    
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    modified_l_channel = clahe.apply(lab_planes[0])
    
    modified_lab_image = cv2.merge((modified_l_channel, lab_planes[1], lab_planes[2]))
    color_balanced_image = cv2.cvtColor(modified_lab_image, cv2.COLOR_LAB2BGR)
    
    return not np.array_equal(image, color_balanced_image)

def main():
    # 加载原始图片和处理后的图片
    original_image = cv2.imread("./datasets/test.jpeg", cv2.IMREAD_COLOR)
    # color_balance_image = cv2.imread("./results/task_result.jpg", cv2.IMREAD_COLOR)
    color_balance_image = cv2.imread("./datasets/111.jpeg", cv2.IMREAD_COLOR)

    # 校验自动色彩均衡是否应用
    has_auto_color_balance = check_auto_color_balance(color_balance_image)

    # 输出结果
    if has_auto_color_balance:
        print("图片应用了自动色彩均衡")
    else:
        print("图片未应用自动色彩均衡")

if __name__ == "__main__":
    main()