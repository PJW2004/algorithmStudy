# 브루트 포스가 모든 해를 다 구하긴 하지만,
# 효율적으로 모든 해를 구해야 한다.
t = int(input())
for _ in range(t):
    # m,n 경우의 수.
    # x,y 정답.
    m,n, x,y = map(int,input().split())
    x -= 1
    y -= 1
    k = x # 가 되어야 한다.
    while k < m*n: # k 가 마지막의 수보다 크다면 그건 거짓.
        if k%n == y:
            print(k+1)
            break
        k += m
    else:
        print(-1)
