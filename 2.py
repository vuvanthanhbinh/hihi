N , l , u = map(int , input().split())
u = min(u, N)
s = 0 
for x in range(l , u + 1):
    s += N-x+1
print(s)