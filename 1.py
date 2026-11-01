n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
r = [i + 1 for i in range(n) if a[i] and b[i]]
if not r :
    print(0)
else:
    print(len(r))
    print(*r)