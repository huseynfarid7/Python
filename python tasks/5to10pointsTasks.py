# 0 ve 3 arasinda ededi ardicilliq yaratmaq,range funksiyasi
numbers = range(4)
for i in numbers:
 print(i)

# range funksiyasi 2 parametrli
# numbers from 2 to 4 (5 daxildeyil)
numbers = range(2, 5)
print(list(numbers))

# numbers from -2 to 3 (4 daxildeyil)
numbers = range(-2, 4)
print(list(numbers))


# range funksiyasi 3 parametrli
# 2 ve 10 ededleriaralighindaededlerin 3 vahidartmaghi
numbers = range(2, 10, 3)
print(list(numbers))

# 4 ve -1 ededleri araliginda ededlerin 1 vahid azalmagi
numbers = range(4, -1, -1)
print(list(numbers))

# numbers from 1 to 4 with increment of 1
# range(0, 5, 1) is equivalent to range(5)
numbers = range(0, 5, 1)
print(list(numbers))


#dövrün 5 dəfə təkrarlanması nümunəsi:
for i in range(5):
 print(i, 'kod')

########################################################################################################################

# sert operatoru
eded1=int(input("1ci ededi daxil edin: "))
eded2=int(input("2ci ededi daxil edin: "))
if eded1>eded2:
    print(eded2,eded1)
else:
    print(eded1,eded2)


# sert operatoru 1
a=-10
if  a<-10:
  if a==0:
    print("Verilmis eded sıfırdır")
  else:
    print("Verilmis eded menfi ededdir")
else:
    print("Verilmis eded musbetdir ")

# sert operatoru 2
a=64
if a<50:
 if a%2==0:
   print("eded cutdur")
 else:
   print("eded tekdir")
else:
   print("eded 50-den boyukdur")

###############################################################################################################

#while operatorundan istifade etmekle 2 den 35 dek ededler ardicilligindan cut ededleri ekrana cixaran kodu tertib edin
a=2
while a<35:
    if a%2==0:
        print(a,end=" ")
    a=a+1
#1 ve 100 daxil olmaqla tesadufi tam ededi ekrana cixardan kodu tertib edin.
import random
num=random.randint(1,100)
print(num)

#kvadrat
import turtle
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()

#ucbucaq
import turtle
for i in range(0,3):
    turtle.forward(100)
    turtle.left(120)

turtle.exitonclick()

#rengli olmasini isterse
import turtle
for i in ["red","green","yellow","blue"]:
    turtle.color(i)
    turtle.forward(100)
    turtle.left(90)

turtle.exitonclick()

#ic ice
a=-10
if a<= -10:
    if a==0:
        print("Verilmis eded sifirdir")
    else:
        print("Verilmis eded menfi ededdir")
else:
    print("verilmis eded musbet ededdir")

#tipden tipe kecid
x=10
y=10.01
print(type(x))
print(type(y))

x=10
z=float(x)
print("z is",z,"and is of type",type(z))

x=10
x=float(x)
print("x is",x,"and is of type",type(x))

x=50.8
x=int(x)
print("x is",x,"and is of type",type(x))

#int to str
x=12
y="23"
z=str(x)+y
print("z is",z,"and is of type",type(z))

#str to int
x="101"
z=int(x)
print("z is",z,"and is of type",type(z))

x=12
y="23"
z=x+int(y)
print("z is",z,"and is of type",type(z))

#break and continue
str="python"
for i in str:
    if i=="o":
        break
    print(i)

i=0
while 1:
    print(i," ",end="")
    i=i+1
    if i == 10:
        break
    print("netice")

for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"beraberdir",x,"*",n//x)
            break
    else:
        print(n,"sade ededdir")

num=10
while num < 100:
    num=num+10
    if num==50:
        continue
    print("Current num: ",num)

for num in range(2,10):
    if num%2==0:
        print("Cut eded",num)
        continue
    print("Tek eded",num)