motocycles = ['honda','yamaha','suzuki']

# 修改元素
motocycles[0] = "ducati"
print(motocycles)

# 元素添加到末尾
motocycles.append("honda")
print(motocycles)

# 元素插入
motocycles.insert(0, "anyName")
print(motocycles)

#  del 删除元素
del motocycles[0]
print(motocycles)


# pop 删除，栈顶出栈
poped_motocycle = motocycles.pop()
print(motocycles)
print(poped_motocycle)

# pop 删除，任意位置出栈
poped_motocycle1 = motocycles.pop(1)
print(motocycles)
print(poped_motocycle1)


# remove 根据值删除元素,只删除第一个发现的，非循环删除

motocycles.remove("suzuki")
print(motocycles)