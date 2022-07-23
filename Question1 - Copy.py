# fibonacci series using while loop:

number = int(input("till what number you want to print series:"))
first = 1
second = 1
i = 0
while i <  number:
    if(first <=number):
      print(first , end= " ")
      next = first + second 
      first = second 
      second = next
    i += 1