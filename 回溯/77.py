class Solution:
    def combine(self, n: int, k: int):
        if k <= 0:
            return []
        res = []

        def dfs(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                dfs(i + 1, path)
                path.pop()

        dfs(1, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    max = sol.combine(20, 16)
    print(max)