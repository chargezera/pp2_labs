def num_countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter a number: "))

print("Countdown from", n, "to 0:")
for num in num_countdown(n):
    print(num)