class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        i = 0;
        j = len(heights)-1
        while i<j:
            capacity = min(heights[i],heights[j]) * (j-i)
            if capacity > max:
                max = capacity
            if heights[i]>heights[j]:
                j -= 1
            else:
                i += 1
        return max
        