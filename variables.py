a = str('1')
b = int(1)
c = float(a)
print(a)
print(type(a))
print(type(b))
print(type(c))

x, y, z = "apple", "banana", "cherry"
print(x)
print(y)
print(z)

colors = ["red", "blue", "pink"]
e, f, g = colors
print(e)
print(f)
print(g)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
print(x, y)

#Globla variable

x = "awesome"

def myfunc():
  x="fanatstic!"
  print("Python is " + x)
myfunc();

print("python is " + x)

#global keyword


def func_name():
  global x
  x="darshan"
  print("name of person is " + x)
func_name()

print("using global keyword " + x)
