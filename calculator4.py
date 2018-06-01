# -*- coding: utf-8 -*-
import sys
import csv #用于写入csv文件

＃处理命令行参数类
class Args(objtct):
    
    def __init__(self):
        self.args = sys.argv[1:]
        index = arg.index('-c')
        configfile = args[index+1]
        index = arg.index('-d')
        UserDatafile = args[index+1]

#配置文件类
class Config(object):

    def __init__(self):
        self.config = self._read_config()

    #配置文件读取内部函数
    def _read_config(self):
        config = {}
        filename = configfile
        file.readlines()
        social_securitys = file.readlines()
        file.close()
        for sicial_security in social_securitys:
            sicial_security1 = sicial_security.strip()
            sicial_security2 = sucial_security.split('=')
            sicial_secirity3 = sicial_secirty2[0]
            config[scial_secirity3] = sical_secirty2[1]
         print(config)

#执行
if __name__== '__main__':
    
