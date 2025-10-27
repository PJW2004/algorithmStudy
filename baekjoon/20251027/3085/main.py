# 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다.
# 고른 칸에 들어있는 사탕을 서로 교환한다.
# -> O(N^2)
# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
# -> O(N^2)
# 인접한 두칸을 고르게 되면 변경되는 긴 연속 부분은 3건.
# 따라서, O(N^4) 이다.

# 시간 제한은 1초다.
# 3 <= N <= 50 이므로, 최악인 50^4 은 6,250,000 이다.
def check(a, start_row, end_row, start_col, end_col):
    # 가장 긴 연속 부분을 결정하기 위한 함수
    n = len(a) # 전체 리스트의 길이.
    ans = 1 # 개수 세기.
    for i in range(start_row, end_row+1): # O(N^2)
        cnt = 1 # 개수 카운트 (초기화 가능)
        for j in range(1, n): # 로우의 첫부터 마지막 까지.
            if a[i][j] == a[i][j-1]: # 왼쪽에 있는 값이 현재 위치의 값과 동일하다면.
                cnt += 1 # 개수 카운트 (동일한 사탕 이므로)
            else: # 현재 위치의 값과 같지 않다면 개수 초기화.
                cnt = 1
            if ans < cnt: # 지금까지 모아둔 카운트가 최대 개수라면.
                ans = cnt # 갱신.
    for i in range(start_col, end_col+1): # O(N^2)
        cnt = 1 # 개수 카운트 (초기화 가능)
        for j in range(1, n): # 컬럼의 첫부터 마지막 까지.
            if a[j][i] == a[j-1][i]: # 위에 있는 값이 현재 위치의 값과 동일하다면.
                cnt += 1 # 개수 카운트 (동일한 사탕 이므로)
            else: # 현재 위치의 값과 같지 않다면 개수 초기화.
                cnt = 1
            if ans < cnt: # 지금까지 모아둔 카운트가 최대 개수라면.
                ans = cnt # 갱신.
    return ans # 검토된 최대 개수 반환. # O(2*N^2)

n = int(input())
a = [list(input()) for _ in range(n)]
ans = 0
for i in range(n): # 행 O(N^4)
    for j in range(n): # 열 O(N)
        if j+1 < n: # 열이 최대 개수가 아니라면.
            # 두 칸을 고르고 사탕 교환.
            a[i][j],a[i][j+1] = a[i][j+1],a[i][j]
            # 사탕 검토
            temp = check(a, i, i, j, j+1) # O(2*N^2)
            if ans < temp: # 지금까지 모아둔 카운트(temp) 가 최대 개수라면.
                ans = temp # 갱신
            a[i][j],a[i][j+1] = a[i][j+1],a[i][j]
        if i+1 < n: # 행이 최대 개수가 아니라면.
            # 두 칸을 고르고 사탕 교환.
            a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
            # 사탕 검토
            temp = check(a, i, i+1, j, j) # O(2*N^2)
            if ans < temp: # 지금까지 모아둔 카운트(temp) 가 최대 개수라면.
                ans = temp # 갱신
            a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
print(ans)