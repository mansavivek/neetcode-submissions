class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        countsArr = []
        if len(nums)==0:
            return 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                count+=1
            if nums[i]==nums[i+1]:
                continue
            if nums[i+1] - nums[i] > 1:
                countsArr.append(count)
                # if count!=1:
                #     prevCount = count
                count = 1
        countsArr.append(count)
        print(nums, count, countsArr)
        # if prevCount>count:
        #     return prevCount
        return max(countsArr) 
        