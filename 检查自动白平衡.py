import cv2
import numpy as np

def check_auto_white_balance(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized_image = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(gray_image)
    return not np.array_equal(gray_image, equalized_image)

def main():
    # 加载原始图片和处理后的图片
    original_image = cv2.imread("./datasets/test.jpeg", cv2.IMREAD_COLOR)
    
    # auto_wb_image = cv2.imread("./results/task_result.jpg", cv2.IMREAD_COLOR)
    auto_wb_image = cv2.imread("./datasets/111.jpeg", cv2.IMREAD_COLOR)

    # 校验自动白平衡是否应用
    has_auto_white_balance = check_auto_white_balance(auto_wb_image)

    # 输出结果
    if has_auto_white_balance:
        print("图片应用了自动白平衡")
    else:
        print("图片未应用自动白平衡")

if __name__ == "__main__":
    main()