# 定义队员类
class Player:
    def __init__(self, id, scores):
        self.id = id
        # 排序成绩降序
        self.scores = sorted(scores, reverse=True)

    # 定义比较函数
    def __lt__(self, other):
        for a, b in zip(self.scores, other.scores):
            if a != b:
                return a > b
        return self.id < other.id


def main():
    import sys

    input = sys.stdin.read
    data = input().split()
    idx = 0
    n, m, k = map(int, data[idx : idx + 3])
    idx += 3
    players = []
    for i in range(1, n + 1):
        scores = list(map(int, data[idx : idx + k]))
        idx += k
        player = Player(i, scores)
        players.append(player)
    # 排序
    players.sort()
    # 输出前m个队员的编号
    selected = [str(player.id) for player in players[:m]]
    print(" ".join(selected))


if __name__ == "__main__":
    main()
