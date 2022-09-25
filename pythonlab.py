#----------------EXPERIMENT-1
a = 5
print("Type of a: ", type(a))
b = 5.0
print("\nType of b: ", type(b))
c = 2 + 4j
print("\nType of c: ", type(c))



#-------------------------EXPERIMENT-2
num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number '))
add = num1 + num2
dif = num1 - num2
mul = num1 * num2
div = num1 / num2
floor_div = num1 // num2
power = num1 ** num2
modulus = num1 % num2
print('Sum of ',num1 ,'and' ,num2 ,'is :',add)
print('Difference of ',num1 ,'and' ,num2 ,'is :',dif)
print('Product of' ,num1 ,'and' ,num2 ,'is :',mul)
print('Division of ',num1 ,'and' ,num2 ,'is :',div)
print('Floor Division of ',num1 ,'and' ,num2 ,'is :',floor_div)
print('Exponent of ',num1 ,'and' ,num2 ,'is :',power)
print('Modulus of ',num1 ,'and' ,num2 ,'is :',modulus)





#--------------------------------EXPERIMENT 3
#-------------------AIM: Write a program to defining strings in Python.

# defining strings in Python
# all of the following are equivalent
my_string = 'Hello'
print(my_string)
my_string = "Hello"
print(my_string)
my_string = '''Hello'''
print(my_string)
# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
the world of Python"""
print(my_string)


#----------------EXPERIMENT 4
#-------------AIM: Write a python script to print the current date in the following format “Sun May 07

import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))


#-------------------EXPERIMENT 5
#-----------AIM: Write a program to create, append, and remove lists in python.

class mylist():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        self.n.remove(b)
    def dis(self):
        return (self.n)
 
obj=mylist()
 
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    choice=int(input("Enter choice: "))
    if choice==1:
        n=int(input("Enter number to append: "))
        obj.add(n)
        print("List: ",obj.dis())
 
    elif choice==2:
        n=int(input("Enter number to remove: "))
        obj.remove(n)
        print("List: ",obj.dis())
 
    elif choice==3:
        print("List: ",obj.dis())
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
 
print()

    

#---------------EXPERIMENT 6
#-------------------AIM: Write a program to demonstrate working with tuples in python

# Different types of tuples
# Empty tuple
my_tuple = ()
print(my_tuple)
# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)
# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Audisankara', 2: 'Engineering', 3: 'College'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Audisankara', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)


#------------EXPERIMENT 8
#------------AIM: Write a python program to find largest of three numbers.

# Python program to find the largest number among the three input numbers
# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12
# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
  largest = num2
else:
  largest = num3
print("The largest number is", largest)




#------------EXPERIMENT 9
#----------AIM:Write a Python program to convert temperatures to and from Celsius, Fahrenheit.

# Python Program to convert temperature in celsius to fahrenheit
# change this value for a different result
celsius = 37.5
# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))



#-------EXPERIMENT 10
#---------AIM: Python program to display all the prime numbers within an interval

lower = 900
upper = 1000
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
# all prime numbers are greater than 1
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:
        print(num)

#-------------EXPERIMENT 11
#----------------AIM: Write a Python script to print First n prime numbers.

# Python Program to print n prime number using for loop
Number = int(input(" Please Enter any Number: "))
print("Prime numbers between", 1, "and", Number, "are:")
for num in range(1, Number + 1):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:
      print(num)


#------------EXPERIMENT 12
#----------AIM: Write a Python script to multiply matrices # 3x2 matrix

X = [ [1,2],[3,4],[4,5] ]
# 2x3 matrix
Y = [ [1,2,3],[4,5,6] ]
# resultant matrix
result = [ [0,0,0],[0,0,0],[0,0,0] ]
my_list = []
# iterating rows of X matrix
for i in range( len(X) ):
  for j in range(len(Y[0])):
    for k in range(len(Y)):
      result[i][j] += X[i][k] * Y[k][j]
for r in result:
  print(r)



#----------EXPERIMENT 13
#------------AIM: Write a python program to find factorial of a number using Recursion.

# Factorial of a number using recursion
def recur_factorial(n):
  if n == 1:
    return n
  else:
    return n*recur_factorial(n-1)
num = 5
# check if the number is negative
if num < 0:
  print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
  print("The factorial of 0 is 1")
else:
  print("The factorial of", num, "is", recur_factorial(num))




#-------------EXPERIMENT 16
#----------------AIM: Write a program that inputs a text file. The program should print all of the unique

# Program to sort alphabetically the words form a string provided by the user
my_str = "Hello this Is an Example With cased letters"
# To take input from the user
#my_str = input("Enter a string: ")
# breakdown the string into a list of words
words = my_str.split()
# sort the list
words.sort()
# display the sorted words
print("The sorted words are:")
for word in words:
  print(word)



#-------------EXPERIMENT 17
#-----------AIM: Write a Python class to convert an integer to a roman numeral.

class py_solution:
  def int_to_Roman(self, num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
                  1
            ]
    syb = [
      "M", "CM", "D", "CD",
      "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
            ]
    roman_num = ''
    i = 0
    while num > 0:
      for _ in range(num // val[i]):
       roman_num += syb[i]
       num -= val[i]
      i += 1
    return roman_num
print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(4000))





#-------EXPERIMENT 18
#-----------------AIM: Write a Python class to implement pow(x, n)

class py_solution:
  def pow(self, x, n):
    if x==0 or x==1 or n==1:
      return x
    if x==-1:
      if n%2 ==0:
        return 1
      else:
        return -1
    if n==0:
      return 1
    if n<0:
      return 1/self.pow(x,-n)
    val = self.pow(x,n//2)
    if n%2 ==0:
      return val*val
    return val*val*x
print(py_solution().pow(2, -3))
print(py_solution().pow(3, 5))
print(py_solution().pow(100, 0))


#---------------EXPERIMENT 19
#-----------------AIM:Write a Python class to reverse a string word by word.

# Function to reverse words of string
def rev_sentence(sentence):
  # first split the string into words
  words = sentence.split(' ')
   # then reverse the split string list and join using space
  reverse_sentence = ' '.join(reversed(words))
  # finally return the joined string
  return reverse_sentence
if __name__ == " __main__ ":
  input = 'araknasidua'
  print rev_sentence(input)


#-----------------EXPERIMENT 20
#------------------AIM: Write a python program to define a module to find Fibonacci Numbers and import

# Program to display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms: "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
  print("Please enter a positive integer")
elif nterms == 1:
  print("Fibonacci sequence upto",nterms,":")
  print(n1)
else:
  print("Fibonacci sequence:")
  while count < nterms:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1
