from bisect import bisect_right

def main():
    n, m = map(int, input().split())
    positions = list(map(int, input().split()))
    # 二分答案法
    # N 个位置中选择 M 个上车点，并且要让每个位置到上车的最大距离最小
    # 二分这个最大距离：
    # 尝试 M 个站点能不能覆盖 N 个地点
    
    def try_put(distence: int):
        count = 0
        index = 0
        while index < n:
            station_pos = positions[index] + distence
            # 找到第一个大于station_pos的位置p
            # 这个station能覆盖的区域为[index, p-1]
            station_index = bisect_right(positions, station_pos, lo = index) - 1
            cover_pos = positions[station_index] + distence
            index = bisect_right(positions, cover_pos, lo = station_index)
            count += 1
        return True if count <= m else False

    left = 0
    right = positions[-1] - positions[0]
    ans = right

    while left <= right:
        mid = (left + right) // 2
        if try_put(mid):
            right = mid - 1
            ans = mid
        else:
            left = mid + 1
    print(ans)

if __name__ == "__main__":
    main()
