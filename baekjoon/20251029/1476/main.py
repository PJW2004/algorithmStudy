# 1 <= E <= 15
# 1 <= S <= 28
# 1 <= M <= 19
# 모든 조합의 개수는 15 * 28 * 19 = 7,980년 까지다.
# 시간 제한은 2초.
target_e, target_s, target_m = map(int, input().split())
year = 0
while True:
    year += 1
    
    e = (year - 1) % 15 + 1
    s = (year - 1) % 28 + 1
    m = (year - 1) % 19 + 1
    
    # 원래는 문자열 비교 했는데, 그게 더 느림.
    if e == target_e and s == target_s and m == target_m:
        print(year)
        break