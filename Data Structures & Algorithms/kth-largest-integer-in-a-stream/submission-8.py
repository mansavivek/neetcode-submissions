class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums
        self.arr.sort()

    def add(self, val: int) -> int:
        if len(self.arr)==0 or self.arr[len(self.arr)-1]<=val:
            self.arr.append(val)
        else:
            for i in range(len(self.arr)):
                if self.arr[i]>val:
                    self.arr.insert(i, val)
                    break
        return self.arr[len(self.arr)-self.k]
