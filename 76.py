'''
76. 最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
官方题解
直觉

本问题要求我们返回字符串SS 中包含字符串TT的全部字符的最小窗口。我们称包含TT的全部字母的窗口为可行窗口。

可以用简单的滑动窗口法来解决本问题。

在滑动窗口类型的问题中都会有两个指针。一个用于延伸现有窗口的 rightright指针，和一个用于收缩窗口的leftleft 指针。在任意时刻，只有一个指针运动，而另一个保持静止。

本题的解法很符合直觉。我们通过移动right指针不断扩张窗口。当窗口包含全部所需的字符后，如果能收缩，我们就收缩窗口直到得到最小窗口。

答案是最小的可行窗口。
'''

import copy


class Solution:
    def minWindow(self, s, t):

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[
                    character]:
                formed += 1

            # Try and co***act the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[
                        character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

            # Keep expanding the window once we are done co***acting.
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

    def minWindow2(self, s: str, t: str) -> str:
        res = [-1, -1]

        sl = list(s)
        tl = list(t)

        def getWindowFromIndex(start, mapper) -> []:
            left, right = start, start
            while right < len(s):
                if left == right and (not sl[left] in tl):
                    left += 1
                    right += 1
                else:
                    if sl[right] in tl:
                        if sl[right] in mapper:
                            if mapper[sl[right]] == 1:
                                mapper.pop(sl[right])
                            else:
                                mapper[sl[right]] -= 1
                    if len(mapper) == 0:
                        return [left, right]
                    right += 1
            return [left, left]

        left = 0
        mapper1 = {}
        for node in t:
            if node in mapper1:
                mapper1[node] += 1
            else:
                mapper1[node] = 1

        while (left < len(s)):
            win = getWindowFromIndex(left, copy.deepcopy(mapper1))
            if win[1] - win[0] + 1 < len(t):
                break
            if win[1] - win[0] < res[1] - res[0] or res == [-1, -1]:
                res = win
            left = win[0] + 1
        return "".join(sl[res[0]:res[1] + 1])
        pass


sol = Solution()
# max = sol.minWindow("DADBDCD", "ABC")
max = sol.minWindow("ADOBECODEBANC", "ABC")
# max = sol.minWindow("a", "a")
# max = sol.minWindow("aa", "aa")
# max = sol.minWindow("ADOBEC", "BANC")

print(max)
