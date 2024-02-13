import collections

class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0 for _ in range(26)]
            for char in s:
                count[ord(char) - ord('a')] += 1

            ans[tuple(count)].append(s)
        return ans.values()


'''
Time Complexity: O(kN) where N is the number of strings and k is the character count of each string.
Space Complexity: O(kN) = total amount of information stored would be kN.
'''