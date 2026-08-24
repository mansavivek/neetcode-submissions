class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        ans =[]
        for i in nums:
            if i != val:
                ans.append(i)
                count+=1
        for i in range(count):
            nums[i] = ans[i]
        return count
        