#coding:utf-8

"""
KyotoCorpus4.0-200707/dat/synから、素性取得
2016/6/9 @dkubo
"""

ROOT_DIR="../data/KyotoCorpus4.0-200707/dat/syn/"

import os
import re
import codecs

#######################################3
#				再帰オープン
#######################################3
def fild_all_files(directory):
	for root, dirs, files in os.walk(directory):
		yield root
		for file in files:
			yield os.path.join(root,file)



if __name__ == '__main__':
	for file in fild_all_files(ROOT_DIR):
		matchOB=re.search(r"KNP$",file)
		if matchOB:
			with codecs.open(file,'r','euc_jp') as f:
				for line in f:
					arr=line.split()
					print(arr)




