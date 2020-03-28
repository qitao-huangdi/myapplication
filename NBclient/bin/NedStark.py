#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import os,sys,platform
from ..core import HouseStark

#for WINDOWS
if platform.system() == "Windows":
    BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
    print(BASE_DIR)
#for linux
else:
    BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])

sys.path.append(BASE_DIR)


if __name__ == '__main__':

    HouseStark.ArgvHandler(sys.argv)