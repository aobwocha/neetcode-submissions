class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow_V2 = 0
        while True:
            slow = nums[slow]
            slow_V2 = nums[slow_V2]
            if slow == slow_V2:
                return slow