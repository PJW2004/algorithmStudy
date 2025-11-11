# 이거 끝내고 과제 하기 꼭

# 2 <= M <= 10
# 3 <= N <= 100
# 1 <= 행성의 크기 <= 10,000

# 첫째 줄에 우주의 개수 M, 각 우주의 개수 N이 주어짐.
# 둘째 줄부터 M개의 줄에 공백으로 구분된 행성의 크기가 한 줄에 하나씩 1분 우주부터 차례대로 주어짐.
m,n = map(int, input().split())

# 1 <= i
# j <= N
universe = [list(map(int, input().split())) for _ in range(m)] # 우주의 개수

# 구성이 같은데 순서만 다른 우주의 쌍은 한번만 셈.
# 우주의 쌍 조건은 다음과 같음.
# Ai < Aj -> Bi < Bj
# Ai = Aj -> Bi = Bj
# Ai > Aj -> Bi > Bj
# 모든 쌍은 동일해야 한다.
# 반례: A1 = 1 < A3 = 2인데, B1 = 12 > B3 = 10 이다.
# 1 3 2
# 12 50 10

# 모든 쌍을 검토하면 되지 않을까.
# 작으면 1, 같으면 2, 크면 3
newniverse = []
# O(N^3) ..?
for planet in universe:
    if_planet = ""
    for i in range(n-1):
        for j in range(i, n):
            if i == j:
                continue
            if planet[i] < planet[j]:
                if_planet += "1"
            elif planet[i] == planet[j]:
                if_planet += "2"
            elif planet[i] > planet[j]:
                if_planet += "3"
    newniverse.append(if_planet)

# 중복된 항목의 개수를 세는게 아님.
# 같은 항목들로 만들 수 있는 쌍의 개수를 세는거임.
# 조합을 이용하자.
# O(N)
counts = {}
for if_planet in newniverse:
    if if_planet in counts:
        counts[if_planet] += 1
    else:  
        counts[if_planet] = 1

# O(N)
total_pairs = 0
for _n in counts.values():
    # 갯수가 n개일 때, 만들수 있는 쌍의 개수는 nC2.
    # nC2 의 2인 이유는 쌍을 구하는 문제이기 때문.
    if _n > 1:
        total_pairs += (_n * (_n - 1)) // 2
print(total_pairs)

# O(N^3) + O(N) + O(N) 