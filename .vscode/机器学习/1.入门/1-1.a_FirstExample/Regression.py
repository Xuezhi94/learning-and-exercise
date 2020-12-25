# 导入需要用到的库
import matplotlib.pyplot as plt
import numpy as np

#定义存储输入数据(x)和目标数据(y)的数组
x, y = [], []
#遍历数据集，变量sample对应的正是一个个样本
for sample in open(
        "H:/下载/MachineLearning-master/MachineLearning-master/_Data/prices.txt",
        "r"):
    _x, _y = sample.split(",")
    #将字符串数据转化为浮点数
    x.append(float(_x))
    y.append(float(_y))
#读取完数据后，将它们转化为Numpy数组以方便进一步的处理
x, y = np.array(x), np.array(y)
#标准化
x = (x - x.mean()) / x.std()
#将原始数据以散点图的形式画出
plt.figure
plt.scatter(x, y, c='g', s=6)
plt.show()
