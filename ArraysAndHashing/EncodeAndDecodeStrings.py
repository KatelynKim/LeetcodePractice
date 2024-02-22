class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            count = int(s[i:j])
            res.append(s[j+1: j+count+1])
            i = j + count + 1

        return res

'''
Time complexity
- encode: O(N) where N is the number of strings in the strs list.
- decode: O(c) where c is the number of total characters.
'''
