class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        wMax = 0
        for i in range(k):
            if nums[wMax] <= nums[i]:
                wMax = i
        result.append(nums[wMax])

        for i in range(k, len(nums)):
            new = nums[i]
            if new >= nums[wMax]:
                wMax = i
            elif new < nums[wMax]:
                if i-k == wMax:
                    wMax = i-k+1
                    for j in range(i-k+1, i+1):
                        if nums[wMax] <= nums[j]:
                            wMax = j
            result.append(nums[wMax])
        return result