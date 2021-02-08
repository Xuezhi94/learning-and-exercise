import numpy as np
from Util.Bases import ClassifierBase


class Perceptron(ClassifierBase):
    def __init__(self):
        super(Perceptron, self).__init__()
        self._w = self._b = None

    def fit(self, x, y, sample_weight=None, lr=0.01, epoch=10**6):
        x, y = np.atleast_2d(x), np.array(y)
        if sample_weight is None:
            sample_weight = np.ones(len(y))
        else:
            sample_weight = np.array(sample_weight) * len(y)
        #初始化参数
        self._w = np.zeros(x.shape[1])
        self._b = 0
        for _ in range(epoch):
            y_pred = self.predict(x)
            #获取加权误差向量
            _err = (y_pred != y) * sample_weight
            #引入随机性以进行随机梯度下降
            _indices = np.random.permutation(len(y))
            _idx = _indices[np.argmax(_err[_indices])]
