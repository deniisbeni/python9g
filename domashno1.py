#1задача
num = int(input("Enter a number: "))
n = 1
n1 = 1
print(n, n1, end=" ")
if num >= 1:
    for i in range(1, num - 1):
        next_num = n + n1
        print(next_num, end=" ")
        n = n1
        n1 = next_num
#Не разбрах задачата дали трябва да е до 10то число на фибоначи или до числото което се въвежда потребителя. 

#2задача
num = int(input("Enter a number: "))
first = True
for i in range(1, num + 1):
    if num % i == 0:
        if i % 2 != 0:
            if first:
                print(i, end=" ")
                first = False
            else:
                print(i, end=" ")