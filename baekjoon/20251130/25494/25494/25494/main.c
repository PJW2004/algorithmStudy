#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	int t;
	scanf("%d", &t);
	int index;
	for (index = 1; index <= t; index++) {
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		// t 는 100 까지
		// 1 <= a, b, c <= 60

		// (x mod y) == (y mod z) == (z mod x)
		int max = a;
		if (b > max) max = b;
		if (c > max) max = c;

		// 가장 큰 수에서 구해야지.
		int x, y, z;
		int count = 0;
		for (x = 1; x <= a; x++) {
			for (y = 1; y <= b; y++) {
				for (z = 1; z <= c; z++) { 
					if (((x % y) == (y % z)) && ((y % z) == (z % x))) {
						count = count + 1;
					}
				}
			}
		}
		printf("%d\n", count);
	}
	return 0;
}