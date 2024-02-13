class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = [0 for _ in range(26)]
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1

        for count in counter:
            if count != 0:
                return False
        return True


'''
Time Complexity: O(N)
Space Complexity: O(1) -> Table size remains constant regardless of N.

Alternately, you could just return sorted(s) == sorted(t), but sorting is O(Nlog(N))

'''


