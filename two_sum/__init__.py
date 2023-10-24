from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res: List[int] = []
        founded: bool = False

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res = [i, j]
                    founded = True

            if founded:
                return res

        return res
