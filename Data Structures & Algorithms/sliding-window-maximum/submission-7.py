class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        l,r = 0, k
        wMax = max(nums[l:r])
        res = [wMax]
        while r < len(nums):
            if nums[l] == wMax:
                wMax = max(nums[l+1: r])
            if nums[r] >= wMax:
                wMax = nums[r]
            l += 1
            r += 1
            res.append(wMax)
        return res
        