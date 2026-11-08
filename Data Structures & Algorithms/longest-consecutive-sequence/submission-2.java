class Solution {
    public int longestConsecutive(int[] nums) {
                Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int longest = 0;
        for (int num : nums) {
            int streak = 0, curr = num;
            while(numSet.contains(curr)) {
                streak++;
                curr++;
            }
            longest = Math.max(longest, streak);
        }

        return longest;
    }
}
