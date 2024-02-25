class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        hashmap = {}
        maxLength = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)

            # while the current substring minus the count of the most freuqent character is greater than
            # k (the max num of replaceable chars), shift the left pointer.
            while (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r-l+1)


        return maxLength







