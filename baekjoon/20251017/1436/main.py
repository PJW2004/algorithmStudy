n = int(input())
start_number = 666
count = 1
while 1:
    if count == n:
        break
    start_number += 1
    if "666" in str(start_number):
        count += 1
print(start_number)