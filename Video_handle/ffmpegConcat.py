#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Author: Mack
# @Time: 2023/1/11 15:57 
# @File: ffmpegConcat.py
# @Software: PyCharm


from ffmpy import FFmpeg
import os
import uuid
import subprocess


# 视频拼接
def concat(video_list: list, output_dir: str):
    if len(video_list) == 0:
        raise Exception('video_list can not empty')
    _ext = check_format(video_list)
    _fps = check_fps(video_list)
    _result_path = os.path.join(
        output_dir, '{}{}'.format(
            uuid.uuid1().hex, _ext))
    _tmp_config = make_tmp_concat_config(video_list, output_dir)
    # ff = FFmpeg(inputs={'{}'.format(_tmp_config): '-f concat -safe 0 -y'}, outputs={
    # _result_path: '-c copy'})
    ff = FFmpeg(inputs={'{}'.format(_tmp_config): '-f concat -safe 0 -y'}, outputs={
        _result_path: '-c:s mov_text '})
    print(ff.cmd)
    ff.run()
    os.remove(_tmp_config)
    return _result_path


# 构造拼接所需临时文件
def make_tmp_concat_config(video_list: list, output_dir: str):
    _tmp_concat_config_path = os.path.join(output_dir, '{}.txt'.format(uuid.uuid1().hex))
    with open(_tmp_concat_config_path, mode='w', encoding='utf-8') as f:
        f.writelines(list(map(lambda x: 'file {}\n'.format(x), video_list)))
    return _tmp_concat_config_path


# 校验每个视频的格式
def check_format(video_list: list):
    _video_format = ''
    for x in video_list:
        _ext = os.path.splitext(x)[-1]
        if _video_format == '' and _ext != '':
            _video_format = _ext
            continue
        if _video_format != '' and _ext == _video_format:
            continue
        if _video_format != '' and _ext != _video_format:
            raise Exception('Inconsistent video format')
    return _video_format


# 校验每个视频的fps
def check_fps(video_list: list):
    _video_fps = 0
    for x in video_list:
        _fps = get_video_fps(x)
        if _video_fps == 0 and _fps:
            _video_fps = _fps
            continue
        if _video_fps != 0 and _fps == _video_fps:
            continue
        if _video_fps != '' and _fps != _video_fps:
            raise Exception('Inconsistent video fps')
    if _video_fps == 0:
        raise Exception('video fps error')
    return _video_fps


# 获取视频fps
def get_video_fps(video_path: str):
    ext = os.path.splitext(video_path)[-1]
    if ext != '.mp4' and ext != '.avi' and ext != '.flv':
        raise Exception('format not support')
    ffprobe_cmd = 'ffprobe -v error -select_streams v -of default=noprint_wrappers=1:nokey=1 -show_entries stream=r_frame_rate {}'
    p = subprocess.Popen(
        ffprobe_cmd.format(video_path),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)
    out, err = p.communicate()
    # print("subprocess 执行结果：out:{} err:{}".format(out, err))
    fps_info = str(out, 'utf-8').strip()

    if fps_info:
        if fps_info.find("/") > 0:
            video_fps_str = fps_info.split('/', 1)
            fps_result = int(int(video_fps_str[0]) / int(video_fps_str[1]))
        else:
            fps_result = int(fps_info)
    else:
        raise Exception('get fps error', f'this issue is: {err} ')
    return fps_result


if __name__ == '__main__':
    print(
        concat(['D:/360极速浏览器下载/0000GDU5=qLI5E48KViFO0tOocpimk.mp4', 'D:/360极速浏览器下载/0000XTU5ZHjhT9488=iZ711=EtjPLV.mp4'],
               'G:/output'))
