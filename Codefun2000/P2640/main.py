from collections import deque

def main():
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().split())))

    distence = [ [0 for __ in range(n)] for _ in range(m) ]
    # neihbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # for r in range(m):
    #     for c in range(n):
    #         d = grid[r][c]
    #         if d > 0:
    #             # run bfs 计算器邻域距离
    #             q = deque()
    #             q.append((r,c,d))
    #             distence[r][c] += d
    #             visited = set()
    #             visited.add((r,c))
    #             while q:
    #                 cur_r, cur_c, cur_d = q.popleft()
    #                 for dr, dc in neihbors:
    #                     next_r = cur_r + dr
    #                     next_c = cur_c + dc
    #                     next_d = cur_d - 1
    #                     if next_r < 0 or next_r >= m or next_c < 0 or next_c >= n:
    #                         continue
    #                     if next_d <= 0:
    #                         continue
    #                     if (next_r, next_c) in visited:
    #                         continue
    #                     q.append((next_r, next_c, next_d))
    #                     visited.add((next_r, next_c))
    #                     distence[next_r][next_c] += next_d
   
    for r in range(m):
        for c in range(n):
            d = grid[r][c]
            if d > 0:
                # [x_min, x_max)
                rr_min = max(0, r - d + 1)
                rr_max = min(m, r + d)
                for rr in range(rr_min, rr_max):
                    r_dis = abs(r - rr)
                    remain_dis = d - r_dis
                    # [y_min, y_max)
                    cc_min = max(0, c - remain_dis + 1)
                    cc_max = min(n, c + remain_dis)
                    for cc in range(cc_min, cc_max):
                        c_dis = abs(c - cc)
                        distence[rr][cc] += d - r_dis - c_dis
    
    # run dp on distence
    dp = [ [ 0 for __ in range(n) ] for _ in range(m) ]
    dp[0][0] = distence[0][0]
    for c in range(1, n):
        dp[0][c] = dp[0][c-1] + distence[0][c]
    for r in range(1, m):
        dp[r][0] = dp[r-1][0] + distence[r][0]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + distence[r][c]

    print(dp[m-1][n-1])

                
if __name__ == "__main__":
    main()
