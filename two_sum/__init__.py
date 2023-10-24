from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res: List[int] = []
        lns_inner: int = len(nums)
        lns: int = lns_inner - 1

        for i in range(lns):
            for j in range(i+1, lns_inner):
                if nums[i] + nums[j] == target:
                    res = [i, j]
                    return res

        # empty return
        return res

