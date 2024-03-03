class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        new_nums = dict(enumerate(nums))
        target_indices = [key for (key, value) in new_nums.items() if value == target]
        return target_indices