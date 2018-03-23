import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] #SimHei是黑体的意思
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题

def run_plot(filename):
	fullfilename = filename + ".dat"
	# 获取全文数据
	data = np.genfromtxt(fullfilename,delimiter='\t',skip_header=0)
	x, y = data[:,0], data[:,1]
	# 绘图 标签 颜色：color='red'
	plt.plot(x, y, 'b', label='Experiment data', linewidth=3)
	plt.legend()
	# 保存图像
	plt.savefig(filename + ".png")
#	plt.show()
	plt.close()
	
def start():
	z = [7,10,15,25,30,40,50]
	w = [0.6, 1.21, 1.67]

	filenames = []
	for j in w:
		for i in z:
			filenames.append("z"+str(i)+"w"+str(j))

	for filename in filenames:
		print(filename)
		run_plot(filename)

start()


