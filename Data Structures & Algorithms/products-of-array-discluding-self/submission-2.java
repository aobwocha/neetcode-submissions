class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        int[] rightTracker = new int[nums.length];

        int rightTotal = 1;
        for (int i = nums.length - 1; i > -1; i--) {
            rightTracker[i] = rightTotal;
            rightTotal *= nums[i];
        }
        
        int leftTotal = 1;
        for (int i = 0; i < nums.length; i++) {
            result[i] = leftTotal * rightTracker[i];
            leftTotal *= nums[i];
        }

        return result;
    }
}  
