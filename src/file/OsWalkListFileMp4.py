# *-* coding:utf -*
import os

fileTupple = os.walk("G:\BaiduNetdiskDownload\专业美术")
list=[];
for root,dirs,files in fileTupple:
    for file in files:
        if os.path.splitext(file)[1] == ".mp4":
            list.append(os.path.join(root,file))

for i in list:
    print(i)
#金融与信息技术

