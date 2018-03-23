import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.pylab import mpl
import tools
mpl.rcParams['font.sans-serif'] = ['SimHei'] #SimHei是黑体的意思
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题

# 文件名称
file_name = '7.0cm1d'
# 文件类型
file_type = 'csv'
# 文件全名
file_full_name = file_name + '.' + file_type

# 获取全文数据
all_data = np.genfromtxt(file_full_name,delimiter=',',skip_header=2)
all_data = all_data[:,0:2]
print(all_data)

x_label = all_data[:,0]
y_label = all_data[:,1]

# gap = tools.calculate_gap(x_label,y_label)
# print(gap)

# 设置标题  
plt.title(u"标题")
# 设置X轴标签  
plt.xlabel(u"横坐标")
# 设置Y轴标签  
plt.ylabel(u"纵坐标")
# 绘图 标签 颜色
plt.plot(x_label,y_label,color='blue',label=u'真实数据')
plt.legend()
# 保存图像
plt.savefig(file_name + ".png")
plt.show()
