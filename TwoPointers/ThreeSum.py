class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):
            l, r = i + 1, len(nums)-1

            # if curr num is the same as the prev one, skip to not create duplicates
            if nums[i] == nums[i-1] and i > 0:
                continue

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if (total == 0):
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                if total < 0:
                    l += 1
                if total > 0:
                    r -= 1
        return res

'''
Time complexity
O(N2) since two nested for loops.

'''