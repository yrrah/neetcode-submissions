class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            split = (left + right) // 2

            if nums[split] == target:
                return split

            if nums[split] < target:
                left = split + 1

            if nums[split] > target:
                right = split - 1

        return -1