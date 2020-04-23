# -*- coding:utf-8 -*-
import re
def checkFileName(filename):
    regx = r'(pb|pl|jl)[0-9]{8}_.+_实验[0-9](_v[0-9])*\.'
    searchObj = re.search(regx, filename, re.I|re.U)
    if searchObj:
        print("ok")
        return True
    else:
        print ("Nothing found!!")
        return False



