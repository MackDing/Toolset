from pydub import AudioSegment

def convert_mp3_to_aiff(mp3_file, aiff_file):
    # 使用pydub加载MP3文件
    audio = AudioSegment.from_mp3(mp3_file)

    # 将音频导出为AIFF格式
    audio.export(aiff_file, format='aiff')

# 调用示例
mp3_file = './datasets/3大核心句型.mp3'  # 输入的MP3文件路径
aiff_file = './results/output.aiff'  # 输出的AIFF文件路径

convert_mp3_to_aiff(mp3_file, aiff_file)