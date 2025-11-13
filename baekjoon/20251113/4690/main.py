# a^3 = b^3 + c^3 + d^3 을 전부 찾으라는 문제 같은데?
out = []
# 어차피 6부터 시작
for a in range(6, 101): # a 는 100 이하니까
    a_cube = a**3
    for b in range(2, a): # a 보다 작은 범위
        b_cube = b**3
        for c in range(b, a):
            c_cube = c**3
            for d in range(c, a):
                if a_cube == (b_cube + c_cube + d**3):
                    out.append(f'Cube = {a}, Triple = ({b},{c},{d})')
print('\n'.join(out))