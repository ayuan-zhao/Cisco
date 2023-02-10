class Solution:
    def maximumDifference(self, prices) -> int:
        if not prices:
            return -1
        maxDiff = 0
        left, right = 0,1
        while right < len(prices):
            if prices[right] > prices[left]:
                diff = prices[right] - prices[left]
                maxDiff = max(diff,maxDiff)
                right += 1
            else:
                left = right
                right += 1
        if maxDiff == 0:
            return -1
        else:
            return maxDiff
        
        

    def maximumDifference2(self,prices)->int:
        maxDiff,minPrice= -1, float("inf")
        for price in prices:
            minPrice = min(minPrice,price)
            maxDiff = max(maxDiff,price - minPrice)
        if maxDiff <= 0:
            return -1
        else:
            return maxDiff


if __name__ == "__main__":
    
    so = Solution()
    prices= (1,5,2,7)
    maxDiff = so.maximumDifference(prices)
    maxDiff2 = so.maximumDifference2(prices)
    print("maxDiff",maxDiff)
    print("maxDiff2",maxDiff2)


            
        
            
            