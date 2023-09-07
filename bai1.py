print ("xin chao")
a = 1
print(a)
a = 'Hello World'
print(a)
a = [1, 2, 3]
print(a)
a = [1.2,'Hello','W', 2]
print(a)

x = 2
a = 1 < x < 3 # True
print(a)
a = 10 < x < 20 # False
print(a)
a = 3 > x <= 2 # True
print(a)
a = 2 == x < 4 # True
print(a)
#if else
b = 10
if (b>0) :
    print("b la so nho hon 0")
elif (b < 0):
    print("b la so nho hon 0")
elif (b==1) :
    print(b)
else:
    print("no")
#for... in
for x in "banana":
      print(x)
      
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#while
count = 0
while (count < 9):
    print ('The count is:', count)
    count = count + 1
print ("Good bye!")
# ham
def sum(a, b):
    return (a+b)
print (sum(4, 6))
#chuoi
str1 = "Hello"
str2 = 'world'
print (str1[0])
print (str2[0])
# noi chuoi
str = str1 + " " + str2
print (str)
#trich chuoi
print (str[0:4])
print (str[:4])
print (str[-3:])
print (str[6:-3])
#do dai cua chuoi
count = len(str)
print(count)
#tim thay the chuoi
str = 'Hello world'
newstr = str.replace('Hello','Bye')
print (newstr)
#tim chuoi con
str = 'Hello world'
print (str.find('world'))
print (str.find('Bye'))
#tach chuoi
print (str.split(' '))
#xu ly chuoi
str3 = "//space//"

s1 = str3.strip('/')
print(s1)
s1 = str3.lstrip('/')
print(s1)
s1 = str3.rstrip('/')
print(s1)

s = len("hello")
print('hshdh  ' +  str(s))