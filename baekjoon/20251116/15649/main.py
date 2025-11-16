# N 과 M 이 주어진다.
# N 은 자연수
# M 은 크기
# 1 <= M <= N <= 8
n,m = map(int,input().split())

# M 만큼 중복되지 않고 반복되어야 한다.
# 이 경우 재귀 함수를 사용해야 한다.
# 백트래킹과 DFS
visited = [False]*(n+1) # 1부터 N까지의 숫자를 사용했는지 체크
sequence = [] # 정답 순열

def dfs():
    # 도착 : 만약 현재 순열(sequence)의 길이가 M과 같다면
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    
    # 탐색 : 다음 숫자 선택
    for i in range(1, n+1): # 1-N까지의 모든 숫자 탐색
        """
              [ ]
         |   |   |   |
         |   |   |   |
        [1] [2] [3] [4]
        """
        if not visited[i]: # 만약 i번째 숫자를 아직 사용하지 않았다면
            # 선택 (Choose)
            visited[i] = True  # i를 사용했다고 표시
            sequence.append(i) # 순열 바구니에 i를 추가

            # 계속 가기 (Recurse)
            """
                   [1]
              |     |     |
              |     |     |
            [1,2] [1,3] [1,4]
            """
            dfs()

            # 선택 취소 (BackTrack)
            sequence.pop()
            visited[i] = False
dfs()