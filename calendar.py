# prints calendar
# import calendar
# 
# year=int(input("Enter the year: "))
# month=int(input("Enter the month: "))
# 
# print(calendar.month(year,month))
# 


# Python program to find Largest of 2 Numbers
# def nums(a,b):
    # if a>b:
        # print(a)
    # else:
        # print(b)
# 
# nums(2,4)

# Python program to Print Natural number 1 to N
# def natural(n):
    # for i in range(1,n+1):
    #  print(i)
# natural(5)

# leap year
# year=int(input("Enter a number:"))
# if year%4==0 and year%100!=0 and year%400==0:
    # print (f"{year} is a leap year")
# else:
    # print(f"is not a leap year")
# 



# Python Program to Print Negative Numbers in a Range
# min=int(input("Enter a number: "))
# max=int(input("Enter a number: "))
# 
# for i in range(min,max+1):
    # if i<0:
    #  print(i)



# Python Program to Print Positive Numbers in a Range
# min=int(input("Enter a number: "))
# max=int(input("Enter a number: "))
# 
# for i in range(min,max+1):
#    if i>=0:
    # print(i)
# 

# min=int(input("Enter a number:"))
# max=int(input("Enter a number:"))
# Python Program to Print Positive Numbers and negative numbers
# in a range
# def nums(a,b):
    # negative_nums=0
    # positive_nums=0
    # for i in range(a,b):
        # if i<0:
            # negative_nums+=1
        # else: 
        #    positive_nums+=1
    # print(positive_nums)
    # print(negative_nums)
# nums(-9,4)
# 

# def profit_loss( actual_cost,sale_cost):
    # if actual_cost>sale_cost:
        # loss=actual_cost-sale_cost
        # print(f"Your loss is {loss}")
# 
    # elif sale_cost>actual_cost:
    #    profit=sale_cost-actual_cost
    #    print(f"your profit is {profit}")
# 
    # 
# profit_loss(2000,10000)
    
#  Python to display the Factorial of a number.
# def factorial():
    # a=int(input("Enter a number:"))
    # if a<0:
        # print(f"Should be greater than zero")
    # else:
        # multiply=1
        # for i in range(1,a+1):
            # multiply*=i
        # print(multiply)
# factorial()
        # 
# 
#
# Python program to reverse a word 
# def reverse():
    # a=input("Enter a word:")
    # x=a[::-1]
    # print(x)
# 
# reverse()
# 
# Python program to reverse a number
# def reversenum():
    # a=str(input("Enter a number:"))
    # h=a[::-1]
    # print(h)
# reversenum()

# Python program to reverse a number

# sum=0
# 
# a=int(input("Enter a number:"))
# while a!=0:
    # rem=a%10
    # sum=(sum*10)+rem
    # a=a//10
    # print(rem)
    

# program to print n natural number in descending order using a while loop.
# def natural_numbers():
    # a=int(input("Enter range:"))
    # while (a!=0):
        # print(a,end=" ")
        # a=a-1
# natural_numbers()

# program to display the first 7 multiples of 7
# def multiples():
#    count=0
#    for i in range(200):
    #    if i%7==0:
        #    print(i,end=" ")
        #    count+=1
        #    if i==8:
            #    break

# multiples()


# program that appends the square of each number to a new list.
# def square():
    # x=[2,3,4,5,6,7,8,9,10]
    # y=[]
    # for i in x:
        # y.append(i**2)
    # print(y)
# 
# square()
# 


# program where values are squares of keys
# def nums():
    # x={i:i**2 for i in range(1,15)}
    # print(x)
# 
# nums()


# 

# print a python prog to create a dict form two lists without losing
# duplicate values

# def dict():
    # a=["a","b","c","d"]
    # b=[1,2,3,4]
    # my_dict={ }
    # for i in a:
        # for m in b:
            # my_dict[m]=b
        # print(my_dict)
# 
# dict()

# or
# a=["a","b","c","d"]
# b=[1,2,3,4]
# w=dict(zip(a,b))
# print(w)
# 

#min and max values in a dictionary
# def item():
    # a={"a":1,"b":2,"c":3,"d":4}
    # y=a.values()
    # print(min(y))
    # print(max(y))
# 
# item()

# factorial of a number
# def factorial():
#  
#  a=int(input("Enter a number:"))
#  if a<0:
    #  print(f"Should be greater than zero")
#  else:
    #   multiply=1
    #   for i in range(1,a+1):
        #  multiply*=i
    #   print(multiply)
# 
# factorial()

