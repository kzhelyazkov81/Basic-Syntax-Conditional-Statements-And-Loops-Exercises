divisor = int(input())
divisible = int(input())

while True:
    result = divisible % divisor
    if result == 0:
        break
    else:
        divisible -= 1

print(divisible)
