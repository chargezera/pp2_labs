def even_number_generator(n):
    for i in range(2, n, 2):
        yield i

n = int(input("Enter a number: "))

for num in even_number_generator(n):
    print(num)