import cv2
import numpy as np

def check_smoothed(original_image, processed_image, threshold=10):
    diff = cv2.absdiff(original_image, processed_image)
    diff_sum = np.sum(diff)
    return diff_sum > threshold

def main():
    # 加载原始图片和处理后的图片
    original_image = cv2.imread("./datasets/test.jpeg", cv2.IMREAD_COLOR)
    # processed_image = cv2.imread("./results/task_result.jpg", cv2.IMREAD_COLOR)
    processed_image = cv2.imread("./datasets/test.jpeg", cv2.IMREAD_COLOR)


    # 校验是否使用了平滑滤波
    has_smoothed = check_smoothed(original_image, processed_image)

    # 输出结果
    if has_smoothed:
        print("图片应用了平滑滤波")
    else:
        print("图片未应用平滑滤波")

if __name__ == "__main__":
    main()