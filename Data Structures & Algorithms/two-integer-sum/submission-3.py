class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap ={}
        for i, n in enumerate(nums):
            # diff = target - n
            if target - n in hmap:
                return[hmap[target - n],i]
            hmap[n] = i