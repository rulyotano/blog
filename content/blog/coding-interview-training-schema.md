---
title: My Coding Interview Training Schema
date: '2026-05-14T00:00:00+00:00'
draft: false
author: Raul
tags:
- Blog
- Algorithms
- Career
- Interview
url: /blog/article/coding-interview-training-schema
cover:
  image: /images/coding-interview-training-schema/cover.png
  alt: Coding Interview Training Schema — 6 steps and 15 patterns
  relative: false
---

Coding interviews are not just about solving problems — they measure your communication, thinking process, and problem-solving skills, from gathering requirements all the way to testing and complexity analysis. If you only have one or two weeks to prepare, this is a short but effective preparation schema focused on training those skills, not memorizing thousands of problems.

## Interview Schema

During preparation, every problem you solve — even if you already know the solution or have solved it before — practice speaking out loud. If you can't speak out loud, simulate it in your head and walk through your reasoning as if you were talking to an interviewer.

Write comments as placeholders at the start so you never forget a step:

```
/*
# 1. Understand the problem
# 2. Find edge cases
# 3. Propose several solutions
# 4. Implementation
# 5. Testing
# 6. Analysis
*/
```

### 1. Understand the Problem

Ask clarification questions, even for things that seem obvious. It has happened to many people — myself included — that after starting to implement, they realize the whole approach was wrong because of a misunderstood requirement.

At the end of this step, summarize what you understood and confirm it with the interviewer. This builds trust and prevents wasted effort.

### 2. Find Edge Cases

Think through any boundary or corner case before writing code:

- **Numbers:** 0, negative, very large integers
- **Arrays:** null, empty, fewer items than required
- **Strings:** null, empty, very short, special characters
- **Matrices:** null, empty, irregular dimensions
- **Trees / Linked Lists:** null root, single node, circular structures
- **Problem-specific:** values that break your invariants

### 3. Propose Several Solutions

This is the most critical step. Always start with the brute force or the first idea that comes to mind — even if you already know a better one. It shows structured thinking.

Then look for improvements:
- Can you reduce time complexity with a different data structure?
- Can you eliminate redundant passes?
- Can you trade memory for speed or vice versa?

If you're stuck, ask for a hint. It is not a failure — it shows collaboration. Use concrete examples and test cases to unlock your thinking; different inputs often reveal the pattern.

Pick the best solution you found. If it is not optimal, explain why and what the optimal would look like.

### 4. Implementation

Write the code. If you get stuck, go back to your test cases and trace through the algorithm step by step.

Keep talking during implementation. Explain what you are doing and why. If you need a quiet moment to think, say so — *"Give me a moment to think through this."* Silence without warning feels awkward to an interviewer.

> The interview does not just measure problem-solving skills — it measures communication and the ability to work with others.

Training on a whiteboard or on LeetCode's editor (no autocomplete) is especially useful, as it mimics the actual interview environment.

### 5. Testing

Finishing the code does not mean you are done. Run through a few test cases manually:

1. A normal, representative case
2. One or two of the edge cases you identified earlier
3. Trace through your code line by line — do not just read it

Catching your own bugs before the interviewer does makes a strong impression.

### 6. Analysis

Discuss your solution:

- **Time complexity:** What is the Big O? Why?
- **Space complexity:** What extra memory are you using?
- **Is it optimal?** If not, what would the optimal approach look like and what are the trade-offs?

---

## Training

You cannot and should not try to solve every problem on LeetCode or HackerRank. Random practice without structure is hard to scale, and you will never get a representative sample of problem types. The good news: free resources are enough for most interviews.

### LeetCode Top Interview Questions

Start with LeetCode's [Top Interview Questions](https://leetcode.com/explore/featured/card/top-interview-questions-easy/) list, available for free under the Explore section. It is curated, well-balanced, and a great baseline.

Always apply the interview schema above — even for problems you know. If you force the habit in practice, it will come naturally in the actual interview.

### Train by Pattern

