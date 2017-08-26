import numpy as np

a = np.arange(10) ** 2
b = np.arange(10) ** 3
c = a + b
print(c)

t = np.arange(0., 5., 0.2)
print(t.shape)

m =np.array([np.arange(3),np.arange(3) ,np.arange(3)])
print(m.shape)
print(m[0,0])

t =np.arange(5 ,dtype =float)
print(t)
t =np.arange(5 ,dtype =complex)
print(t)
print(t.dtype)

dt = np.dtype([('name', np.str, 40), ('numitems', np.int32), ('price', np.float32)])
print(dt)
itemz = np.array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=dt)
print(itemz)
print(itemz[1])

print("---")

b = np.arange(24).reshape(2,3,4)
print(b)
print(b[0,1])
print(b[0,1,1])
print(b[0 ,1 ,1:3])
print(b[0 ,1 ,::2])
print(b[0 ,: ,-1])
print(b[0,:,1:3])

print("---")

print(b.ravel())
print(b)
#reshape并不改变b，而是返回b的改变形态
b.reshape(3 ,8)
print(b)
b.resize((3 ,8))
print(b)
b.shape =(4 ,6)
print(b)

print("---")

a =b.reshape(3 ,8)
print(b ==a)
b.shape =(3 ,8)
print(a ==b)


print("---")
print(b.reshape(2 ,3 ,4).ndim)
print(b.size)
#单个元素的内存字节数
print(b.itemsize)
print(b.T)

#随机[0,1.csv)的随机浮点数
print(np.random.rand(3 ,2))
#满足正态分布的随机浮点数
print(np.random.randn(3 ,2))
#规定区间内随机整数
print(np.random.randint(0,7,[8,7]))