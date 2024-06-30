#1 print the number from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

#2 print number from 100 to 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
 
#3 print the multiplication table of number n
# n = int(input("enter the table you want to fetch? "))
# i = 1
# while i <= 10:
#     total = n * i
#     print(f" {n} * {i} = {total}")
#     i += 1
   
#4 print the elemets of the following list using a loop
# number = [1, 4, 9, 16, 25, 36, 49]
# i = 0
# while i < len(number):
#     print(number[i])
#     i += 1

   
#5    WAP Search for a number x in the tuple using loop:

# number = (1, 2, 3, 5, 7, 9, 10)
# x = int(input("Enter the number you want to find? "))

# i = 0
# while i < len(number):
#     if(number[i] == x):
#         print("Found at index", i)
#     i += 1
# else:
#     print("Not in the list")


#break element

# i = 1
# while i <= 5:
#     print(i)
#     if (i == 3):
#         break
#     i +=1
# print("loop ended")

# #continue 

# i = 0
# while i <=5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1

#=================FOR LOOP=========
# #forloop
# list = [1, 4, 9, 16, 25, 36]
# for num in list:
#     print(num)

# #WAP searach for a number x in the tuple using loop:

# num = (1, 4, 9, 16, 25, 36, 49, 64, 36)
# x = 36
# i = 0
# for el in num:
#     if(el == x):
#          print("Found at index", i)
#     i += 1
# else:
#      print("Not in the list")


#===================RANGE============================
# seq = range(5)
# for i in seq:
#     print(i)

# for i in range(2, 10, 2):
#     print(i)

# #Ques print number from 1 to 100

# for i in range(1, 101):
#     print(i)

#ques print the number from 100 to 1

# for i in range(100, 0, -1):
#     print(i)

# print the multiplication table of a number n

# numb = int(input("print the number: "))

# for el in range(1, 11):
#     final = numb*el
#     print(final)

#WAP to find the sum of first n number (using while)

# num = int(input("enter the number: "))
# sum = 0
# i = 1
# while i <= num:
#     sum += i
#     i += 1
# print("total sum =", sum)
