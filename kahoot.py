from binascii import a2b_hex


def pattern():
    n=int(input("Enter a number"))
    for i in range(n):
        for j in range(i):
            print(i,end=" ")
            print("\n")
def nums():
    a=int(input("Enter value a:"))
    b=int(input("Enter value b:"))
    print(f"\n a is {a} b is {b}")
    a=a+b
    b=a-b
    a=a-b

    print("\n")
    print(f"a is {a} b is {b}")

    nums()
    
# def number():
    
#     even_numbers=0
#     odd_numbers=0
    
#     for x in range(10,55):
#         if x%2==0:
#          even_numbers+=1
#         print(f"The even numbers are {even_numbers} ")
#         else:
#          odd_numbers+=1
#         print(f"The odd numbers are {odd_numbers} ")
# number()          

def number(numm,numm2):
    even=0
    odd=0
    for x in range(numm,numm2):
        if x%2==0:
            even+=1
            return even
        else:
            odd+=1
            return odd 
   
   
def nums():
    even=0
    odd=0
    for x in range(10,55):
        if  x%2==0:
            even+=1
            count(even)

        else:
            odd+=1
            count(odd)

    nums()

def map():
    key=["name","age","job"]
    values=["Laura",20,"ui/ux deisgner"]

    my_dict={k:v for k,v in zip(key,values)}
    print(my_dict)
   
  
# a=int(input("Enter a number:")) 
# b=int(input("Enter a number:")) 
# 
# choice={
    # '1':a+b,
    # '2':a-b
# }
# z=input("Press 1 for Add & 2 for subtract")
# print(choice.get(z))


# def acc(v1,v2,t1,t2):
    # a=((v2-v1)/(t2-t1))
    # return a
# 
# def numz():
    # val1=int(input("Enter a number:"))
    # val2=int(input("Enter a number:"))
    # val3=int(input("Enter a number:"))
# 
    # print(val1,val2,val3)
    # a=[]
    # a.append(int(val1))
    # a.append(int(val2))
    # a.append(int(val3))
# 
    # a.sort()
    # 
    # print(a)
# 
 

# val1=input("Enter a number:")
# a=[]
# while len(val1)<3:
    # a.append(int(val1))
    # a.sort()
# print(a)

# def grp():
    # for x in range(1,25):
    #   if x%5==0:
        # continue
    #   else:
        # print (x)
# grp()
        # 
# 
# def word():
    # a=[2,3,4,6,6,6,7]
    # z=a.count(6)
# 
    # print(z) 
# 
# word()
# 
     
# a="Adam s a boy.Adam loves food"
# z=input("Enter a word you want to check: ")
# y=a.split()
# for i in y:
    # if i==z:
        # print(a.count(i))
# 

# def even_odd():
    # a=[9,94,5,6,3,4,5,2,8,7]
    # for i in a:
        # if i%2==0:
        #  print("even")
        # else:
        #  print("odd")
# even_odd()

# def nums(a,b):
    # multiple=a*b
    # sum=a+b
    # if multiple>500:
        # print(multiple)
    # else:
        # print(sum)
# 
# nums(7,100)

# def greatest(a,b,c):
    # if a>b and a>c:
        # print(a)
    # elif b>a and b>c:
        # print(b)
    # else:
        # print(c)
# greatest(2,10,6)

# def multiple():
    # for a in range(10,50):
        # if a%5==0:
            # print (a, end=" ")
# 
        # 
        # 
# multiple()

# def laura():
    # a=[3,4,5,6,7,8]
    # if a[0]==a[-1]:
        # print(True)
    # else:
        # print(False)
# 
# laura()

# def far_celcius(f):
    # c=(f-32)*(5/9)
    # print(c)
# far_celcius(50)
# 

# w=int(input("Enter a number: "))
# for a in range(w):
    # for i in range (a):
        # print(i,end=" ")
    # print("\n")


# def pattern(fh):
    # for a in range(fh):
        # for x in range (a):
            # print("*",end=" ")
        # print("\n")
# 
# pattern(6)

