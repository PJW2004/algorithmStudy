# 브루트 포스 알고리즘은 먼저 가능한 방법을 찾아내고.
# 가능한 방법을 활용하여 값을 구하는 방식.
# 9명의 난쟁이중 7명의 난쟁이를 찾는 문제이며, 총합은 100 이다.
# 9명의 난쟁이 중에 7명을 찾을지.
# 7명의 난쟁이가 아닌 2명을 찾을지.
# 9명의 난쟁이를 먼저 입력받는다.
dwarfs = []
# O(N)
for _ in range(9):
    dwarfs.append(int(input())) # 9명의 난쟁이 입력.
# O(N)
dwarfs_sum = sum(dwarfs) # 모든 키의 합.
# O(N^2) 모든 경우의 수 계산
for i in range(9):
    break_point = False
    for j in range(9):
        if i != j:
            dwarfs_j = dwarfs[j]
            if (dwarfs_sum - dwarfs[i] - dwarfs_j) == 100:
                # 7명의 난쟁이의 키는 모두 다르다.
                dwarfs.remove(dwarfs[i])
                dwarfs.remove(dwarfs_j)
                break_point = True
                break
    if break_point:
        break
# O(N)
for dwarf in sorted(dwarfs):
    print(dwarf)