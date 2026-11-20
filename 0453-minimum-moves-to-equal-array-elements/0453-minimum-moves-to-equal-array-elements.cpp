class Solution {
public:
    int minMoves(vector<int>& nums) {
        long long sum = 0;
        int minVal = nums[0];

        for (int x : nums) {
            sum += x;
            minVal = min(minVal, x);
        }

        return (int)(sum - (long long)nums.size() * minVal);
    }
};