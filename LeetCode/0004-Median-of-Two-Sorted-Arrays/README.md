# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)


## 题目

There are two sorted arrays **nums1** and **nums2** of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume **nums1** and **nums2** cannot be both empty.

**Example 1:**

    nums1 = [1, 3]
    nums2 = [2]
    
    The median is 2.0

**Example 2:**

    nums1 = [1, 2]
    nums2 = [3, 4]
    
    The median is (2 + 3)/2 = 2.5


## 题目大意


給定兩個大小為 m 和 n 的有序數組 nums1 和 nums2。

請你找出這兩個有序數組的中位數，並且要求算法的時間複雜度為 O(log(m + n))。

你可以假設 nums1 和 nums2 不會同時為空。



## 解题思路


- 給出兩個有序數組，要求找出這兩個數組合併以後的有序數組中的中位數。要求時間複雜度為 O(log (m+n))。
- 這一題最容易想到的辦法是把兩個數組合併，然後取出中位數。但是合併有序數組的操作是 `O(max(n,m))` 的，不符合題意。看到題目給的 `log` 的時間複雜度，很容易聯想到二分搜索。
- 由於要找到最終合併以後數組的中位數，兩個數組的總大小也知道，所以中間這個位置也是知道的。只需要二分搜索一個數組中切分的位置，另一個數組中切分的位置也能得到。為了使得時間複雜度最小，所以二分搜索兩個數組中長度較小的那個數組。
- 關鍵的問題是如何切分數組 1 和數組 2 。其實就是如何切分數組 1 。先隨便二分產生一個 `midA`，切分的線何時算滿足了中位數的條件呢？即，線左邊的數都小於右邊的數，即，`nums1[midA-1] ≤ nums2[midB] && nums2[midB-1] ≤ nums1[midA]` 。如果這些條件都不滿足，切分線就需要調整。如果 `nums1[midA] < nums2[midB-1]`，說明 `midA` 這條線劃分出來左邊的數小了，切分線應該右移；如果 `nums1[midA-1] > nums2[midB]`，說明 midA 這條線劃分出來左邊的數大了，切分線應該左移。經過多次調整以後，切分線總能找到滿足條件的解。
- 假設現在找到了切分的兩條線了，`數組 1` 在切分線兩邊的下標分別是 `midA - 1` 和 `midA`。`數組 2` 在切分線兩邊的下標分別是 `midB - 1` 和 `midB`。最終合併成最終數組，如果數組長度是奇數，那麼中位數就是 `max(nums1[midA-1], nums2[midB-1])`。如果數組長度是偶數，那麼中間位置的兩個數依次是：`max(nums1[midA-1], nums2[midB-1])` 和 `min(nums1[midA], nums2[midB])`，那麼中位數就是 `(max(nums1[midA-1], nums2[midB-1]) + min(nums1[midA], nums2[midB])) / 2`。圖示見下圖：

    ![](https://img.halfrost.com/Leetcode/leetcode_4.png)
