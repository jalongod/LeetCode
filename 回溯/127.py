'''
127. 单词接龙
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List


class Solution:
    

    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        tmp = [[0 for _ in range(len(wordList)+1)]for __ in range(len(wordList)+1)]
        res = -1

        def isonediff(s1, s2, c):
            if c > 1:
                return False
            if len(s1) == 0:
                return True
            if s1[0] is s2[0]:
                return isonediff(s1[1:], s2[1:], c)
            else:
                return isonediff(s1[1:], s2[1:], c+1)

        def check(i, j):
            if i > j:
                i, j = j, i
            if tmp[i][j]:
                return True
            tmp[i][j] = isonediff(wordList[i], wordList[j], 0)
            return tmp[i][j]

        def backtrace(begin, end, wl, path):
            nonlocal res
            bi = wl.index(begin)
            if begin is end:
                if res == -1:
                    res = len(path)
                else:
                    res = min(res, len(path))
            for i in range(len(wl)):
                if wl[i] in path:
                    continue
                if check(bi, i):
                    path.append(wl[i])
                    backtrace(wl[i], end, wl, path)
                    path.pop()
        
        backtrace(beginWord, endWord, wordList, [])
        return res+1


sol = Solution()
max = sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(max)
