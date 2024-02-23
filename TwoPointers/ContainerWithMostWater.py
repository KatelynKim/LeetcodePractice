class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxArea = 0
        l, r = 0, len(height)-1

        while l < r :
            if height[l] >= height[r]:
                maxArea = max(maxArea, (r-l)*height[r])
                r -= 1
            else:
                maxArea = max(maxArea, (r-l)*height[l])
                l += 1

        return maxArea

'''
Time Complexity - O(N)
'''