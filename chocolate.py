# -*- coding: utf-8 -*-
class Solution:
    def maxChocolate(self, numjars, chocolates):
        if not numjars:
            return 0
        jar1, jar2 = 0, 0
        for choc in chocolates:
            maxChoc = max(jar1 + choc, jar2)
            jar1 = jar2
            jar2 = maxChoc
        return maxChoc

      
    def maxChocolate2(self,numjars,chocolates):
        memo = [-1 for _ in range(numjars)]
        def dp(start):
            if start >= numjars:
                return 0
            if memo[start] != -1:
                return memo[start]
            res = max(dp(start + 1), dp(start + 2) + chocolates[start])
            return res
        return dp(0)


    


if __name__ == "__main__":
    numjars = 4
    chocolates = [1, 3, 5, 6]
    so = Solution()
    maxChoc = so.maxChocolate(numjars, chocolates)
    print(maxChoc)
    maxChoc2 = so.maxChocolate2(numjars, chocolates)
    print(maxChoc2)