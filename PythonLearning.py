#创建列表

'''
a = [x for x in range(1,5)]
print(a)



import time

time.clock()

b = [x*2 for x in range(1,11)]
print(b)
costtime =time.clock()
print(costtime)


b = [x for x in range(1,100) if x%2==0]
print(b)




a = [10,20,30]

print(id(a))

b = ['asd']

a.append(50)

a.extend(b)

a.insert(1,'sdf')

print(a,id(a))

'''
'''

a=[10,20,30,40,50,60,20,30,6,76,54]
b=a.index[20,0]
print(b)

'''

a = {'name':'gaoqi','age':22,'job':'programer'}

b={'name':'gaoqis','money':32000,'work':'programer'}

print(a.update(b))

































































