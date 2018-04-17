#This solution is way better than  brute force

A = [1,2,3,4]
B = [2,4,7,8]
commonalities = set(A) - (set(A) - set(B))
