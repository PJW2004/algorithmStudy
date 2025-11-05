# 제한 시간 0.5초
# 아주 기본
# import time
# start = time.time()
# ans = ""
# for i in range(1,100_000_000): # 1 <= n <= 100,000,000
#     # 100,000,000 은 9자리수
#     ans += str(i)
# end = time.time()
# print(end-start)
# 필터링
# 1 - 9 = 1
# 10 - 99 = 2
# 100 - 999 = 3
# 1000 - 9999 = 4
# ----------------
# (9-1+1)*1
# (99-10+1)*2
# (999-100+1)*3
n = int(input())
ans = 0
number = 1 # 1 <= n
length = 1
while number <= n: # 지정된 수를 넘으면 안됨.
    # breakpoint()
    # 10-1 = 9
    # 100-1 = 99
    # 1000-1 = 9999
    end = number*10-1 
    if end > n: # end 가 지정된 수보다 크다면 안됨. / 오차
        end = n
    ans += (end-number+1)*length
    number *= 10
    length += 1
print(ans)