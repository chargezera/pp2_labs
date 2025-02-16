def squares_generator(N):
    for i in range(N + 1):
        yield i ** 2

num = int(input("Enter the number to generate to: "))
for square in squares_generator(num):
    print(square)