'''https://www.youtube.com/watch?v=lBRtnuxg-gU'''

''' finding minimal path distance from top left element to bottom right element '''

def mincost(cost,m,n): #Complexity is O(mn)

    MM =[[0 for _ in range(n)] for _ in range(m)] #matrix storing the path distances

    MM[0][0] = cost[0][0] #first element has to be the same

    for i in range(1,m):
        MM[i][0] = cost[i][0] + MM[i-1][0]   #filling up first row since there is only one path

    for j in range(1,n):
        MM[0][j] = cost[0][j] + MM[0][j-1]  #filling up first column since there is only one path

    for k in range(1,m):
        for p in range(1,n):
            MM[k][p] = cost[k][p] + min(MM[k-1][p],MM[k][p-1])

    return MM[m-1][n-1]


cost = [[1,3,5,8],
       [4,2,1,7],
       [4,3,2,3]]

print(mincost(cost,3,4))
