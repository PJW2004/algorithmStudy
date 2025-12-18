#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>

bool visited[10]; 
int sequence[10];
void dfs(int index, int n, int m) {
	if (index == m) {
		for (int i = 0; i < m; i++) {
			printf("%d ", sequence[i]); // 수정됨: m이 아니라 배열 sequence[i]를 출력
		}
		printf("\n"); // 줄바꿈
		return;
	}
	for (int i = 1; i <= n; i++) {
		visited[i] = true; 
		sequence[index] = i;
		dfs(index + 1, n, m);
		visited[i] = false;
	}
}

int main() {
	// N 과 M이 주어진다.
	// N 은 자연수
	// M 은 크기
	// 1 <= M <= N <= 7
	int n, m;
	scanf("%d %d", &n, &m);

	// 1부터 N까지 자연수 중에서 M개를 고른 수열
	// 같은 수를 여러번 골라도 된다.

	// 중복되는 수열을 여러 번 출력하면 안됨.
	// 각 수열은 공백으로 구분해서 출력.
	// 수열은 사전 순으로 증가하는 순서로 출력.
	dfs(0, n, m);

	return 0;
}