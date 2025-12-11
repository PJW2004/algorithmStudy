#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

// 10^100 -> 1뒤에 0이 100개 (총 101자리)
// C 언어의 문자열 특성(\0) 추가
#define MAX_LEN 105

char P[MAX_LEN];
int K;

// 문자열 나눗셈(BigInt Modulo Small Int)
// remainder = (remainder * 10 + current_digit)%divisor
// 이 방식의 시간 복잡도는 O(L * K) 이다. (L은 문자열 길이, K는 나눌 수).

// 큰 수(문자열)를 작은 수(int)로 나눈 나머지를 반환
// 반환값이 0이면 나누어 떨어진다는 뜻
int check_modulo(char* big_int, int divisor) {
	int remainder = 0;

	for (int i = 0; big_int[i] != '\0'; i++) {
		// 현재 자릿수의 숫자를 가져옴 ('0'을 빼서 정수로 변환)
		int current_digit = big_int[i] - '0';

		// 이전 나머지 * 10 + 현재 숫자
		// 그리고 다시 divisor로 나눈 나머지를 구함
		remainder = (remainder * 10 + current_digit) % divisor;
	}
	return remainder;
}

int main() {
	// 개인마다 어떤 특정한 소수 p와 q를 주어 두 소수의 곱 pq 를 비밀 키로 둔다.
	// 두 소수 p, q 중 하나라도 K보다 작은 암호는 좋지 않은 암호로 간주하여 제출하지 않음.
	// 두 소수의 곱으로 이루어진 N 과 K 가 주어져 있을때,
	// 그 암호가 좋은 암호인지 좋지 않은 암호인지 구하는 프로그램을 작성하여야 한다.
	// P(4 <= P <= 10^100)
	// K(2 <= K <= 10^6)
	// GOOD 인경우 GOOD
	// BAD 인경우 P,Q 중 가장 작은 소수.

	// 브루트 포스로는 p, q 둘다 구하겠네.
	scanf("%s %d", P, &K);

	for (int i = 2; i < K; i++) {
		if (check_modulo(P, i) == 0) {
			printf("BAD %d\n", i);
			return 0;
		}
	}
	printf("GOOD\n");

	return 0;
}