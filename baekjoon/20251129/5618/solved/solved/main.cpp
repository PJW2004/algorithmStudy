#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    int n;
    int a[3];
    int i, j;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    // 가장 작은 값 찾기
    int min = a[0];
    for (i = 1; i < n; i++) {
        if (a[i] < min)
            min = a[i];
    }

    // 1부터 min까지 모든 수 검사
    for (i = 1; i <= min; i++) {
        int ok = 1; // 공약수인지 표시

        for (j = 0; j < n; j++) {
            if (a[j] % i != 0) {
                ok = 0;
                break;
            }
        }

        if (ok)
            printf("%d\n", i);
    }

    return 0;
}