# 브루트 포스
# 2와 5로 나누어 떨어지지 않은 정수.
# 자릿수가 모두 1로만 되어 있는 숫자의 가장 작은 값의 자리수를 출력.
# ---------------------------------------------------------------
# while True:
#     try:
#         n = int(input())
#     except:
#         break

#     num = 0
#     i = 1
#     while True:
#         num = n * i
#         if num % n == 0:
#             if all([True if _num == "1" else False for _num in str(num)]):
#                 print(len(str(num)))
#                 break
#         i += 1
# ---------------------------------------------------------------
# 1 로만 늘려보기.
# while True:
#     try: 
#         n = int(input())
#     except:
#         break

#     num = "1"
#     i = 1
#     while True:
#         _num = num * i
#         if int(_num) % n == 0:
#             print(len(str(_num)))
#             break
#         i += 1
# ---------------------------------------------------------------
# 1 의 규칙성을 이용해 보기.
while True:
    try:
        n = int(input())
    except:
        break

    num = 0
    i = 1
    while True:
        num = num * 10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1