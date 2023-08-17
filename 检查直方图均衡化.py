import cv2
import numpy as np

def calculate_histogram(image):
    hist, _ = np.histogram(image, bins=np.arange(256 + 1))
    return hist

def check_histogram_equalization(image_before, image_after, threshold=10):
    hist_before = calculate_histogram(image_before)
    hist_after = calculate_histogram(image_after)
    # print(hist_before)
    # print(hist_after)
    diff = np.abs(hist_before - hist_after)
    # print(diff)
    return np.any(diff > threshold)

def main():
    # 加载原始图片和处理后的图片
    original_image = cv2.imread("./results/task_result.jpg", cv2.IMREAD_COLOR)
    hist_eq_image = cv2.imread("./datasets/test.jpeg", cv2.IMREAD_COLOR)
    #  hist_eq_image = cv2.imread("./results/task_result.jpg", cv2.IMREAD_COLOR)

    # 转换为灰度图像
    gray_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    gray_hist_eq = cv2.cvtColor(hist_eq_image, cv2.COLOR_BGR2GRAY)

    # 校验直方图均衡化是否应用
    has_histogram_equalization = check_histogram_equalization(gray_original, gray_hist_eq)

    # 输出结果
    if has_histogram_equalization:
        print("图片应用了直方图均衡化")
    else:
        print("图片未应用直方图均衡化")

if __name__ == "__main__":
    main()