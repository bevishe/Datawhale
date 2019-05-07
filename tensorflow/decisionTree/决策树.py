# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019-05-05
"""

import numpy as np
import pandas as pd
from sklearn import tree
# 色泽 根 敲声 纹理 脐部 触感 好瓜
dataSet = np.array([[1,1,1,2,1,1,0],
					[2,1,0,2,1,1,0],
					[2,1,1,2,1,1,0],
					[1,1,0,2,1,1,0],
					[0,1,1,2,1,1,0],
					[1,0,1,2,0,0,0],
					[2,0,1,2,0,0,0],
					[2,0,1,2,0,1,0],
					[2,0,0,0,0,1,1],
					[1,2,2,2,2,0,1],
					[0,2,2,1,2,1,1],
					[0,1,1,1,2,0,1],
					[1,1,1,0,1,1,1],
					[0,0,0,0,1,1,1],
					[0,1,1,1,2,1,1],
					[2,0,1,2,0,0,1],
					[1,1,0,0,0,1,1],
					])
rows = pd.Series(np.arange(1,dataSet.shape[0]+1))
columns = pd.Series(['色泽','根','敲声','纹理','脐部','触感','好坏'])
dataSet = pd.DataFrame(dataSet,columns=columns,index=rows)
print(dataSet)

clf = tree.DecisionTreeClassifier(criterion='entropy')
x_train = dataSet.iloc[:,0:-1]
y_train = dataSet.iloc[:,-1:]

def Ent(data,column):
	data = data.iloc[:,column:column+1]
	print(data)

def Gain(data,columns):
	pass
Ent(dataSet,2)
