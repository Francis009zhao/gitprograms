class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

        for i in range(1,K+1):
            for j in range(1,N+1):
                dp[i][j] = dp[i - 1][j - 1] + (dp[i][j - 1] + 1)
                if dp[i][j] >=N:
                    return j
        return 0
        # dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
        # for i in range(1, K + 1):
        #     for step in range(1, N + 1):
        #         dp[i][step] = dp[i - 1][step - 1] + (dp[i][step - 1] + 1)
        #         print(dp[i][step])
        #         if dp[K][step] >= N:
        #             return step
        # return 0

print(Solution().superEggDrop(2,6))