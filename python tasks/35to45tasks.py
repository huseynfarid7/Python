#task 035
name=input("enter your name: ")
for g in range(3):
    print(name)

#task 036
name=input("enter your name: ")
number=int(input("Enter the number: "))
for g in range(number):
    print(name)

#task 037
a=str(input("enter your name: "))
for g in a:
    print(g)

#task 038
a=str(input("enter your name: "))
b=int(input("enter the number: "))
for g in a*b:
    print(g)

#task 039
a=int(input("enter a number between 1 and 12: "))
if a >=1 and a<12:
 for g in range(1,11):
  print(a,'x', g ,'=',a*g)
else:
 print("the number you entered isn't among 1 and 12")

#task 040
a=int(input("give me a number below 50: "))
if a<50:
 for g in range(a):
  print(g+1)
else:
 print("the number is too high")

#task 41
a=input("enter your name: ")
b=int(input("enter a number: "))
c="too high"
if b<10:
    for g in range(b):
        print(a)
else:
    for g in range(3):
        print(c)

#task 42 -

#task 43
answer=input("which direction you want to count[up or down]? ")
if answer == "up":
   a=int(input("please enter the top number you want: "))
   for g in range(a):
       print(g+1)
elif answer == "down":
    b=int(input("please enter a number below 20: "))
    for g in range(20,b, -1):
        print(g)
else:
    print("I don't understand")

#task 44 -

# task uni
print("Enter correct password to continue ")
num=2
count=0
while count < 3:
    password = input("Enter password: ")
    if password=='abc37810':
        print("Access granted")
        break

    elif num== 0:
        print("Too many attempts,you are locked out")
        break

    else:
        print(f"Access denied.you have {num} attempts left,try again.")
        num=num-1