#!/usr/bin/env python
#!-*-coding:utf8-*
#£¡author: pyphrb
from pinyin import PinYin
f = open('createdict.txt', 'w')
test = PinYin()
test.load_word()
def listsThree(lists):
	array1 = lists[0]
	array2 = lists[1]
	array3 = lists[2]
	with open('dict.txt', 'r') as userDict:
		for i in userDict:
			i.strip('\r\n')
			f.write(array1 + i.strip() + '\n')
			f.write(array1 + array2 + array3[0:1] + i.strip() + '\n')
			f.write(array1 + array2[0:1] + array3[0:1] + i.strip() + '\n')
			f.write(array1[0:1] + array2[0:1] + array3[0:1] + i.strip() + '\n')
			f.write(array1.capitalize() + array2[0:1] + array3[0:1] + i.strip() + '\n')
			f.write(array1.capitalize()[0:1] + array2[0:1] + array3[0:1] + i.strip() + '\n')
	#f.close()
	print array1 + array2 + array3[0:1]
	print array1 + array2[0:1] + array3[0:1]
	print array1[0:1] + array2[0:1] + array3[0:1]
	print array1.capitalize() + array2[0:1] + array3[0:1]
	print array1.capitalize()[0:1] + array2[0:1] + array3[0:1]


def listsTwo(lists):
	array1 = lists[0]
	array2 = lists[1]
#array3 = lists[2]
	with open('dict.txt', 'r') as userDict:
		for i in userDict:
			i.strip('\r\n')
			f.write(array1 + i.strip() + '\n')
			f.write(array1 + array2 + i.strip() + '\n')
			f.write(array1 + array2[0:1] + i.strip() + '\n')
			f.write(array1[0:1] + array2[0:1] + i.strip() + '\n')
			f.write(array1.capitalize() + array2[0:1] + i.strip() + '\n')
			f.write(array1.capitalize()[0:1] + array2[0:1] + i.strip() + '\n')
	#f.close()
	print array1 + array2 
	print array1 + array2[0:1]
	print array1[0:1] + array2[0:1]
	print array1.capitalize() + array2[0:1]
	print array1.capitalize()[0:1] + array2[0:1]

def listsFour(lists):
	array1 = lists[0]
	array2 = lists[1]
	array3 = lists[2]
	array4 = lists[3]
	with open('dict.txt', 'r') as userDict:
		for i in userDict:
			i.strip('\r\n')
			f.write(array1 + i.strip() + '\n')
			f.write(array1 + array2 + array3[0:1] + i.strip() + '\n')
			f.write(array1 + array2[0:1] + array3[0:1] + array4[0:1] + i.strip() + '\n')
			f.write(array1[0:1] + array2[0:1] + array3[0:1] + array4[0:1] + i.strip() + '\n')
			f.write(array1.capitalize() + array2[0:1] + array3[0:1] + array4[0:1] + i.strip() + '\n')
			f.write(array1.capitalize()[0:1] + array2[0:1] + array3[0:1] + array4[0:1] + i.strip() + '\n')
	#f.close()
	print array1 + array2 + array3[0:1] + array4[0:1]
	print array1 + array2[0:1] + array3[0:1] + array4[0:1]
	print array1[0:1] + array2[0:1] + array3[0:1] + array4[0:1]
	print array1.capitalize() + array2[0:1] + array3[0:1] + array4[0:1]
	print array1.capitalize()[0:1] + array2[0:1] + array3[0:1] + array4[0:1]
with open('username.txt', 'r') as un:
	for userinfo in un:
		lists = test.hanzi2pinyin(string=userinfo.strip())
		if len(lists) == 2:
			listsTwo(lists)
		elif len(lists) == 3:
			listsThree(lists)
		elif len(lists) == 4:
			listsFour(lists)
		else:
			print 'you chinese name maybe ==1 or > 4 ,please current'
#un.close()
f.close()
