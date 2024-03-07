class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        # DFS where j is used to mark the start of the substring of the word, and root is the current letter whose children we will check to
        # see if they match the remaining word.
        def dfs(j, root):
            for i in range(j, len(word)):
                char = word[i]
                # If char is ., it can match any letters. Recursively check every child of the current root, but increment i cos we want to
                # check the remainder of word after '.'
                if char == '.':
                    for child in root.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if char not in root.children:
                        return False
                    root = root.children[char]
            return root.endOfWord
        return dfs(0, self.root)
