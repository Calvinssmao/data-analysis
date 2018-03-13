import matplotlib.pyplot as plt
import numpy as np

file_name = '8cm(2D).csv'
ex_line = 5

x1 = 0
x2 = 1600
y1 = 0
y2 = 1200

with open(file_name) as file_object:
	contents = file_object.read().rstrip()
	content = contents.split('\n')[ex_line:][y1:y2]
	Z = []
	for each in content:
		each = each.split(',')[1:-1][x1:x2]
		Z.append(each) 

	for i, val1 in enumerate(Z):
		for j,val2 in enumerate(val1):
			Z[i][j] = float(val2)

	Z = np.array(Z)
	print(Z)
	#plt.imshow(Z, cmap=plt.get_cmap('bone'))
	plt.imshow(Z, cmap=plt.get_cmap('hot'))
	#plt.imshow(Z, cmap=plt.cm.gray) #灰度
	plt.colorbar() 
	plt.show()  
