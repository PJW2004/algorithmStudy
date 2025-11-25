# N 과 M 이 주어진다.
# N 은 자연수
# M 은 크기
# 1 <= M <= N <= 8 
# 이전과 동일.
n,m = map(int,input().split())

# M 만큼 중복되지 않고 반복되어야 한다.
# 그리고 고른 수열은 오름차순이어야 한다. (추가)
# 어디서 부터 수를 더해야 하는지 시작을 의미하는 변수가 추가되어야 함.
visited = [False]*(n+1) # 참 / 거짓
sequence = [] # 정답 순열
def dfs(start:int):
    if len(sequence) == m:
        print(' '.join(map(str, sequence))) # 수열을 출력
        return
    for i in range(start, n+1):
        if visited[i]: # 만약 참이면 다시 시작
            continue
        # 선택 (Choose)
        visited[i] = True
        sequence.append(i)

        # 계속 가기 (Recurse)
        dfs(i+1)

        # 선택 취소 (BackTrack)
        sequence.pop()
        visited[i] = False
dfs(1)