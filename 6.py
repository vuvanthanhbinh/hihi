n , k = map(int , input().split())
used = [False] * (n + 1)
a = [0] * k
out = []

def go(p):
    if p == k:
        out.append(" ".join(map(str , a)))
        return 
    for v in range(1 , n + 1):
        if used[v]:
            continue 
        used[v] = True 
        a[p] = v
        go(p + 1)
        used[v] = False

go(0)
print("\n".join(out)) if out else print(0)