from typing import Iterable, Callable, List, Tuple, TypeVar, Optional

T = TypeVar("T")
def timsort_lite(iterable: Iterable[T], key: Optional[Callable[[T], object]] = None) -> List[T]:
    a: List[T] = list(iterable)
    n = len(a)
    if n < 2:
        return a

    # DSU: key 캐시 (한 번만 호출)
    if key is None:
        keys = a[:]              # 비교 가능한 타입 가정(문자열/숫자 등)
    else:
        keys = [key(x) for x in a]

    # -------- helpers --------
    def compute_minrun(n: int) -> int:
        # CPython과 유사한 32~64 사이의 minrun
        r = 0
        while n >= 64:
            r |= n & 1
            n >>= 1
        return n + r

    def binary_left(a_keys: List[object], lo: int, hi: int, k) -> int:
        # a_keys[lo:hi)에서 k의 좌측 삽입 위치
        while lo < hi:
            mid = (lo + hi) // 2
            if a_keys[mid] < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def binary_insertion_sort(a: List[T], keys: List[object], lo: int, hi: int, start: int) -> None:
        # a[lo:hi)를 정렬하되, a[lo:start]는 이미 정렬되어 있다고 가정.
        for i in range(start, hi):
            ai, ki = a[i], keys[i]
            pos = binary_left(keys, lo, i, ki)  # 안정성: ==일 때 왼쪽에 꽂아서 '왼쪽 우선'
            # 한 칸씩 당기기 대신 슬라이싱으로 밀착 이동
            a[pos+1:i+1] = a[pos:i]
            keys[pos+1:i+1] = keys[pos:i]
            a[pos] = ai
            keys[pos] = ki

    def count_run_and_make_ascending(a: List[T], keys: List[object], lo: int, hi: int) -> int:
        # a[lo:run_hi)까지 단조증가 run 탐지. 감소 run이면 뒤집어서 증가로 만든다.
        run_hi = lo + 1
        if run_hi == hi:
            return run_hi
        # 증가/감소 판정
        if keys[run_hi] < keys[lo]:  # 감소 run
            run_hi += 1
            while run_hi < hi and keys[run_hi] < keys[run_hi - 1]:
                run_hi += 1
            # 뒤집기 (안정성 유지: run 내부 상대순서가 뒤집혀도 '증가'가 되도록)
            a[lo:run_hi] = reversed(a[lo:run_hi])
            keys[lo:run_hi] = reversed(keys[lo:run_hi])
        else:  # 증가 run (동점 포함)
            while run_hi < hi and keys[run_hi] >= keys[run_hi - 1]:
                run_hi += 1
        return run_hi

    def merge(a: List[T], keys: List[object], lo: int, mid: int, hi: int) -> None:
        # 안정 병합: a[lo:mid] 와 a[mid:hi]는 개별적으로 정렬됨.
        # 더 짧은 쪽만 버퍼로 사용해 메모리를 아낀다.
        left_len = mid - lo
        right_len = hi - mid
        if left_len <= right_len:
            left_a = a[lo:mid]
            left_k = keys[lo:mid]
            i = 0
            j = mid
            p = lo
            while i < left_len and j < hi:
                # 안정성: == 이면 왼쪽(run) 먼저
                if left_k[i] <= keys[j]:
                    a[p] = left_a[i]
                    keys[p] = left_k[i]
                    i += 1
                else:
                    a[p] = a[j]
                    keys[p] = keys[j]
                    j += 1
                p += 1
            # 왼쪽 잔여 복사
            if i < left_len:
                a[p:p + (left_len - i)] = left_a[i:left_len]
                keys[p:p + (left_len - i)] = left_k[i:left_len]
            # 오른쪽 잔여는 이미 제자리에 있음
        else:
            right_a = a[mid:hi]
            right_k = keys[mid:hi]
            i = mid - 1
            j = len(right_a) - 1
            p = hi - 1
            while i >= lo and j >= 0:
                # 안정성: == 이면 왼쪽(run)이 먼저였으므로, 뒤에서 합칠 땐 오른쪽이 '뒤'로 간다.
                if keys[i] > right_k[j]:
                    a[p] = a[i]
                    keys[p] = keys[i]
                    i -= 1
                else:
                    a[p] = right_a[j]
                    keys[p] = right_k[j]
                    j -= 1
                p -= 1
            # 오른쪽 잔여 복사(뒤에서 앞으로)
            if j >= 0:
                a[lo:lo + (j + 1)] = right_a[:j + 1]
                keys[lo:lo + (j + 1)] = right_k[:j + 1]
            # 왼쪽 잔여는 이미 제자리

    # -------- main pipeline --------
    minrun = compute_minrun(n)
    runs: List[Tuple[int, int]] = []  # (lo, length)

    lo = 0
    while lo < n:
        run_hi = count_run_and_make_ascending(a, keys, lo, n)
        run_len = run_hi - lo
        # run 길이가 너무 짧으면 minrun까지 확장(이진삽입)
        if run_len < minrun:
            forced_hi = min(n, lo + minrun)
            binary_insertion_sort(a, keys, lo, forced_hi, run_hi)
            run_hi = forced_hi
            run_len = run_hi - lo
        runs.append((lo, run_len))
        lo = run_hi

    # 단순 병합(작은 run부터 인접 병합).  // 실제 팀소트는 스택 불변식으로 더 세련되게 병합 순서를 정한다.
    # 그래도 안정/효율은 충분히 교육용으로 체감 가능.
    while len(runs) > 1:
        # 가장 짧은 인접 쌍을 찾아 병합(힙 없이 O(k) 스캔)
        best_i = 0
        best_len = float("inf")
        for i in range(len(runs) - 1):
            cur = runs[i][1] + runs[i + 1][1]
            if cur < best_len:
                best_len = cur
                best_i = i
        lo, L = runs[best_i]
        mid = lo + L
        _, R = runs[best_i + 1]
        hi = mid + R
        merge(a, keys, lo, mid, hi)
        # 병합한 두 run을 하나로 치환
        runs[best_i:best_i + 2] = [(lo, L + R)]
        # 이후 인접 run들의 인덱스가 당겨짐

    return a


import sys
database = []
for _ in range(int(sys.stdin.readline())):
    word:str = sys.stdin.readline().strip() # 띄어쓰기도 계산에 들어갈 수 있음.
    if word in database:
        continue
    database.append(word)
for word in timsort_lite(database, key=lambda s: (len(s), s)):
    print(word)