class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]*len(arr)
        for i in range(len(arr)):
            rightMax = -1
            for j in range(i+1, len(arr)):
                rightMax = max(arr[j], rightMax)
            ans[i] = rightMax
        return ans
        