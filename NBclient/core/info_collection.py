#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from NBclient.plugins import plugin_api
import json,platform,sys


class InfoCollection(object):
    def __init__(self):
        pass

    def collect(self):
        '''收集信息，但不汇报'''
        #收集以前先判断操作系统，返回“windows 或 Linux”
        os_platform = self.get_platform()
        try:
            func = getattr(self,os_platform)
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError as e:
            sys.exit("Error:MadKing doens't support os [%s]! " % os_platform)

    def get_platform(self):
        """获取平台信息"""
        os_platform = platform.system()

        return os_platform

    def Linux(self):
        sys_info = plugin_api.LinuxSysInfo()

        return sys_info

    def Windows(self):
        sys_info = plugin_api.WindowsSysInfo()
        #print(sys_info)
        #f = file('data_tmp.txt','wb')
        #f.write(json.dumps(sys_info))
        #f.close()
        return sys_info

    def build_report_data(self,data):

        #add token info at here before send

        return data
