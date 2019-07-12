#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 322. coin change


class Solution:
    def coinChange(self, coins, amount: int) -> int:

        length = len(coins)
        if length <= 0:
            return -1
        if amount == 0:
            return 0
        counts = [0] * length

        # 倒叙
        for i in range(length):
            for j in range(i):
                if (coins[j] < coins[i]):
                    coins[i], coins[j] = coins[j], coins[i]
                pass

        for i in range(len(coins)):
            counts[i] = int(amount / coins[i])
            pass
        left = amount
        count = 0
        for i in range(length):
            for j in range(counts[i]):
                if left == coins[i]:
                    # print(str(count + 1) + '次dd')
                    return count + 1
                if left < coins[i]:
                    # print(str(count + 1) + '次ddee')
                    break
                else:
                    left -= coins[i]
                    count += 1
                    # print(str(count) + '次' + str(coins[i]))
                pass
            pass
            print(str(count) + '次' + str(coins[i]))
        pass

        return -1


if __name__ == '__main__':
    sol = Solution()
    max = sol.coinChange([186, 419, 83, 408], 6249)
    # max = sol.lengthOfLIS([2, 5, 3, 7])
    print(max)
