from pydub import AudioSegment
import random

# 加载本地音频文件
# input_audio = AudioSegment.from_file("./datasets/test.wav")
# input_audio = AudioSegment.from_file("./results/output.aiff")
input_audio = AudioSegment.from_file("./datasets/3大核心句型.mp3")

# 目标总时长为1分钟
target_duration = 50000  # 毫秒

# 计算噪音、静音、弱声部分的时长
noise_duration = 10000  # 10秒
silence_duration = 10000  # 10秒
weak_audio_duration = 20000  # 20秒

# 剪切为目标时长
if len(input_audio) > target_duration:
    input_audio = input_audio[:target_duration]

# 生成噪音段落
noise = AudioSegment.silent(duration=noise_duration)
noise = noise.overlay(
    AudioSegment.silent(duration=random.randint(100, 200)) +
    AudioSegment.silent(duration=random.randint(100, 200)).fade_in(10),
    loop=True)
# 生成静音段落
silence = AudioSegment.silent(duration=silence_duration)

# 生成降低语音信号音量的段落
weak_audio = AudioSegment.silent(duration=weak_audio_duration)
weak_audio = weak_audio.overlay(input_audio.apply_gain(-20), loop=True)

# 拼接原音频的10秒
original = input_audio[20000:30000]

# 合并所有部分
final_audio = noise + silence + weak_audio + original

# 导出结果音频文件
# final_audio.export("./results/test_audio_with_effects.wav", format="wav")
#final_audio.export("./results/test_audio.aiff", format="aiff")
final_audio.export("./results/test_audio.mp3", format="mp3")