"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1

"""

class Solution(object):
    def singleNumber(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #

        dict_tmp = {}
        for i in nums:
            if i in dict_tmp:
                dict_tmp[i] += 1
            else:
                dict_tmp[i] = 1
        list_tmp = []
        for j in dict_tmp:
            if dict_tmp[j] == 1:
                list_tmp.append(j)
        print(list_tmp)





print(Solution().singleNumber([2,2,1,3,5,5]))







