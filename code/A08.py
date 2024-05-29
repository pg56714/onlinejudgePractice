a = int(input())
num_packs = a // 12
remaining_pencils = a % 12
total_cost = num_packs * 50 + remaining_pencils * 5
print(total_cost)