# if adictionary is empty
# dict={}
# if len(dict)==0:
    # print(f"dict is empty")
# 

# accepts lowercase words and returns uppercase words
# def words(word):
    # y=word.upper()
    # print(y)
# words("laura")
# 

# takes in radius and returns the area of the circle
# def area(r):
    # A=3.14*r**2
    # print(A)
# area(4)
# 

#separates the positive and negative numbers in a list
# def positve_neg():
#  a=[1,2,3,4,5,6,7,-8,-4,-3,-2]
#  z=[]
#  y=[]
#  for i in a:
    #  if i<0:
        #  z.append(i)
        # 
    #  else:
        #  y.append(i)
#  print(z)
#  print(y)
# positve_neg()
 
# Concatenate two lists index-wise
# def conc():
    # list1=["M","na","i","Ke"]
    # list2=["y","me","s","lly"]
    # list3=[i+j for i,j in zip(list1,list2) ]
    # print(list3)
    # 
# conc()

# Concatenate two lists in the following order 
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# list1=["Hello","take"]
# list2=["Dear","sir"]
# list3=[i+j for i in list1 for j in list2]
# print(list3)

# or

# list1=["Hello","take"]
# list2=["Dear","sir"]
# for k in list1:
    # for l in list2:
        # w=k+l
        # print(w,end="")

# Given a two Python list. Write a program to iterate both
# lists simultaneously and display items from list1 in original
# order and items from list2 in reverse order.

# list1=[10,20,30,40]
# list2=[100,200,300,400]
# 
# reverse_list=list2[::-1]
# list3=[i,j for i,j in zip(list1,list2)]
# 
#Make the first half of a sentence uppercase and the last half lowercase.
# list="Alinda is beautiful"
# split=len(list)//2
# sentence1=(list[0:split]).upper()
# sentence2=list[split:]
# print(sentence1+sentence2)
# 

# convert two lists into a dict
# keys=["a","b","c","d"]
# values=[2,4,6,8]
# new_dict=dict(zip(keys,values))
# print(new_dict)

# or
# keys=["a","b","c","d"]
# values=[2,4,6,8]
# numbers={}
# for k in keys:
    # for i in values:
        # numbers[k]=i
# print(numbers)


# Merge two dictionaries into one 
# a={"a":1,"b":2,"c":3}
# b={"d":5,"e":6,"f":7}
# new_dict={**a,**b}
# print(new_dict)
        # 

# or
# a={"a":1,"b":2,"c":3}
# b={"d":5,"e":6,"f":7}
# a.update(b)
# print(a)
# 


#Print the value of key ‘history’ from the below
# sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80 }}}}
# print(sampleDict["class"]["student"]["marks"]["history"])
# 

# Initialize dictionary with default values
# employees = ['Kelly', 'Emma']
# defaults ={"designation": 'Developer', "salary": 8000}
# new_dict=dict.fromkeys(employees,defaults)
# print(new_dict)

# employees = ['Kelly', 'Emma']
# defaults ={"designation": 'Developer', "salary": 8000}
# new_dict=dict.fromkeys(employees,defaults)
# print(new_dict["Kelly"])


# a={"c":1,"b":2,"a":3}
# y=sorted(a)
# print(y)
 

# new list without repeated items
# b=[2,3,4,5,2] 
# s=[]
# for i  in b:
    # if i not in s:
        # s.append(i)
# 
# print(s)
 
# modulus
# def modulus():
    # f=[2,3,4,5,6,7,8]
    # for i in f:
    #    print(i%3)
# 
# modulus()



#  Create a dictionary by extracting the keys from a given dictionary
# a={"c":1,"b":2,"a":3}
# keys=["c","a"]
# res=dict()
# for k in keys:
#    res.update({k:a[k]})
# print(res)



# or
# a={"c":1,"b":2,"a":3}
# keys=["c","a"]
# z={k:a[k] for k in keys}
# print(z)

# delete a list of keys from a dictionary
# a={"c":1,"b":2,"a":3}
# keys=["c","a"]
# for k in keys:
    # a.pop(k)
# print(a)
# 
# 
# Rename key of a dictionary
# a={"c":1,"b":2,"a":3}
# a["e"]=a.pop("c")
# print(a)

# Get the key of a minimum value from the following dictionary
# sample_dict = {'Physics': 82,'Math': 65,'history': 75}
# print(min(sample_dict, key=sample_dict.get))

