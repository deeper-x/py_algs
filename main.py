from typing import List
import two_sum


if __name__ == "__main__":
    # two_sum
    s: two_sum.Solution = two_sum.Solution()
    res: List[int] = s.twoSum([1, 4, 5, 6, 7], 5)
    print(res)
