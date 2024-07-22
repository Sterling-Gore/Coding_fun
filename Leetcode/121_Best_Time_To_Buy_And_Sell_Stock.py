def maxProfit(prices: list[int]) -> int:
        max = 0
        j = 0
        for i in range(len(prices)):
            if prices[i] < prices[j]:
                j = i
            else:
                if max < prices[i] - prices[j]:
                    max = prices[i] - prices[j]
        
        return max




example1 = [7,1,5,3,6,4]
example2 = [7,6,4,3,1]

print( maxProfit(example1) )
print( maxProfit(example2) )