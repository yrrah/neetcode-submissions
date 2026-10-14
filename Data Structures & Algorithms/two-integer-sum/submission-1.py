class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pair of indicies that satisfy
        # therefore there can be no duplicates in nums

        values = {}

        for i in range(len(nums)):
            values[nums[i]] = i

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in values and values[remainder] != i:
                return [i, values[remainder]]
        
        return []
        