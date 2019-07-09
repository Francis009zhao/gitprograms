class Solution(object):
    def twoSum(self, nums:[int], target:int):
        size = len(nums)
        for i, m in enumerate(nums):
            j = i + 1
            while j < size:
                if target == (m + nums[j]):
                    return [i, j]
                else:
                    j += 1



print(Solution().twoSum([2.9,2,7,11,15],9))
'''
def tow_sum_with_dict2(nums: List[int], target: int) -> List[int]:
    _dict = {}
    for i, m in enumerate(nums):
        if _dict.get(target - m) is not None:
            return [i, _dict.get(target - m)]
        _dict[m] = i


'''