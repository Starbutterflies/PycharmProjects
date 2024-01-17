import numpy as np
x0 = np.ones(20).reshape(20,1)
x1 = np.arange(20).reshape(20,1)
x2 = np.arange(20).reshape(20,1)
y = (x1 + 2 * x2 )# 做出来的y的值
X = np.hstack([x0, x1, x2])

# 第一步，定义一个thelta
thelta = np.array([0,1,1]).reshape(3,1) # 这个就是定义的thelta
alpha = 0.001 # 定义学习率
diff = np.dot(X,thelta) - y
gradient = np.dot(X.transpose(),diff)/20             # 首先进行一次梯度下降
thelta = thelta - 0.001 * gradient # 第一次梯度下降
print(thelta)


for i in range(1500):

    diff = np.dot(X, thelta) - y
    gradient = np.dot(X.transpose(), diff) / 20  # 首先进行一次梯度下降

    # 第一次梯度下降
    thelta = thelta - alpha*gradient
    print(thelta)
