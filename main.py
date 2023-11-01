import random

numbers = [i for i in range(10)]

ans = - 1
fn = 7

start = 0
end = len(numbers) - 1
while start < end:
    input
    if fn == numbers[(end + start)//2]:
        ans = (end - start)//2
        break
    elif fn > numbers[(end - start) //2]:
        end = (end - start)//2 - 1
    else:
        start = (end - start)//2 + 1
        print(ans)
input()
