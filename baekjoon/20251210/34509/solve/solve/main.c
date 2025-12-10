#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	// N 은 2자리 수.
	for (int n = 10; n < 100; n++) { // 10 - 99
		int tens_place = (n / 10);
		int ones_place = (n % 10);
		int reverse_n = (ones_place * 10) + tens_place;
		// N을 문자열로 보고 뒤집었을 때 얻는 수는 4의 배수. 
		// (단, 뒤집었을 때 가장 앞의 0은 무시.)
		// n = 40 -> 04 % 4 == 0 > true
		if (reverse_n % 4 == 0) {
			// N의 각 자리 수의 합은 6의 배수.
			if ((tens_place + ones_place) % 6 == 0) {
				// N에는 숫자 8이 없다.
				if (tens_place != 8 && ones_place != 8) {
					printf("%d\n", n);
					return 0;
				}
			}
		}
	}
	return 0;
}