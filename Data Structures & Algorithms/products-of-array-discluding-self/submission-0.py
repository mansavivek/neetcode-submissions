class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        index = -1
        product = 1
        if 0 in nums:
            res = [0]*len(nums)
            index = [i for i,x in enumerate(nums) if x==0]
            if len(index)>1:
                return res
            elif len(index)==1:
                [product := product * num for num in nums if num!=0]
                res[index[0]]= product
                return res
        [product := product * num for num in nums]
        print (product)
        for i in nums:
            res.append(product//i)
        return res

        