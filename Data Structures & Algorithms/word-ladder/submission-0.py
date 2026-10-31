from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord: return beginWord

        wordList.append(beginWord)
        adj = defaultdict(list)
        for a in range(len(wordList)):
            for b in range(a + 1, len(wordList)):
                word1, word2 = wordList[a], wordList[b]
                if len(word1) != len(word2): continue

                numDiff = 0
                for i in range(len(word1)):
                    if wordList[a][i] != wordList[b][i]:
                        numDiff += 1
                        if numDiff > 1: break

                if numDiff == 1:
                    adj[wordList[a]].append(wordList[b])
                    adj[wordList[b]].append(wordList[a])
        
        # Number of words in transformation sequence
        # if it exists so it includes the start word.
        depth, visited, q = 1, {beginWord}, deque([beginWord])
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                print(word)
                for neighbor in adj[word]:
                    if neighbor in visited: continue
                    if neighbor == endWord: return depth + 1
                    visited.add(neighbor)
                    q.append(neighbor)
            depth += 1
        return 0



