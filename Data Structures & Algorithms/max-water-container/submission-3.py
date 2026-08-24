class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxC = 0
        i = 0;
        j = len(heights)-1
        while i<j:
            capacity = min(heights[i],heights[j]) * (j-i)
            maxC = max(maxC,capacity)
            if heights[i]>heights[j]:
                j -= 1
            else:
                i += 1
        return maxC
        