class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_num = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    min_num = nums[j]
                    nums[i], nums[j] = nums[j], nums[i]
