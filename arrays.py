import numpy as np
# 1 D array
n=np.array([10,20,30])
print(n*2)
print("n = ",n)
# 2 D ARRAY
n1=np.array([[10,20,30],[40,50,60]])
print("n1= ",n1)
print(n1*2)
# 3 D ARRAY
np2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("np2= ",np2)
np3=np.arange(4)
print("np3 = ",np3)
np4=np.zeros((2,3))#2 rows 3 columns
print("np4= ",np4)
np5=np.ones((2,3))# 2 rows 3 columns
print("np5 = ",np5)
# random numbers
np6=np.random.rand(5)
print("np6 =",np6)
np7=np.random.rand(2,3)
print("np7 =",np7)
np8=np.random.randint(1,10,5)#range = 1-10 and they should be 5
print("np8= ")