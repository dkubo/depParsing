#coding:utf-8

"""
/KyotoCorpus4.0-200707/dat/synから素性取得
2016/6/9 @dkubo
"""

ROOT_DIR="/home/daiki/デスクトップ/naist/class/ProjectP/data/KyotoCorpus4.0-200707/dat/syn/"

import os
import re
import codecs

#######################################
#		再帰オープン
#######################################
def fild_all_files(directory):
	for root, dirs, files in os.walk(directory):
		yield root
		for file in files:
			yield os.path.join(root,file)



if __name__ == '__main__':
	sentID=1		#文に割り当てるid
	bunsetsu=""
	bunsetsuArr=[]
	sentenceHash={}
#	for file in fild_all_files(ROOT_DIR):		#ファイル再帰オープン
	file=ROOT_DIR+'950101.KNP'							#まずは1月1日のみを対象とする
	matchOB=re.search(r'KNP$',file)
	if matchOB:
		print("---------------------------------------")
		print(file)
		print("---------------------------------------")
		with codecs.open(file,'r','euc_jp') as f:
			for line in f:
				arr=line.split()
				if arr[0] == '#':
					continue
				elif arr[0] == '*':
					bunsetsuID = arr[1]
					if bunsetsu != '':
						bunsetsuArr.append(bunsetsu)
					bunsetsu = ""
				elif arr[0] == 'EOS':
					print(sentID)
					sentenceHash[sentID]=bunsetsuArr
					bunsetsuArr=[]
					sentID+=1

				else:
					bunsetsu+=arr[0]
#			print(sentenceHash)




