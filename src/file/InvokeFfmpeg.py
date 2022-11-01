# *-* coding:utf-8 -*
import os
import ctypes

dllHandler = ctypes.cdll.LoadLibrary(os.getcwd() + '\\avcodec-57.dll')
ret = dllHandler.avcodec_configuration()

data = ctypes.string_at(ret, -1).decode("utf-8")
print(data)