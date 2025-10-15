# 정보
작성자 : 박정원 <br/>
작성일 : 2025-10-15 <br/>
링크 : https://www.acmicpc.net/problem/28702

# 풀이
이 문제의 본질은 등차수열이다. <br/>
등차수열이란, 연속된 두 항의 차이가 일정한 수열을 말한다.

예를 들어 [ 5, 6, 7, 8 ... ] 은 각 항의 차이가 1 로 일정한 등차수열이다.

문제에서 "Fizz"나 "Buzz" 같은 문자가 나오는 것은, 이 등차수열의 특정 숫자를 규칙에 따라 문자로 바꾼 것 뿐이다. <br/>
즉 이 문자들을 다시 원래 숫자로 되돌려 생각하면 된다.
## 1. 기준점 찾기와 공차($d$)의 확정
```
Print the line that should follow the given three consecutive lines. 
If there can be multiple possible answers, print any of them.
```
가장 먼저 할 일은 주어진 세 개의 입력($S_1$, $S_2$, $S_3$) 중에서 어떤 것이 숫자인지 찾는 것이다. <br/>
문제에서 셋 중 하나는 반드시 숫자라고 했으므로, 이 숫자가 우리 계산의 기준점이 된다.

|기호|요약|설명|
|--|--|--|
|$k$|기준점의 위치|첫 번째 숫자인지, 두 번째인지, 세 번째인지 위치를 나타낸다. ($k$는 1, 2, 3중 하나)|
|$v_k$|기준점의 값|그 숫자의 실제 값|

```
The following is the output of the FizzBuzz problem ...
```
그리고 이 문제의 등차수열에서 항들의 차이, 즉 공차($d$)는 항상 1이다. <br/>
왜냐하면 "FizzBuzz" 규칙 자체가 1씩 커지는 숫자들에 대해 적용되기 때문이다.

## 2. 네 번째 항($a_4$)의 숫자값 계산
이제 기준점과 공차($d$)를 이용해 원하는 네번째 항의 숫자값을 계산할 수 있다. <br/>
등차수열의 일반항 공식은 다음과 같다. <br/>
$$a_n=a_k+(a-k) \times d$$
이 수식을 문제에 맞게 해석하면 다음과 같이 된다.
|기호|설명|
|--|--|
|$a_n$|알고 싶은 n번째 항의 값. <br/>여기서는 네번째 항이므로 $n=4$ 가 된다. <br/>즉, $a_4$ 를 구하는 것이 목표.|
|$a_k$|기준점의 값, 즉 $v_k$|
|$n$|목표 항의 위치. 즉, 4|
|$k$|기준점의 위치. 1,2,3 중 하나|
|$d$|공차. 이 문제에서는 항상 1|

따라서 최종 공식은 매우 간단해진다.<br/>
$$a_4=v_k+(4-k) \times 1$$

$$a_4=v_k+(4-k)$$

## 3. 시뮬레이션
각 예시를 테스트 해본다.
### 3-1. 첫 번째 입력($S_1$)이 숫자인 경우
```
13
Fizz
Buzz
```
기준점 위치 ($k$): 1 <br/>
기준점 값 ($v_k$): 13 <br/>
계산: <br/>
$a_4=v_k+4-k$<br/>
$=13+4-1$<br/>
$=16$

### 3-2. 두 번째 입력($S_2$)이 숫자인 경우
```
Fizz
7
8
```
기준점 위치 ($k$): 2 <br/>
기준점 값 ($v_k$): 7 <br/>
계산: <br/>
$a_4=v_k+4-k$<br/>
$=7+4-2$<br/>
$=9$

### 3-3. 세 번째 입력($S_3$)이 숫자인 경우
```
Buzz
Fizz
22
```
기준점 위치 ($k$): 3 <br/>
기준점 값 ($v_k$): 22 <br/>
계산: <br/>
$a_4=v_k+4-k$<br/>
$=22+4-3$<br/>
$=23$

### 4. 계산된 숫자에 FizzBuzz 규칙 적용
- $i$ is a multiple of both $3$ and $5$, print “FizzBuzz”.
- If $i$ is a multiple of $3$ but is not a multiple of $5$, print “Fizz”.
- If $i$ is not a multiple of $3$ but is a multiple of $5$, print “Buzz”.
- If $i$ is neither a multiple of $3$ nor $5$, print $i$ itself.