Inspired by this [YouTube video](https://www.youtube.com/watch?v=DjYZk8nrXVY&list=PLCYEYz3DtQjzNG-wmnxoQQJ9W3zUb3Pte&index=2), the most effective way to prepare is to train on specific patterns rather than random problems. Once you recognize a pattern, a whole class of problems becomes familiar.

#### 1. [Prefix Sum](https://en.wikipedia.org/wiki/Prefix_sum)

Precompute cumulative sums for O(1) range queries.

- 303 [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
- 525 [Contiguous Array](https://leetcode.com/problems/contiguous-array/)
- 560 [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

#### 2. [Two Pointers](https://www.geeksforgeeks.org/dsa/two-pointers-technique/)

Use two indices moving toward or away from each other to avoid nested loops.

- 167 [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- 15 [3Sum](https://leetcode.com/problems/3sum/)
- 11 [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

#### 3. [Sliding Window](https://www.geeksforgeeks.org/dsa/window-sliding-technique/)

Maintain a dynamic window over an array or string to find subarrays/substrings that meet a condition.

- 643 [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
- 3 [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- 76 [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

#### 4. [Fast & Slow Pointers](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews/blob/main/%E2%9C%85%20%20Pattern%2003:%20Fast%20%26%20Slow%20pointers.md)

Two pointers moving at different speeds — useful for cycle detection and finding midpoints in linked lists.

- 141 [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- 202 [Happy Number](https://leetcode.com/problems/happy-number/)
- 287 [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

#### 5. Linked List In-Place Reversal

Reverse a linked list or a portion of it without extra space.

- 206 [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- 92 [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
- 24 [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

#### 6. Monotonic Stack

Use a stack that maintains elements in monotone order to find next greater/smaller elements efficiently.

- 739 [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
- 496 [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
- 84 [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

#### 7. Top K Elements

Use a heap to efficiently track the K largest or smallest elements without full sorting.

- 215 [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- 347 [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- 373 [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

#### 8. Overlapping Intervals

Sort intervals and merge or insert by comparing start/end boundaries.

- 56 [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- 57 [Insert Interval](https://leetcode.com/problems/insert-interval/)
- 435 [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- 253 [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

#### 9. Modified Binary Search

Apply binary search beyond sorted arrays — on rotated arrays, answer spaces, or monotone functions.

- 33 [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- 153 [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- 240 [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

> others

- 704 [Binary Search](https://leetcode.com/problems/binary-search/)
- 162 [Find Peak Element](https://leetcode.com/problems/find-peak-element/)

#### 10. Binary Tree Traversal

Master all traversal orders: inorder, preorder, postorder, and level-order (BFS).

- 257 [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)
- 230 [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- 124 [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- 107 [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
  
> others

- 94 [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- 104 [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- 102 [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

#### 11. Depth-First Search (DFS)

Explore as deep as possible before backtracking — applies to trees and graphs.

- 133 [Clone Graph](https://leetcode.com/problems/clone-graph/)
- 113 [Path Sum II](https://leetcode.com/problems/path-sum-ii/)
- 210 [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

> others

- 112 [Path Sum](https://leetcode.com/problems/path-sum/)
- 200 [Number of Islands](https://leetcode.com/problems/number-of-islands/)
- 695 [Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

#### 12. Breadth-First Search (BFS)

Explore level by level — ideal for shortest path and layer-by-layer problems.

- 102 [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- 994 [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- 127 [Word Ladder](https://leetcode.com/problems/word-ladder/)

#### 13. Matrix Traversal

Apply DFS or BFS on a 2D grid, treating each cell as a node.

- 733 [Flood Fill](https://leetcode.com/problems/flood-fill/)
- 130 [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
- 200 [Number of Islands](https://leetcode.com/problems/number-of-islands/)

> others

- 79 [Word Search](https://leetcode.com/problems/word-search/)

#### 14. Backtracking

Explore all possible paths by building candidates incrementally and pruning invalid ones.

- 78 [Subsets](https://leetcode.com/problems/subsets/)
- 46 [Permutations](https://leetcode.com/problems/permutations/)
- 51 [N-Queens](https://leetcode.com/problems/n-queens/)

> others

- 39 [Combination Sum](https://leetcode.com/problems/combination-sum/)

#### 15. Dynamic Programming

Break problems into overlapping subproblems, store results to avoid recomputation.

- 70 [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- 322 [Coin Change](https://leetcode.com/problems/coin-change/)
- 300 [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- 416 [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- 1143 [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- 312 [Burst Balloons](https://leetcode.com/problems/burst-balloons/)

---

## Summary

Following this schema consistently during practice is what builds the muscle memory needed for actual interviews. Harder roles — senior positions or top-tier companies — may require going deeper into each pattern and exploring advanced topics.

If you want to go further, these books are highly recommended:

- [Cracking the Coding Interview](https://www.crackingthecodinginterview.com/) by Gayle Laakmann McDowell — the classic reference for interview preparation
- [Introduction to Algorithms (CLRS)](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/) — rigorous algorithms and data structures reference
