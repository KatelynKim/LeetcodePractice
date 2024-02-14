class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        postfix = 1
        prefixArr = []
        postfixArr = []

        # append prefix first. For the first element in nums, the prefix would be 1 because the first element
        # does not have any preceding numbers.
        for i in range(len(nums)):
            prefixArr.append(prefix)
            prefix *= nums[i]

        # append postfix first. For the last element in nums, the postfix would be 1 because the last element
        # does not have any number that comes after it.
        for i in range(len(prefixArr)-1, -1, -1):
            postfixArr.append(postfix)
            postfix *= nums[i]

        for i in range(len(prefixArr)):
            prefixArr[i] *= postfixArr[len(prefixArr)-1-i]

        return prefixArr
