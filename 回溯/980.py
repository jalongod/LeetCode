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