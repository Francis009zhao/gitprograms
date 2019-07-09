"""

给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：

区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:



[6] = 6 * 6 = 36;

[2] = 2 * 2 = 4;

[1] = 1 * 1 = 1;

[6,2] = 2 * 8 = 16;

[2,1] = 1 * 3 = 3;

[6, 2, 1] = 1 * 9 = 9;



从上述计算可见选定区间 [6] ，计算值为 36， 则程序输出为 36。

区间内的所有数字都在[0, 100]的范围内;
输入例子1:
3
6 2 1

输出例子1:
36
"""
# import sys
#
# N = int(input())
# shuzu = []
# for i in range(N):
#     shuzu.append(input())
# shuzu.sort(reverse=True)
# print(shuzu)
#
# maxs = []
# for i in range(N):
#     maxs.append(shuzu[i] * shuzu[i])
#     maxs.append(shuzu[-1] * sum(shuzu[:-1]))
#
# print(maxs.sort(reverse=False)[0])

n=int(input())
arr=[int(x) for x in input().split()]
print(arr)
stack = []
arr.append(0)
print(arr)
result = 0
i = 0
presum = []
tempsum = 0
while i<len(arr):
    if not stack or arr[i]>=stack[-1]:
        presum.append(tempsum)
        tempsum = 0
        stack.append(arr[i])
        i+=1
    else:
        temp = stack.pop(-1)
        tempsum+=(temp+presum.pop())
        result = max(tempsum*temp,result)
print(result)