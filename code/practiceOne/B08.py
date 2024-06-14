player1, player2 = input().split()

# 定義每個出拳對應的勝出拳型
win_map = {"Y": "X", "O": "Y", "X": "O"}  # 剪刀贏布  # 石頭贏剪刀  # 布贏石頭

# 判斷勝負
if player1 == player2:
    print(0)  # 平手
elif win_map[player1] == player2:
    print(1)  # 玩家1贏了
else:
    print(2)  # 玩家2贏了
