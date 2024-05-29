class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        res = []
        n = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                continue
            else:
                nums[i] *= 2
                nums[i+1] = 0

        for j in nums:
            if j != 0:
                res.append(j)
            else:
                n+=1
        return res+[0]*n