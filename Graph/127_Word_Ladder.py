from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        # All words are of same length
        L = len(beginWord)
        # Dictionary to hold all combination of words that can be formed
        # By changing one letter at a time
        all_combi_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word
                all_combi_dict[word[:i] + '*' + word[i+1:]].append(word)

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]
                # For all the words sharing the same intermediate state
                for word in all_combi_dict[intermediate_word]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                all_combi_dict[intermediate_word] = []
        return 0
