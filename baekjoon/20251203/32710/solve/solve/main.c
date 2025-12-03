#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	// 구구단 표는 A x B = C 형태로 이루어져있다.
	// 구구단은 2단부터 9단 까지 있다.

	// 양의 정수 N이 주어졌을 때, 해당 수가 구구단 표에서 등장하는지 판별해보자.
	// 1 <= N <= 100
	// 최대 양의 정수는 9 x 9 = 81 임.

	// 나머지로 계산해볼까.
	// 몫이 9 이상이면 0.
	int is_visible = 0;
	int N;

	scanf("%d", &N);

	if (N <= 9) {
		is_visible = 1;
	}
	else {
		int index;
		for (index = 2; index <= 9; index++) {
			// 1. 나누어 떨어지는가? (약수)
			// 2. 몫이 9이하인가? (구구단은 9까지만)
			// 2. 몫이 1이상인가? (자연수 나눗셈)
			if (N % index == 0) {
				int qutient = N / index;
				if (qutient <= 9 && qutient >= 1) {
					is_visible = 1;
					break;
				}
			}
		}
	}
	if (is_visible) {
		printf("1\n");
	}
	else {
		printf("0\n");
	}
	return 0;
}