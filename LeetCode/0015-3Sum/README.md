# [15. 3Sum](https://leetcode.com/problems/3sum/)

## 题目

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

```c
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

## 題目大意

給定一個數組，要求在這個數組中找出 3 個數之和為 0 的所有組合。

## 解題思路

先給數組排序，確定一個數，枚舉另外兩個數，注意去重，如果第一個數已經是正數了，則可以退出