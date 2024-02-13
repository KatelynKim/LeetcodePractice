class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary where every time a new key is added, its default value is set to 0.
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1

        frequencies = [ [] for _ in range(len(nums) + 1)]

        for num, count in counter.items():
            frequencies[count].append(num)
        ans = []

        # Iterate through the frequencies array in reverse (high -> low freq).
        for i in range(len(frequencies)-1, -1, -1):
            for j in range(len(frequencies[i])):
                ans.append(frequencies[i][j])
                if (len(ans) == k):
                    return ans
        return ans

'''
Time Complexity: O(N)
Space Complexity: O(N)
'''



