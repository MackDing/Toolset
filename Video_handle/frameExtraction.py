import cv2

def extract_frames(video_path, output_folder, frame_interval=1):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("无法打开视频文件")
        return

    # 获取视频帧率和总帧数
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 计算每隔多少帧抽取一帧
    step = frame_interval * fps

    # 逐帧抽取并保存
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % step == 0:
            output_file = f"{output_folder}/frame_{count // step:04d}.jpg"
            cv2.imwrite(output_file, frame)

        count += 1

    cap.release()
    print(f"成功抽取 {count // step} 帧图像")

if __name__ == "__main__":
    video_file = r"F:\Dataset\2023\August\人员上下楼梯扶手1.0\vas\down.mp4"  # 替换为你的视频文件路径
    output_folder = r"F:\Dataset\2023\August\人员上下楼梯扶手1.0\vas"  # 替换为输出帧图像的文件夹路径

    extract_frames(video_file, output_folder, frame_interval=20)  # 每隔10帧抽取一帧