# 정보
작성자 : 박정원 <br/>
작성일 : 2025-10-16 <br/>
링크 : https://www.acmicpc.net/problem/1181

# 풀이
```python
database = {}
for _ in range(int(input())):
    word:str = input()
    word_count:int = sum([ord(character) * len(word) 
                        for character in word]) # 길이에 대한 가중치도 제공하자.
    database[word] = word_count # 중복된 단어는 하나만 남기고 제거.
for word, _ in sorted(database.items(), key=lambda x: x[1]):
    print(word)
```
처음에는 각 단어에 대한 아스키코드로 계산 후 문자 길이에 대한 가중치를 제공해주면 될 것 같았다.
