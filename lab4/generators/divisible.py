def div_3_and_4(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))

for num in div_3_and_4(n):
    print(num);