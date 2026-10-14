class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        
        sorted_nums = sorted(nums)

        last_num = sorted_nums[0]
        for num in sorted_nums[1:]:
            if last_num == num:
                return True
            last_num = num

        return False
        