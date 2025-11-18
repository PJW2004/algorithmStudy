# 첫째줄 N
# 둘째줄 K : 몇개 선택할 건지
n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)] # 카드 리스트

visited = [False]*(n+1) # 1부터 N까지의 숫자를 사용했는지 체크
sequence = [] # 정답 순열
sequences = []

def dfs():
    # 도착 : 만약 현재 순열(sequence)의 길이가 K와 같다면
    if len(sequence) == k:
        out = ""
        for i in sequence:
            out += str(cards[i-1])
        sequences.append(out)
        return
    
    # 탐색 : 다음 숫자 선택
    for i in range(1, n+1): # 1-N 까지의 모든 숫자 탐색
        if not visited[i]: # 만약 i번째 숫자를 아직 사용하지 않았다면
            # 선택 (Choose)
            visited[i] = True # i를 사용했다고 표시
            sequence.append(i) # 순열 바구니에 i를 추가

            # 계속 가기 (Recurse)
            dfs()

            # 선택 취소 (BackTrack)
            sequence.pop()
            visited[i] = False
dfs()
print(len(set(sequences)))