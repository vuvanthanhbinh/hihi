n , r = map(int , input().split())
fix = [0] * (n + 1)
for _ in range(r):
    u , v = map(int , input().split())
    fix[u] = v
used = [False] * (n + 1)
a = [0] * n 
out = []

def go(p):
    if p == n:
        out.append(" ".join(map(str , a)))
        return 
    for v in range(1 , n + 1):
        if used[v] or (fix[p] and fix[p] != v):
            continue 
        used[v] = True 
        a[p] = v
        go(p + 1)
        used[v] = False

go(0)
print("\n".join(out)) if out else print(0)