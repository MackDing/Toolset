import cv2
import numpy as np

def showPolygon(image_path, polygon_coords, linestring_coords):
    # 加载本地图片
    image = cv2.imread(image_path)

    # 将多边形和线的坐标转换为图像上的坐标
    image_height, image_width, _ = image.shape
    polygon_points = [(int(x * image_width), int(y * image_height)) for x, y in polygon_coords]
    linestring_points = [(int(x * image_width), int(y * image_height)) for x, y in linestring_coords]

    # 绘制多边形和线
    polygon_points = np.array(polygon_points, np.int32)
    polygon_points = polygon_points.reshape((-1, 1, 2))
    cv2.polylines(image, [polygon_points], isClosed=True, color=(0, 0, 255), thickness=2)

    linestring_points = np.array(linestring_points, np.int32)
    linestring_points = linestring_points.reshape((-1, 1, 2))
    cv2.polylines(image, [linestring_points], isClosed=False, color=(0, 255, 0), thickness=2)

    # 显示带有多边形和线的图像
    cv2.imshow("Image with Polygon and Line", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 调用函数
image_path = "./datasets/111111111111111_in.jpg"
polygon_coords = [(0.31493, 0.50370), (0.20452, 0.80556), (0.78795, 0.80741), (0.67001, 0.44259)]
linestring_coords = [(0.27353, 0.64444), (0.70891, 0.63519)]
showPolygon(image_path, polygon_coords, linestring_coords)