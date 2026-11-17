import sys

data = list(map(int, sys.stdin.buffer.read().split()))

n, k = data[0], data[1]

fixed = [0] * (n + 1)

# Đọc điều kiện cố định
pos = 2
for _ in range(k):
    u, v = data[pos], data[pos + 1]
    pos += 2

    if fixed[u] != 0 and fixed[u] != v:
        print(0)
        sys.exit()

    fixed[u] = v

# Đánh dấu các giá trị đã được giữ chỗ
reserved = set()

for i in range(1, n + 1):
    if fixed[i] != 0:
        if fixed[i] in reserved:
            print(0)
            sys.exit()

        reserved.add(fixed[i])

a = [0] * (n + 1)
used = [False] * (n + 1)

found = False

def backtrack(i):
    global found

    if i > n:
        found = True
        sys.stdout.write(' '.join(map(str, a[1:])) + '\n')
        return

    # Vị trí đã được cố định
    if fixed[i] != 0:
        v = fixed[i]

        used[v] = True
        a[i] = v

        backtrack(i + 1)

        used[v] = False
        return

    # Vị trí chưa cố định
    for v in range(1, n + 1):
        if not used[v] and v not in reserved:
            used[v] = True
            a[i] = v

            backtrack(i + 1)

            used[v] = False

backtrack(1)

if not found:
    print(0)