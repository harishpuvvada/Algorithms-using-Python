#A naive recursive implementation of 0-1 Knapsack Problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W , wt , val , n):   #Time Complexity is O(2^n)

    # Base Case
    if n == 0 or W == 0 :
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W , wt , val , n-1)

    else:
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),knapSack(W , wt , val , n-1))
        #      max(---- eq for including nth wt-------------------,---- for not including------)


#Using Dynamic programming
def dynamicProg_KP(W, wt, val, n): #Time Complexity is O(nW)
    #creating a table using list comprehensions
    K = [[0 for x in range(W+1)] for x in range(n+1)] #here "+1" cuz we go from 0 to W,0 to n

    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif (wt[i-1] <= w):
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    print(K) #print table
    return K[n][W]




# To test above functions
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(dynamicProg_KP(W , wt , val , n))
print(knapSack(W , wt , val , n))
