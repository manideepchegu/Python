class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n==1:
            return [[],[nums[0]]]
        r = self.subsets(nums[:n-1])
        s = []
        for e in r:
            s.append(e+[nums[n-1]])
        return r+s 
