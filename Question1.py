# fibonacci series using while loop:

number = int(input("enter a number: "))
first = 0
second = 1
i = 0
while i <= number:
    print(first , end= " ")
    next = first + second 
    first = second 
    second = next
    i += 1