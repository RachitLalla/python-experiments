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

l:complex
l:str=10j
l:int # no error
def dell():
  #global l # if this
  #print(l)
  #l=10# trying to change a global variiable without declaring it as global inside the scope(should be the first statement referencing the variable) ? python will consider this a s us trying to create a local variable with the same name as a preexisting global variable and will throw an unbound local Error in the precceding line(print(l) saying that we  tried to refeerence a local variable before assigning it a value)
  xx=2
  #del l # provided that the line: 'global l' is commented; print(l) doesn't give an error but del l does give UnboundlocalError: local variable l referenced before assignment Why so?-> same reason as above comment
dell()
#yy=24.55
#print(type(yy))#float

global zz
zz=12
##global zz
zz:str=29.3 
##global zz 
""" this line leads to error SyntaxError: annotated name zz can not be global instead of the error: SyntaxError: name zz assigned value before global declaration- which it throws in line: (
zz=12
global zz
)
"""
del zz
#print(zz)
###for and if are treated as same scope
for i in range(10):
  global yy ## since for loop is considered as the same scope as the outer scope(main module in this case) and not a nested scope(like function definitions or class declarations), initializing yy before the global declaration(in line: yy:str=24.55) leads to a compile time SyntaxError: yy is assigned to before global declaration or SyntaxError: name yy is used prior to global declaration(in statement: print(yy)) 
  yy=i
  ######print(yy)
  
print(i)#i is declared in the for loop


print(yy)

#print(xx) # xx is declared in function dellO. This code will generate an error-> NameError: name xx is not defined
"""new var declared in a for/while/etc loop or an if else block is accesible outside it  in python(not in java) but the same is not applicable to a variable declared in a fucntion body"""


##def foo(aa,global bb):# global bb- SyntaxError: invalid syntax
def parameterizedfunc(aa,bb=1):
  aa=10
  bb=20
parameterizedfunc(10,20)
#print(aa,bb)## trying to access local parameters of a function outside the function's scope
##NameError: name aa is not defined
global c
#print("c: ",c)#trying to print c before initiazling it 
#NameError: name c is not defined
c=100
#nonlocal x #SyntaxError: nonlocal declaration not allowed at module level

#print("Str+int: "+9) # TypeError: can only concatenate str(not 'int') to str
print("printing str+str(int): "+str(9))# correct way of doing the above
x=7

print(x)
def nonlocalvaraccess():
  #nonlocal x # Syntax Error no binding for nonlocal x found
  c=10# this is treated as a new local var c, not the global one
  print("c:"+str(c))
  #global x # uncommenting this line will lead to error in the line: 'nonlocal x' in function: innerfunc()-since nonlocal x will try to find x local to any of the enclosing scopes recursively(from inner enclosing scope to outter enclosing scope) 1 step above the current scope(in the scope enclosing the current scope) and so on untill it finds the first x declaration it finds which is local variable in that scope(scope in the chain of enclosing scopes of the current scope where 'nonlocal x' statement is specified). This line 'global x' tells python compiler that this x is the x defined in the global scope( variable defined directly in the current module) and thus this x 'is not local to'/'does not belong to the scope of' the module: nonlocalvaraccess(). Thus python compiler will throw an error
  x=5 # local var x, not the global one
  def innerfunc():
    nonlocal x # if the line 'global x' in all of the enclosing scopes(for example: in the scope of the function: nonlocalvaraccess() which is the immediate and only enclosing scope other than the module/global scope in this case)(except the module/global scope) is uncommented, python compiler  will generate an error at this line: SyntaxError: no Binding for nonlocal 'x' found



    x=3
    print("inside innerfunc()-> nonlocalvaraccess(){ innerfunc(){ nonlocal x=3}}: ",x)
  print("Before innerfunc: ",x)
  innerfunc()
  print("After innerfunc()",x)
print("Before nonlocalvaraccess():"+str(x))
nonlocalvaraccess()
print("After nonlocalvaraccess():"+str(x))

print("c: "+str(c)) ##will print orignal c=100 not the modified value in nonlocalvaraccess() function
'''
---------------------------------------------------------
18th dec 2021: TRY OUT TOMORROW 
Also, Try to create a function to read lines of code, print them each of them with their corresponding output and line number 
'''
largenum=int(1000000000000000033)

idOfTrue=id(True)
idOfIdOfTrue=id(id(True))
idOf1=id(1)
idOfIdOf1=id(id(1))
idOfTrueVar2 = (id(True))
idOf1Var2 = (id(1))
idOfIdOfTrueVar2 = id(id(True))
idOfIdOf1Var2 = id(id(1))






print ((id(True)), ((id(True))),(id(1)),id(1))
print (id(id(True)), id(id(True)),id(id(1)),id(id(1)))

print (id(id(True)), id(id(True)),id(id(1)),id(id(1)))

print ((id(True)), ((id(True))),(id(1)),id(1))
print (id(id(True)), id(id(True)),id(id(1)),id(id(1)))
"""

Output: 
140230620037120 140230620037120 140230620329696
140230555530032 140230555530032 140230555530032

"""

print ((id(1000000000000000033)), ((id(1000000000000000033))),(id(largenum)))