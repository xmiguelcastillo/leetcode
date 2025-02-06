class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)

        for i in range(len(nums)):
            count[nums[i]] += 1

        for key, value in count.items():
            if value != 1:
                return True
        return False
