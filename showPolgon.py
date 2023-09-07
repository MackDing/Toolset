import cv2
import numpy as np

def showPolygon(image_path, polygon_coords, linestring_coords):
    polygon_str = polygon_coords[0]
    linestring_str = linestring_coords[0]
    # print(polygon_str)

    polygon_coords = [(float(coord.split()[0]), float(coord.split()[1])) for coord in polygon_str[10:-2].split(",")]
    linestring_coords = [(float(coord.split()[0]), float(coord.split()[1])) for coord in linestring_str[11:-1].split(",")]

    print(polygon_coords)
    # 加载本地图片
    image = cv2.imread(image_path)

    screen_width, screen_height = 1366, 768

    image = cv2.resize(image, (screen_width, screen_height))

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
image_path = "./datasets/222222222222222222_in.jpg"
polygon_coords =  ["POLYGON((0.42484 0.47778,0.35280 0.85000,0.66957 0.81481,0.61739 0.46481))"]
linestring_coords = ["LINESTRING(0.40870 0.61852,0.62733 0.61852)"]
showPolygon(image_path, polygon_coords, linestring_coords)