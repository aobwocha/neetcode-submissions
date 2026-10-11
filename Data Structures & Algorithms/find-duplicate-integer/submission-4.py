class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow_v2 = 0
        while True:
            slow = nums[slow]
            slow_v2 = nums[slow_v2]
            if slow == slow_v2:
                return slow