def star(n):

    num = 1

    for i in range (0, num):
        for j in range (0, i):
            print(num, end = " ")
            num += 1

print(star(5))
print("Here are half pyramid.")