#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	// 예약할 수 있는 교시의 개수 T
	// 1 <= T <= 1,000
	int T;

	// 건우가 예약한 교시 X
	// 1 <= X <= T
	int X;

	// 조원의 수 N
	// 1 <= N <= 10
	int N;

	scanf("%d %d", &T, &X);
	scanf("%d", &N);
	//	조원이 예약할 수 있는 교시의 개수 K_i
	//	1 <= K_i <= T
	//	참석 가능한 교시를 나타내는 K_i 개의 정수
	//	1 <= A_i,A_1 < A_i,A_2 < ... < A_i,A_Ki <= T
	int all_attend = 1;
	for (int index = 0; index < N; index++) {
		// N 명의 조원이 알려준 참석 가능한 교시에 대한 정보.
		int K; // 이번 조원이 참석 가능한 교시의 개수
		scanf("%d", &K);

		int karr[1000]; // 값을 저장할 배열
		int can_attend_this_student = 0; // 이 학생이 X교시에 올 수 있는지?

		// K번 반복하며 실제 교시 정보를 읽어서 배열에 저장
		for (int j = 0; j < K; j++) {
			scanf("%d", &karr[j]); // 공백은 scanf가 알아서 건너뛰고 숫자만 배열에 넣음

			// 입력받은 값이 건우가 예약한 X와 같은지 바로 확인
			if (karr[j] == X) {
				can_attend_this_student = 1;
			}
		}

		// 이 학생이 X교시에 올 수 없다면, 전체 결과도 실패
		if (can_attend_this_student == 0) {
			all_attend = 0;
			break;
		}
	}

	// X 교시에 모든 조원이 참석 가능? YES : NO
	if (all_attend == 1) {
		printf("YES\n");
	}
	else {
		printf("NO\n");
	}

	return 0;
}