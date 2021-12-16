n=[(a,0) for a in [1,2,3,4,5]]
#l=[(a,b)  for b in [1,2,3,4,5] for (a,x) in n if x==0 and print((a,b)) and  else break ]
def break1():
  #break
  return True

print((lambda x: break1())(1))

"""
def prettyplzzzzz(a=10,b,c=10):

  #error

def prettyplzzzzz(*,a=10,b,c=10):
 #keyword only arguement allows non-default arg to follow default arguement
"""

def prettyplzzzzz():
  """Function to make sense of what the user is trying to do and force execution of a statement even if it is not syntactically correct"""




def a(a,b,c,d):
  print("called a(a,b,c,d)")
  
a(10,30,20,40)


def a(a,b):
  print("called a(a,b)")
a(10,20)


def a(t,b,c=20):
  """a(10,30)
  this is actually calling the current function a(t,b,c=20) rather than calling the previously defined 
  a(a,b)

  this shows that def creates a function object with function signature and with the name of the function as object reference to the function and then later adds definition in it


  error RecursionError max recursion depth exceeded-1000
  """

  print("called a(t,b,c=20)")

a(10,30)

f=a # this method works
def a(a,b,c):
  """
  a(10,30,30) 
  
  error TypeError: int object is not callable(preference is given to arguement a over function name a())"""
  print("called a(a,b,c)")

a(1,2,3)

f(10,30) # a is acting like a variable that points to the address where the fucntion object is stored, def assigns a new value to a every time the new function a() is defined, we can preserve the previous function definition of a by assigning it to a unique variable like f before redefining a()
"""a(10,30,20,40)
I guess: only latest definition of a is considered valid, definition of a is simply overwritten every time a function with the same name is being defined, no function overloading--> verify once


??what if these functions were defined in different modules and imported and tried to be used??
I guess only the definition of a() from the last module to be imported into the current program will be used

error:TypeError: a() takes 2 to 3 arguements but 4 arguements were given 
"""

#
#r="x"
def myfunc():
  #print(r)
  r="xx" """this line if commented, will result in NameError(if there is also no variable r declared and initialized before this function definition starts), if not commented it will lead to the error caused by the preceding line( print(r)) being UnboundLocalError: local variable referenced before assignment, irrespective of if r exists as a global variable outside this function in this module(i.e even if we declare variable r before the start of this function definition, Unbound local error will be shown if this line is  uncommented)"""
myfunc()
#print(r)
#r="aa"

###trying to declare a variable without assigning it a value/initializing it
###a=pass###syntaxerror i.e compile time

####rre###NameError-runtime(not syntaxerror) rre is not defined


#the following works, declarinng a variable without assigning it a value:
l: str#="hello world"##uncommenting the assignment will also work ##also, this annotation str doesn't really affect what kind of value this variable is able to store

l: int=1+2j ##No error even though annotation and assigned value do not match int!=complex, also the preceding line(l: str) does not cause this line to be erroneous (str!=complex)
def myfunc2():
  ####print((global l)) ##invalid syntax
  #print(l)
  #l=10 # uncommenting this line will give compile time error: SyntaxError becuase the line after this line specifies that the l to be used is a global variable, and this line tries to reference l before it's delaration/(or to be more precise, specification in this case- since l is already"declared" before this function definition)
  global l
  l=10
  print(l)
print(l)
myfunc2()
print(l)
