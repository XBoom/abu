import numpy as np 

# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# object	数组或嵌套的数列
# dtype	数组元素的数据类型，可选
# copy	对象是否需要复制，可选
# order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
# subok	默认返回一个与基类类型一致的数组
# ndmin	指定生成数组的最小维度
a = np.array([1,2,3])  
print (a)

# 多于一个维度
b = np.array([[1, 2],[3, 4]])
print(b)
print(b[0])
print(b[1][1])

# 最小维度 
c = np.array([1, 2, 3, 4, 5], ndmin = 3)
print(c)
print(c[0])
#print(c[1]) # error IndexError: index 1 is out of bounds for axis 0 with size 1

# dtype 参数  
a = np.array([1,  2,  3], dtype = complex)  
print (a)