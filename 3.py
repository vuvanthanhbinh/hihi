n = int(input())
a = 1
for i in range(1, n + 1):
    a = 8 * a + 10 **(i-1)
print(a)