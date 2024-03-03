# Leetcode Practice

One leetcode problem a day goes a long way...
But even better is two or three a day at medium+ difficulties 🤪

### March progress

| Dates | Completion | Notes |
|-------|---------|----------|
|  1    | &#10004;| Lowest common ancestors - LCA is where the split occurs. |
|  2    | &#10004;| Validate BST - Update max and min range for left and right subtrees.|


### February progress (26 solved in total)

| Dates | Completion | Notes |
|-------|---------|----------|
|  12   | &#10004;|
|  13   | &#10004;|
|  14   | &#10004;| Longest consecutive sequence - Check if the curr num is the start of a sequence.
|  15   |         |
|  16   |         |
|  17   |         |
|  18   |         |
|  19   |         |
|  20   |         |
|  21   |&#10004; | - Encode and decode strings - Encode strings by adding the count of chars in each string followed by a symbol to mark it as the end of count and the actual string itself. Decode by iterating through each char in the string until the next symbol mark to determine the count, then splice the string appropriately.<br> - Valid palindrome - Have l and r pointers starting at both ends of the string. Skip over non-alphanumerical letters. Stop the loop when l > r. <strong>Consider an edge case all letters are non-alphanumeric.</strong>
|  22   |&#10004; | - ThreeSum - avoid adding duplicates by skipping if 1) curr indexed pivot is identical to the prev pivot; and 2) nums[l] == nums[l-1].<br> - Container with most water - greedy problem <br> - Best time to sell stocks
|  23   |         |
|  24   |&#10004; | - Longest substring without repeating chars: shift left pointer (adjust window) when a char is repeated. <br> - Longest repeating character replacement - Window length should be no more than the count of most freq char in the window + k. Shrink the window as needed to meet this condition. <br> - Valid parenthesis
|  25   |         |
|  26   |&#10004; | - Find minimum in rotated sorted array <br> - Search in rotated sorted array <br> - Merge two sorted lists <br> - Reverse linked list <br> - Reorder list - when splitting the list in the middle, make sure the last element in the first linked list points to nothing.
|  27   |         |
|  28   |         |
|  29   |&#10004; | - Remove nth node from end of list - the right pointer will reach the end of list n steps earlier than the left pointer. <br/> - Linked list cycle - fast pointer will always eventually meet the slow pointer because in each iteration of loop, the distance between them is reduced by 1 (slow pointer moves away from fast pointer by 1, but faster pointer them moves toward it by 2, resulting in the gap between the two reduced by 1. This means time complexity of O(N)) <br> - Invert binary tree - DFS <br/> - Maximum depth of binary tree - the depth of curr node is the max between the left and right children's depth + 1.<br>- Is same tree - dfs <br> - Subtree of another tree - Extension of Is Same Tree
