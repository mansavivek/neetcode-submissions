class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = [];
        for i in nums:
            print(i)
            if i in dictionary:
                return True
            else:
                dictionary.append(i)
        return False
        