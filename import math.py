import math

L, R, a, b = map(int, input("nhập số :").split())


lcm = math.lcm(a, b)


def count(N):
    return (N // a) + (N // b) - 2 * (N // lcm)


print(count(R) - count(L - 1))