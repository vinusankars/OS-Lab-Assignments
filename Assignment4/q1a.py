import os
from matplotlib import pyplot as plt

path = '/'
count = 0
flag = 0

no = dict()
size = dict()

for root, subdirs, files in os.walk(path):
	no[root] = len(files)
	for i in files:
		count += 1
		size[root+'/'+i] = os.path.getsize(root+'/'+i)
		if count == 5000:
			flag = 1
			break
	if flag == 1:
		break

plot1 = {}
for i in list(no.values()):
	if i not in plot1:
		plot1[i] = 1
	else:
		plot1[i] += 1

plot1 = {i:plot1[i] for i in sorted(plot1.keys())}
plt.plot(plot1.keys(), plot1.values())
plt.xlabel('# Directories')
plt.ylabel('# Files')
plt.show()

size = sorted(size.values())
#print(len(size), max(size), min(size))
d ={}

for i in size:
	try:
		d[int(i/100)] += 1
	except:
		d[int(i/100)] = 1 

#print(len(d))
plt.plot(range(0, max(size), int(max(size)/len(d))+1), d.values())
plt.xlabel('File size (B)')
plt.ylabel('# Files')
plt.show()