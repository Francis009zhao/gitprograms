#
# N = eval(input())
#
# for i in range(N):
#     words = list(input())
#     k = 0
#
#     for j in range(len(words)):
#         # print(j)
#         words[k] = words[j]
#         k += 1
#
#         if k >= 3 and words[k - 3] == words[k - 2] and words[k - 2] == words[k - 1]:
#             k -= 1
#         if k >= 4 and words[k - 4] == words[k - 3] and words[k - 1] == words[k - 2]:
#             k -= 1
#     print(''.join(words[:k]))
#

n = int(input())
while n > 0:
    s = input()
    res = []
    for e in s:
        if len(res) < 2:
            res.append(e)
            continue
        if len(res) >= 2:
            if e == res[-1] and e == res[-2]:
                continue
        if len(res) >= 3:
            if e == res[-1] and res[-2] == res[-3]:
                continue
        res.append(e)
    print("".join(res))
    n -= 1


