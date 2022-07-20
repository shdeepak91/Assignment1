#reverse a word:
a = input("Enter a word: ")
b = ""
for i in range (len(a)):
  b = a[i] + b
print(b)