# 시간 제한은 1초
# 세 정수 n, m, k 가 공백으로 주어짐.
# 1 <= k < n <= 1000
# 1 <= m <= 1000
# m * k 를 하고 나머지 k 개를 더한다.
n,m,k = map(int, input().split())
print((m*k)+m)