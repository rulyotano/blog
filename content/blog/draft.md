---
date: '2026-05-14T22:07:11+00:00'
draft: true
---

# My Coding Interview Tarining Schema

## Intro
- Explain how this schema would work for train for most of coding interviews whiteboards hands 1-1 iterviews
- Explain most important is way of communication, thinking process, solving problem skills (from gathering requirements to testing and analysis), over just completing the challenge.
- Im going to give a short preparation process, to train main things to focus, just a couple of problems

## Interview schema
- During preparation, every problem you solve, even if you know the solution, or if you've already solved it. Try to speak in a loud voice, or if you can't, just try to simulate you are talking in your head, and explain everything you have in mind.
- Write in comments every step, as a place holder, to not forget anything. Even in the actual interview you can do so.
-  Steps:

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

### Understand the problem

- After finishing this step, you should get a real understanding of the problem
- Ask any clarification questions, even if it seems obvious.
- Happened to me that after Im implementating I realize the implementation is wrong because I didn't understand the problem
- At the end, write a summary for the interviewer to check if you got it correctly

### Find edge cases
- Try to find any edge case:
  - Input numbers: 0, negative, long int
  - Arrays: null, empty, fewer items than required
  - Strings: null, empty, fewer chars, weird characters
  - Matrix: empty, null, fewer rows or cols
  - TreeNodes (objects): null, roots, ...
  - problematic values depending on the problem specification

### Propose several solutions
- This is the most critical step
- Find the brute force, or the first idea that comes to your mind (try to do it always, even if you know the best optimal solution)
- Then find a better one, or improve brute force
- If nothing comes to your mind, just ask for tips or help
- Pick the better one, and if you can't find the optimal solution, explain why it is suboptimal
- Support your self generating test cases, and can ask for examples to the interviewer. Looking at different input examples can open your mind and help you find the solution.

### Implementation
- Write the code to solve the problem
- If I get stuck, again, support in test cases and go step by step, trying to debug the algorithm.
- Explain in a loud you though process, what are you doing. Always talks during the interview process. If you need a moment to think, just mention it.
  > Remember, the interview is not just to measure problem-solving skills, but also the communication skills and teamwork.
- To train, I recommend doing it on a whiteboard. For example, Leetcode has no autocompletion, so it is good for it.

### Testing
- After finishing coding, you are not finished
- Get a couple of test cases, and debug.

### Analysis
- Discuss the solution. Are there better solutions, or is it optimal?
- What's the time complexity?
- What's the memory complexity?

## Training
- You cannot solve the thousands of problems from LeetCode or HackerRank.
- Also, solving random problems also won't work; it is hard to take a representative number of kinds of problems.
- I think paying is not necessarily needed; the free resources should be enough for most of the interviews.
- That's why I recommend...

### LeetCode Top Interview Questions
- I recommend going through all the problems from LeetCode's [Top Interview Questions](https://leetcode.com/explore/featured/card/top-interview-questions-easy/) list.
- It is under the Explore section
- It is free
- Always try to follow the Interview Schema suggested before. If you force yourself to do it in practice, your chances of doing it in the actual interview are going to be higher.
- If some of the problems are locked, you can always try to find them in other sites, the same with the answers and best solutions.

### Train Kinds based on kind of problems
- Found this idea in this [Youtube Video](https://www.youtube.com/watch?v=DjYZk8nrXVY&list=PLCYEYz3DtQjzNG-wmnxoQQJ9W3zUb3Pte&index=2)
- Train for specific kind or pattern of problems

#### 1. [Prefix Sum](https://en.wikipedia.org/wiki/Prefix_sum)
- 303. [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
- 525. [Contiguous Array](https://leetcode.com/problems/contiguous-array/)
- 560. [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/)

#### 2. [Two Pointers](https://www.geeksforgeeks.org/dsa/two-pointers-technique/)
- 167. [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- 15. [3Sum](https://leetcode.com/problems/3sum/)
- 11. [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)




