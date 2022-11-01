# *-* coding:utf-8 -*
# 使用ffmpeg拆分一个目录下的所有视频文件
import getopt
import sys
import os
import subprocess

def printHelp():
    print('指定路径,拆分该目录下的所有文件,或者指定文件,拆分该文件')
    print('参数')
    print('-h\t显示帮助')
    print('-p\t指定视频所在路径,不能和-f同时使用')
    print('-f\t指定视频文件,不能和-p同时使用')

def splitVoideFromPath(sourceDir):
    fileList = os.listdir(sourceDir)
    for file in fileList:
        splitVideo(file, sourceDir)


def splitVideo(file, sourceDir):
    filenameArr = os.path.splitext(file)
    if filenameArr[1] == ".mp4":
        dstPath = os.path.join(sourceDir, filenameArr[0])
        # print(type(path)) ==> <class 'str'>
        b = os.path.exists(dstPath)
        if not b:
            os.mkdir(dstPath)
        srcMp4 = os.path.join(sourceDir, file)
        dstPattern = os.path.join(dstPath, filenameArr[0] + '%03d.mp4')
        cmd = 'ffmpeg -i ' + srcMp4 + ' -f segment -segment_time 600 -segment_format_options movflags=+faststart ' + dstPattern
        print("start split mp4" + file)
        subprocess.call(cmd, shell=True)
        print("end split mp4" + file)


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hp:f:', ['path=', 'file=','help'])
    for k, v in opts:
        if k in ['-h', '--help']:
            printHelp();
            sys.exit(0)
        if k in ['-p', '--path']:
            print("拆分指定目录下的视频"+v)
            splitVoideFromPath(v)
        if k in ['-f', '--file']:
            print("拆分指定的视频"+v)
            splitVideo(v,".")
