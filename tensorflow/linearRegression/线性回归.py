# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019-05-04
"""

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
'''
使用tensorflow来自己实现一个简单的线性回归
'''
#返回0-1之间100个符合均匀分布的随机数
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 +0.3

#create the tensorflow structure
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biase = tf.Variable(tf.zeros([1]))

y = Weights*x_data +biase

loss = tf.reduce_mean(tf.square(y - y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

#end

sess = tf.Session()
sess.run(init)

for step in range(201):
	sess.run(train)
	y_ = x_data*sess.run(Weights) + sess.run(biase)
	plt.plot(x_data,y_data,color = 'r')
	plt.plot(x_data,y_,color = 'b')
	plt.show()
	if step%20 == 0:
		print(step,sess.run(Weights),sess.run(biase))