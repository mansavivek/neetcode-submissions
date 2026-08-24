class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxA = 0
        stack = []
        for i in range(0, n+1):
            while stack and (i==n or heights[i]<=heights[stack[-1]]):
                h = heights[stack.pop()]
                width = i if not stack else (i - stack[-1] - 1)
                maxA = max(maxA, h*width)
            stack.append(i)
        return maxA