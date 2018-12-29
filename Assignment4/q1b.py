import os
import csv

file = open('stat2.csv', 'w')

path = '/'
count = 0
flag = 0

for root, subdirs, files in os.walk(path):
	for f in files:
		try:
			x = os.stat(root+'/'+f)
			file.write(str(x[1])+','+str(root+'/'+f)+','+'\n')
			count += 1
		except:
			continue
	if flag == 1:
		break

file.close()