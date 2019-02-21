# Method 1 
# Time:  O(C) c is total content of words
# Space: O(1)

class Solution(object):
    def isAlienSorted(self, words, order):
        #store order and index

        order_index = {c: i for i, c in enumerate(order)}

        for i in xrange(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            # Find the first difference word1[k] != word2[k].
            for k in xrange(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[k] != word2[k]:# why has this
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break  #why break
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False

        return True

if __name__='main':
	Solution().isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz") #no "break" will return False