#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int ds;
	int ys;
	int dm;
	int ym;

	scanf("%d %d", &ds, &ys);
	// 0 <= ds < ys <= 50
	// 태양이 올바른 위치에 있었던지 몇년전 (ds)
	// 태양이 그 위치로 돌아오는데 걸리는 시간 (ys)

	scanf("%d %d", &dm, &ym);
	// 0 <= dm < ym <= 50
	// 달이 올바른 위치에 있었던지 몇년전 (dm)
	// 달이 그 위치로 돌아오는데 걸리는 시간 (ym)

	// 달과 태양이 모두 올바른 위치에 있어야 함.
	int ss = (ys - ds) % ys;
	int sm = (ym - dm) % ym;
	// start sun / start moon

	while (ss != sm) {
		if (ss < sm)
			ss += ys;
		else
			sm += ym;
	}
	printf("%d", ss);
	return 0;
}