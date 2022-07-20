
#list = [1,2,3,4,5,6,7,8,9]
n = int(input("enter the number "))

odd_count = 0
even_count = 0
i = 1
while i in range(1,n):
    if i%2 == 0 :
        even_count += 1
    else:
        odd_count += 1
    i += 1
print("Even numbers in the list :" ,even_count)
print("Odd numbers in the list :" , odd_count)

