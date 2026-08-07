class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        index = -1
        product = 1
        
        if 0 in nums:
            index = [i for i,x in enumerate(nums) if x==0]
            if len(index)>1:
                return res
            [product := product * num for num in nums if num!=0]
            res[index[0]]= product
            return res
            
        [product := product * num for num in nums]
        print (product)
        for i,num in enumerate(nums):
            res[i] = product//num
        return res

        