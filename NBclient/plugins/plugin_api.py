#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from NBclient.plugins.linux import sysinfo




def LinuxSysInfo():
    #print __file__
    return  sysinfo.collect()


def WindowsSysInfo():
    #此处确保在windows上才调用此模块，避免在Linux上报错
    from NBclient.plugins.windows import sysinfo as win_sysinfo
    return win_sysinfo.collect()
