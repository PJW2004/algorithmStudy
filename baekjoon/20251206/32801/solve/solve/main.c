#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	// 입력
	// 세개의 integer 이 주어짐 (n,a,b)
	// (1<=n,a,b<=10^6)
	int n, a, b;
	scanf("%d %d %d", &n, &a, &b);

	// 조건
	// 1 부터 n 까지 나오는 숫자 i 로 부터.
	// 만약 a,b 둘로 i가 나뉘어 진다.	-> "FizzBuzz"
	// 만약 a로 i 가 나뉘어 진다.		-> "Fizz"
	// 만약 b로 i 가 나뉘어 진다.		-> "Buzz"
	int countFizzBuzz = 0;
	int countFizz = 0;
	int countBuzz = 0;
	
	int i;
	for (i = 1; i <= n; i++) {
		if ((i % a == 0) && (i % b == 0)) {
			countFizzBuzz += 1;
		}
		else if (i % a == 0) {
			countFizz += 1;
		}
		else if (i % b == 0) {
			countBuzz += 1;
		}
	}
	printf("%d %d %d", countFizz, countBuzz, countFizzBuzz);

	// 출력
	// "Fizz" 가 출력된 횟수 / "Buzz" 가 출력된 횟수 / "FizzBuzz" 가 출력된 횟수
	return 0;
}