# Change value of a key in a nested dictionary
# sample_dict = {
    # 'emp1': {'name': 'Jhon', 'salary': 7500},
    # 'emp2': {'name': 'Emma', 'salary': 8000},
    # 'emp3': {'name': 'Brad', 'salary': 6500}
# }
# sample_dict["emp1"]["name"]="laura"
# print(sample_dict)
# 


# Change key of a value in a nested dictionary
# sample_dict = {
#   'emp1': {'name': 'Jhon', 'salary': 7500},
#   'emp2': {'name': 'Emma', 'salary': 8000},
#   'emp3': {'name': 'Brad', 'salary': 6500}
# }
# new_value=sample_dict(7500, sample_dict.get)


# 27/06/22
# 1 # Write a python function tht takes one argument as a list a=[2,4,6,8] and removes the second last item from the list and returns the whole list without the removed item
# def lists():
    # list =[2,4,6,8]
    # list.remove(6)
    # print(list)
# 
# lists()
# or
# def lists():
    # list =[2,4,6,8]
    # list.pop(-2)
    # print(list)
# 
# lists()
# 2 # WAPP that has a list days =["Monday","Tuesday","Friday","Monday"] and counts the number of occurences of monday

# days=["Monday","Tuesday","Friday","Monday"]
# print(days.count("Monday"))
# 
# 3 #WAPP named smallest that accepts a list of unsorted integers and returns the smallest number in the list.Example:
# a. smallest([3,6,8,2,4,1,5,7])returns 1
# 

# small=[10,5,2,4,1,6,8,2,9]
    #   return min(small)

# 4 # WAPf named divisible_by_seven that using the range function and a for loop returns a list containing numbers between 100 and 200 that are divisible by seven
 
 
# def divisible_by_seven ():
    # s=[]
    # for a in range(100,200):
        # if a%7==0:
            # s.append(a)
        # print(s)
# divisible_by_seven ()


# WAPP that takes two inputs (as integers) from a user and adds the 2 numbers , checks if the sum is greater than 10,less than 10 or equal to 10 and prints a statement after each check

# number=int(input("Enter a number:"))
# number2=int(input("Enter a number:"))
# sum=number+number2
# if sum>10:
    # print(f"{sum} is greater than 10")
# elif sum<10:
    # print(f"{sum} is less than 10")
# else:
    # print(f"{sum} is equal to 10")
# 
# 
# Given an integer array sorted in non-decreasing order, return an array of
# the squares of each number sorted in non-decreasing order

# a=[2,2,2,3]
# y=[i**2 for i in a]
# y.sort()
# print(y)

# 28/06/22
# Python example to access List Index and Values
# list=[2,3,4,5,6]
# for i in range(len(list)):
    # print("Index is= ", i, "value= ", list[i])
# 

# Python Program to Add two Lists
# list1=[2,3,4,5,6]
# list2=[5,0,9,10,6]
# total=[]
# 
# for i in range(3):
    # total.append(list1[i] + list2[i])
# 
# print(total)
# 
    
#Python example for Arithmetic Operations on Lists 
# list1=[2,4]
# list2=[12,14]
# add=[]
# subtract=[]
# multiply=[]
# mod=[]
# div=[]
# expo=[]
# 
# for i in range(2):
    # add.append(list1[i]+list2[i])
    # subtract.append(list1[i]-list2[i])
    # multiply.append(list1[i]*list2[i])
    # mod.append(list1[i]%list2[i])
    # div.append(list1[i]//list2[i])
    # expo.append(list1[i]**list2[i])
# 
# print(add)
# print(subtract)
# print(multiply)
# print(mod)
# print(div)
# print(expo)
# 
    
# Python Program to Calculate the Average of List Items
# list1=[2,4]
# sum=0
# for i in list1:
#    sum+=i
#    average=sum//len(list1)
# print(average)


# Python example to check List is Empty or Not
# a=[]
# if len(a)==0:
#  print(True)
# 
# else:
#  print(False)
# 

# Python example to Clone or Copy a List
# list1=[2,4]
# print("Original List= ",list1)
# print("Original List= ",type(list1))
# 
# new_list=list(list1)
# print("New List= ",new_list)
# print("New List= ",type(new_list))
# 

# Python program to Count Even and Odd Numbers in a List
# list1=[2,4,5,7,8,2,1]
# count_even=0
# count_odd=0
# for i in list1:
    # if i%2==0:
    #   count_even+=1
    #   
    # else:
        # count_odd+=1
# print(f"Even numbers are{count_even}")        
# print(f"Odd numbers are {count_odd}")
        


   