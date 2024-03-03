class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for number in nums:
            count = 0
            for num in range(len(nums)):
                if nums[num] < number:
                    count += 1 
            output.append(count)
        return output
