class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        if not nums:
            return 0

        for num in nums:
            currLength = 1
            if num - 1 in numSet:
                continue
            else:
                nextNum = num + 1
                while nextNum in numSet:
                    currLength += 1
                    nextNum += 1

            maxLength = max(maxLength, currLength)
        return maxLength
