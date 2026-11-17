import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    c = []
    idx = 1
    for _ in range(n):
        row = [int(x) for x in data[idx:idx+n]]
        c.append(row)
        idx += n
        
    min_row = [min(row) for row in c]
    suffix_min = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_min[i] = suffix_min[i + 1] + min_row[i]
        
    best_cost = float('inf')
    best_assign = []
    curr_assign = [0] * n
    used_job = [False] * n
    
    def branch_and_bound(worker, current_cost):
        nonlocal best_cost, best_assign
        if worker == n:
            if current_cost < best_cost:
                best_cost = current_cost
                best_assign = curr_assign[:]
            return
            

        if current_cost + suffix_min[worker] >= best_cost:
            return
            
        jobs = sorted(range(n), key=lambda j: c[worker][j])
        for j in jobs:
            if not used_job[j]:
                if current_cost + c[worker][j] + suffix_min[worker + 1] < best_cost:
                    used_job[j] = True
                    curr_assign[worker] = j + 1
                    branch_and_bound(worker + 1, current_cost + c[worker][j])
                    used_job[j] = False

    branch_and_bound(0, 0)
    print(best_cost)
    print(" ".join(map(str, best_assign)))

if __name__ == '__main__':
    solve()