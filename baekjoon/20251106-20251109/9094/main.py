# 시간제한 1초
# n, m 이 주어짐
# 0 보다 크고 100보다 작거나 같다.
# O(N^4) 정도 될려나
# (a,b) 의 정수인 쌍의 개수를 구해야 하니까.

# 하루지나고 다시 보니까 정리됨.
# 개수: T
# 0 < a < b < n
# 0 < a < b < 100
# (a**2 + b**2 + m)/(a*b) 가 정수인 경우.
# O(N^3) ≈ 941,192 이였구연
for t in range(int(input())):
    n,m = map(int,input().split())
    count = 0 # 한 쌍을 구해야함.
    for b in range(1, n): # 0 < b < n
        for a in range(1, b): # 0 < a < b
            # 예외 처리보단 나머지가 더 좋잖아.
            if (a**2 + b**2 + m) % (a*b) == 0:
                count += 1
    print(count)