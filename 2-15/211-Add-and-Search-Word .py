# Method 1 Trie & DFS recursive
# Time:
# Space:


class TrieNode():
    def __init__(self):
        self.children=collections.defaultdict(TrieNode)
        self.isWord=False #will be true if the node represents the end of word
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word):
        node=self.root
        for w in word:
            node=node.children[w]
        node.isWord=True

    def search(self, word):
        node=self.root
        self.res=False
        self.dfs(node,word)
        return self.res
    
    def dfs(self,node,word):
        if not word:
            if node.isWord:
                self.res=True
            return
        if word[0]==".":
            for n in node.children.values():
                self.dfs(n,word[1:])
        else:
            node=node.children.get(word[0])
            if not node:
                return
            self.dfs(node,word[1:])

# Method 2 Trie & DFS stacking
# Time:
# Space:
###. how to call this function
class TrieNode:
    def __init__(self):
        self.children=collections.defaultdict(TrieNode)
        self.isWord=False #will be true if the node represents the end of word
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word):
        node=self.root
        for w in word:
            #if w in node.children:
            node=node.children[w]
            #else:
                #node.children[w]=TrieNode()
                #node=node.children[w]
        node.isWord=True

    def search(self, word):
        stack=[(self.root,word)]
        while stack:
            node,w = stack.pop()
            if not w:
                if node.isWord:
                    return True
            
            elif w[0]=='.':
                for n in node.children.values():
                    #append (all word trie tree, all letters in word (except "."))
                    stack.append((n,w[1:]))
                    
            else:
                if w[0] in node.children:
                    n=node.children[w[0]]
                    stack.append((n,w[1:]))
        return False
        

["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Method 3 Search 
# Time: search O(C*N)
# Space:
class WordDictionary(object):
    def __init__(self):
        self.len2words = collections.defaultdict(list) #key is word length, value is word

    def addWord(self, word):
        self.len2words[len(word)].append(word)

    def search(self, word):
        words = self.len2words[len(word)] # get list of words which have the same length as word
        # iterate each index and char in search word 
        for i, char in enumerate(word):
        	# because same length, both index and char should be same in any element in words list
            words = [w for w in words if char in ('.', w[i])]
            # if words list is empty
            if not words: return False
        return True