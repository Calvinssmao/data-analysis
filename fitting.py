import numpy as np
import matplotlib.pylab as pl
from scipy.optimize import leastsq
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] #SimHei是黑体的意思
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题           

# 文件名称
file_name = '7.0cm1d'
file_type = 'csv'
file_full_name = file_name + '.' + file_type

data = np.genfromtxt(file_full_name,delimiter=',',skip_header=2)
print(data[:,0:2])
x, y = data[:,0], data[:,1]

# 归一化
max_y = max(y)
for i,j in enumerate(y):
	y[i] = y[i]/max_y

def func(x,p):
    a, b, c, d= p
    return a*np.exp(-(x-b)**2/(2*c**2)) + d

def residuals(p, y, x):
    return y - func(x, p)

# 建议初始化值：纵范围/横范围 中心横坐标 最大横坐标 最小纵坐标 
p0 = [1,0,0.4,0] # 初始参数
plsq = leastsq(residuals, p0, args=(y,x))
y2 = func(x,plsq[0])

print (u"拟合参数:", plsq[0]) # 实验数据拟合后的参数

# 设置标题  
pl.title(u"标题")
# 设置轴标签  
pl.xlabel(u"横坐标")
pl.ylabel(u"纵坐标")
# 绘图 标签 颜色：color='red'
pl.plot(x, y, 'b', label='Experiment data', linewidth=3)
pl.plot(x, y2, 'r--',label='Fitting data', linewidth=2)
pl.legend()
# 保存图像
pl.savefig("fit" + file_name + ".png")
pl.show()