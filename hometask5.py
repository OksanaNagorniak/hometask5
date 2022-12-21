# 1.Вывести треугольник #1 с шириной N с помощью цикла while
print("start triangle 1")
N = 5
d = "*"
print(N * d)
while N != 1:
    N -= 1
    print(N * d)

print("end triangle 1 \n \n \n")
# 2. Вывести треугольник #2 с шириной N с помощью цикла while
print("start triangle 2")
N = 1
d = "*"
print(N * d)
while N != 5:
    N += 1
    print(N * d)
print("end triangle 2 \n \n \n")

# 3. Вывести треугольник #3 с шириной N с помощью цикла while
print ("start triangle 3")
N = 5
d = "*"
k = " "
a = 0
print(N*d)
while N != 1:
    N -= 1
    a += 1
    print((k * a) + (N*d))
print("end triangle 3 \n \n \n")
# 4. Вывести треугольник #4 с шириной N с помощью цикла while
print ("start triangle 4")
N = 1
d = "*"
k = " "
a = 5
print((k*a) + (d*N))
while N != 5:
    N += 1
    a -= 1
    print((k*a)+(N*d))
print("end triangle 4")

