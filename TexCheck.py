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
    			yield path+os.sep+filename

def FindLabel(filename,Pre):
	labelSet = [];
	for (linenum,line) in enumerate(open(filename)):
		result = re.findall("%s\{\s*([^\}]*)\s*\}"%(Pre),line)
		if len(result):
			labelSet.append([linenum+1,result[0]]);
	return labelSet;


def GetLabelDict(rootPath,Pre):
	labelDict = {}
	for filename in GetFileType(rootPath,"tex"):
	    labelSet = FindLabel(filename,Pre)
	    for line,label in labelSet:
	    	if labelDict.has_key(label):
	    		labelDict[label].append([line,filename])
	    	else:
	    		labelDict[label] = [[line,filename]]
	return labelDict

############### Main
if __name__ == "__main__":
	rootPath = "./"

	# Check Label repeat
	labelDict = GetLabelDict(rootPath,"label")
	hasLabelRepeat = False
	for label in labelDict:
		if len(labelDict[label]) > 1:
			hasLabelRepeat = True
			print "ERROR!!!    Label '%s' is Repeat in these files:"%label
			for (line,filename) in labelDict[label]:
				print "%s(Line %d)"%(filename,line)
			print "\n"

	if not hasLabelRepeat:
		print "[OK!]No Label Definition Repeat!!\n"

	# Check Lable Defined
	labelUsed = GetLabelDict(rootPath,"ref")
	hasLabelUndefined = False
	for label in labelUsed:
		if not labelDict.has_key(label):
			hasLabelUndefined = True
			print "ERROR!!!    Label '%s' is used but not DEFINED!!:"%(label)
			for (line,filename) in labelUsed[label]:
				print "%s(Line %d)"%(filename,line)
			print "\n"

	if not hasLabelRepeat:
		print "[OK!]All Label Used is Defined!!\n"

	print "Finished!!"


