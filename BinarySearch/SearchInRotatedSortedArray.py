class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # if mid is part of the left sorted array:
            if nums[mid] > nums[r]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # if mid is part of the right sorted array
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


