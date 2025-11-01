# 0 <= N <= 500,000
# 0 <= M <= 10
# 채널은 무한대.
n = int(input())
m = int(input())
broken = [False] * 10 # 망가진 리모컨의 초기화.
if m > 0:
    a = list(map(int,input().split()))
else:
    a = [] # 망가진 리모컨의 버튼이 없는 경우.
for x in a:
    broken[x] = True # 망가진 리모컨의 버튼이 있는 경우.
def possible(c):
    if c == 0: # c 만큼 이동이 가능한지.
        if broken[0]: # 먼저 망가졌는지
            return 0
        else:
            return 1 # 망가지지 않은 경우.
    l = 0
    while c > 0:
        if broken[c%10]:
            return 0
        l += 1
        c //= 10
    return l
ans = abs(n-100)
for i in range(0, 1_000_000+1): # 경우의 수 최소값.
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c-n)
        if ans > l + press:
            ans = l + press
print(ans)