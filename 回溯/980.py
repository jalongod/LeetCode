'''
980. 不同路径 III

在二维网格 grid 上，有 4 种类型的方格：

1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目，每一个无障碍方格都要通过一次。

 

示例 1：

输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
输出：2
解释：我们有以下两条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def uniquePathsIII(self, grid) -> int:
        count0, startx, starty, has_end, res, width, height, dir = 0, -1, -1, False, 0, len(
            grid), len(grid[0]), [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                v = grid[i][j]
                if v == 0:
                    count0 += 1
                if v == 1:
                    startx = i
                    starty = j
                if v == 2:
                    has_end = True
        if startx == -1 or starty == -1 or not has_end:
            return 0

        def getCount(x, y, used):
            nonlocal res
            if x < 0 or x >= width or y < 0 or y >= height or [
                    x, y
            ] in used or grid[x][y] == -1:
                return
            if grid[x][y] == 2:
                if count0 == len(used) - 1:
                    res += 1
                return
            for d in dir:
                used.append([x, y])
                getCount(x + d[0], y + d[1], used)
                used.pop()
            pass

        getCount(startx, starty, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    # max = sol.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]])
    # max = sol.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]])
    # max = sol.uniquePathsIII([[0, 1], [2, 0]])
    max = sol.uniquePathsIII([[1, 2]])

    print(max)