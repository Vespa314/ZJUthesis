# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 21:18:24 2014

@author: vespa
"""
import os
import re

def GetFileType(path,Filetype):
    for path,subdir,files in os.walk(rootPath,topdown=False):
    	if len(files) == 0 or path.find(".") > 0:
    		continue
    	for filename in files:
    		if len(re.findall(r".*%s$"%(Filetype),filename)) > 0 :
    			yield path+r"/"+filename

def FindLabel(filename):
	labelSet = [];
	for (linenum,line) in enumerate(open(filename)):
		result = re.findall("label{(.*)}",line)
		if len(result):
			labelSet.append([linenum+1,result[0]]);
	return labelSet;



labelDict = {}

rootPath = "./"
for filename in GetFileType(rootPath,"tex"):
    labelSet = FindLabel(filename)
    for line,label in labelSet:
    	if labelDict.has_key(label):
    		labelDict[label].append([line,filename])
    	else:
    		labelDict[label] = [[line,filename]]

for label in labelDict:
	if len(labelDict[label]) > 1:
		print "Label '%s' is Repeat in these files:"%label
		for (line,filename) in labelDict[label]:
			print "%s(Line %d)"%(filename,line)
		print "\n"

print "Finished!!"



