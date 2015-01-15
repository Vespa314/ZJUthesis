
#coding=utf-8
import os
import re
# import chardet
## https://pypi.python.org/pypi/chardet

def GetFileType(rootPath,Filetype):
    for path,subdir,files in os.walk(rootPath,topdown=False):
        if len(files) == 0 or path.find(".") > 0:
            continue
        for filename in files:
            if len(re.findall(r".*%s$"%(Filetype),filename)) > 0 :
                yield path+os.sep+filename

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def CountLineNum(line):
    num = 0
    for ch in line:
        try:
            ch.decode('utf-8')
        except:
            num += 1
    return num/3

def CountTexNum(filename):
    print filename,
    letterNum = 0
    # f = open(filename,"r")
    # chardetResult = chardet.detect(f.read())
    # f.close()
    # if not chardetResult['encoding'] == "utf-8":
        # return 0
    for line in open(filename):
        letterNum += CountLineNum(line)
    print letterNum
    return letterNum

rootpath = "./Chapters"
totalNum = 0
for filename in GetFileType(rootpath,"tex"):
    totalNum += CountTexNum(filename)

print "Total:",totalNum