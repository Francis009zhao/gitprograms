"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

"""
# def cmp_to_key(mycmp):
#     """Convert a cmp= function into a key= function"""
#     class K(object):
#         __slots__ = ['obj']
#         def __init__(self, obj):
#             self.obj = obj
#         def __lt__(self, other):
#             return mycmp(self.obj, other.obj) < 0
#         def __gt__(self, other):
#             return mycmp(self.obj, other.obj) > 0
#         def __eq__(self, other):
#             return mycmp(self.obj, other.obj) == 0
#         def __le__(self, other):
#             return mycmp(self.obj, other.obj) <= 0
#         def __ge__(self, other):
#             return mycmp(self.obj, other.obj) >= 0
#         __hash__ = None
#     return K
#
class Solution(object):
    def largestNumber(self,nums):
        if max(nums) == 0:
            return '0'
        nums = list(map(str, nums))

        from functools import cmp_to_key
        nums.sort(key=cmp_to_key(lambda a, b: int(a + b) - int(b + a)), reverse=True)
        print(nums)
        return ''.join(nums)



        # nums = [int(x) for x in input().split()]
        # largest = []
        # for i in range(len(nums)):
        #     largest.append(nums[i])
        # print(largest)
        # print(nums.sort())

print(Solution().largestNumber([10,2]))

#
# class Solution(object):
#     def largestNumber(self,nums):
#         n = len(nums)
#         for i in range(n):
#             for j in range(n - i - 1):
#                 temp_1 = str(nums[j])
#                 temp_2 = str(nums[j + 1])
#                 if (int(temp_1 + temp_2) < int(temp_2 + temp_1)):
#                     temp = nums[j]
#                     nums[j] = nums[j + 1]
#                     nums[j + 1] = temp
#         output = ''
#         for i in nums:
#             output = output + str(i)
#         return str(int(output))
#
#
#
#         # if max(nums) == 0:
#         #     return '0'
#         # nums = list(map(str, nums))
#         # print(nums)
#         #
#         # from functools import cmp_to_key
#         # nums.sort(key=cmp_to_key(lambda a, b: int(a + b) - int(b + a)), reverse=True)
#         # return ''.join(nums)
#
#
#         # nums = [int(x) for x in input().split()]
#         # largest = []
#         # for i in range(len(nums)):
#         #     largest.append(nums[i])
#         # print(largest)
#         # print(nums.sort())
#
# print(Solution().largestNumber([10,2,6,9,70]))