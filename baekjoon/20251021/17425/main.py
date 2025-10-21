# 테스트 케이스가 추가된 경우.
# O(T*N) 으로 T <= 100,000 이고, N <= 1,000,000 이 된다.
# 그러면 최악은 100,000 * 1,000,000 ≈ 100,000,000,000 이 된다.
# ---------------------------------------------------------------
# test_case = int(input())
# # O(T)
# for _ in range(test_case):
#     # O(N)
#     n = int(input())
#     medicinal_water_sum = 0
#     for i in range(1, n+1):
#         medicinal_water_sum += (n//i)*i
#     print(medicinal_water_sum)
# ---------------------------------------------------------------
n_max = 1_000_000
f = [1]*(n_max+1)
g = [0]*(n_max+1)
"""
2: [1, 1, 3, 1, 3, 1]
3: [1, 1, 3, 4, 3, 1]
4: [1, 1, 3, 4, 7, 1]
5: [1, 1, 3, 4, 7, 6]
"""
for i in range(2, n_max+1):
    j = 1 # i 의 배수
    while i*j <= n_max: # 이면서 n 보다 작은 약수
        f[i*j] += i
        j += 1
for i in range(1, n_max+1):
    g[i] = g[i-1] + f[i] # 1 ~ n 약수의 모든 합
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ans.append(g[n])
print('\n'.join(map(str,ans))+'\n')