# def factorial():
    # n=int(input("Enter a number: "))
    # if n<=0:
        # print("Number should be greater than zero")
    # else:
        # multiply=1
        # for i in range(1,n+1):
            # multiply*=i
        # print(multiply)
# 
# factorial()
        #    
# 

# def factorial():
    # n=int(input("Enter a number: "))
    # if n<=0:
        # print("Number should be greater than zero")
    # else:
        # multiply=1
        # for i in range(1,n+1):
            # multiply*=i
        # print(multiply)
# 
# factorial()
    # 
# 

# w=input("Enter a word: ")
# t= w[::-1]
# print (t)


# def greet(*names):
    # for x in names:
        # print(f"Hello{x}")
# greet("laura","alinda","kengaaju")
# 
# 

# def sum(*numbers):
    # total=0
    # for number in numbers:
        # total+=number
    # print(total)
# 
# sum(3,4,5,6,5)

# def multiply(*numbers):
    # multiple=1
    # for number in numbers:
        # multiple*=number
    # print(multiple)
# multiply(2,3,4,5,5)

# def greet(**kwargs):
    # print(kwargs)
# 
# greet(name="laura",age=75)

# def greet(**kwargs):
    # keys=kwargs.keys()
    # values=kwargs.values()
    # print(keys)
    # print(values)
# 
# greet(name="laura",age=75)
# 

# def greet(**kwargs):
    # keys=kwargs.keys()
    # if "country" in keys:
        # print(f"hello {kwargs['name']} you are from {kwargs['country']}")
# 
    # elif "age" in keys:
        # year=2022-kwargs['age']
        # print(f"hello {kwargs['name']} you were born in {year}")
# 
    # else:
        # return f"Hello anonymous"
# 
# greet(name="alinda",age=21)
# 
# 

# def greet(**kwargs):
    # keys=kwargs.keys()
    # if "country" in keys:
        # print(f"Hello {kwargs['country']} you are from {kwargs['country']}")
# 
    # elif "age" in keys:
        # year=2022-kwargs['age']
        # print(f"Hello {kwargs['name']} you were born in {year}")
# 
# greet(name="laura",age=34)

# def greet(**kwargs):
    # keys=kwargs.keys()
    # values=kwargs.values()
    # if "laura" in values:
        # print(f"Hello {kwargs.keys()}")
# 
# greet(name="laura",age=21)

# class Student:
    # school="AKirachix"
    # def __init__(self,name,age,country):
        # self.name=name
        # self.age=age
        # self.country=country
# 
    # def greet(self):
        # return f"Hello {self.name} you are from {self.country}"


# def odd():
    # for i in range(100):
        # if i%2!=0:
            # print(f"{i} is odd")
# 
# odd()
# 
# def factorial():
    # n=int(input("Enter a number:"))
    # if n<=0:
        # print("number should be greater than zero")
    # else:
        # multiply=1
    # for i in range(1,n+1):   
        # multiply*=i
    # print (multiply)
# 
# factorial()
#

# def word():
    # n=input("Enter a word: ")
    # j=n[::-1]
    # print(j)
# word()
# 
 
# def number():
    # n=int(input("Enter a number: "))
    # h=n[-1]+n[0]
    # print(h)
# number()


# n=str(input("Enter a number: "))
# reverse=n[::-1]
# print(reverse)

# n=input("Enter a number: ")
# sum=0
# while n!=0:
    # rem=n%10
    # sum=(sum*10)+rem
    # n//10
    # print(sum)

# tg python programming
# print("Hello world")
# 
 
#1
# def sumation(a,b):
    # sum=a+b
    # print(sum)
# 
# sumation(3,2)

#2
# def cubes(a):
#  cube=a**3
#  print(cube)
# 
# cubes(2)

# Python program to print Calendar

# import calendar 
# 
# year=int(input("Enter a year: "))
# month=int(input("Enter a month: "))
# print(calendar.month(year,month))
# 

a=[{"name":"Winfred","amount":3000,"age":22},
{"name":"Winfred","amount":3000,"age":22},
{"name":"Winfred","amount":3000,"age":22}]


     
