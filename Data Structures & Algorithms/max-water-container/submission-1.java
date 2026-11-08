class Solution {
    public int maxArea(int[] bars) {
        int result = 0;

        int leftPointer = 0;
        int rightPointer = bars.length - 1;

        while (leftPointer < rightPointer) {
            int lowest = Math.min(bars[leftPointer], bars[rightPointer]);
            result = Math.max(result, (Math.min(bars[leftPointer], bars[rightPointer])) * (rightPointer - leftPointer));

            if (bars[leftPointer] < bars[rightPointer]) {
                leftPointer++;
            } else {
                rightPointer--;
            }
        }

        return result;
    }
}
