# *-* coding:utf-8 -*
import os

fileTupple = os.walk("G:\BaiduNetdiskDownload\专业美术")
for root,dirs,files in fileTupple:
    print("====")
    print(root)
    print(dirs)
    print(files)