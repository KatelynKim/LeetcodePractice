class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            # Here, I didn't realize to add the check for l < r since we don't want to
            # l to go over r. Even though we have the l < r condition in the while loop,
            # we still want the same check when skipping through non-alphanumerical characters
            # because of edge cases like ".,". In this case, we would keep incrementing l or decrementing
            # r until it reaches an alphanumerical char, but since there is none, we reach  the end of list
            # and keep trying to increment/decrement, which would result in an index out of range error.
            while l<r and not s[l].isalpha() and not s[l].isdigit():
                l += 1
            while l<r and not s[r].isalpha() and not s[r].isdigit():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            if s[l].lower () == s[r].lower():
                l += 1
                r -= 1

        return True

