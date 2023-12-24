class Solution {
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
      int m = nums1.length;
      int n = nums2.length;
      int[] nums = new int[m + n];
      double med;

      int p1 = 0, p2 = 0, p = 0;
      while (p1 < m && p2 < n) {
          if (nums1[p1] <= nums2[p2]) {
              nums[p] = nums1[p1];
              p1++;
          } else {
              nums[p] = nums2[p2];
              p2++;
          }
          p++;
      }
      if (p1 != m) { //nums1 has remaining elements
          for (int count = p1; count < m; count++) {
              nums[p] = nums1[count];
              p++;
          }
      } else { // nums2 has remaining elements
          for (int count = p2; count <n; count++) {
              nums[p] = nums2[count];
              p++;
          }
      }

      // MID : nums is a sorted array with all items  
      int midIndex = (m + n) / 2;

      if ((m + n) % 2 == 0) { // even length
          med = (double) (nums[midIndex] + nums[midIndex - 1]) / 2;
      } else {
          med = nums[midIndex];
      }
      return med;
  }
}