'''
---------------------------------------------------------
18th dec 2021: TRY OUT TOMORROW 
Also, Try to create a function to read lines of code, print them each of them with their corresponding output and line number 
'''

"""Note :We need to revise basic python commands to use it in a console/command line


python course?
php?

"""


"""

try properly overriding builtin print function

function attributes/ functools/ something else? to programatically get the formal parameters from a function signature(by specifying the function name) and using that parameter list to define a new function with the same parameters


(((((Basically, I want a easy way to define methods to override existing methods without having to lookup their signature, but just by knowing their NameError)))))

What I want from You:
  get function args in string form
 way to execute a function definition code in a string form from within the python script

 ((Is their a better algorithm possible using functions in python in order to achieve what I want))

for ex:
-----------------------
CODE:(This doesn't work but I am looking for something which helps me achieve something similar )
-------------------------

def func1(x,y,z,*args,k=10,l,**kwargs):
  pass

eval("def func1Modified("+func1.argslist+"):"+"\n\tfunc1(func1Modified.argvalues)")
'''
The above line is wrong, I am looking for something like the above(but executable) which does the following
This line should do something like this when executed:
define a function: func1Modified like this:
def func1Modified(x,y,z,*args,k=10,l,**kwargs):
  #do some Modification here 
  func1(func1Modified.argvalues)# pass all received arguements to func1() i.e func1(1,2,3,4,l=20,j=10)


'''
func1Modified(1,2,3,4,l=20,j=10) #calling the overriden function



our code should be able to define and execute a new function with the same arguements as another specified function


"""
largenum=int(1000000000000000033)

idOfTrue=id(True)
idOfIdOfTrue=id(id(True))
idOf1=id(1)
idOfIdOf1=id(id(1))
idOfTrueVar2 = (id(True))
idOf1Var2 = (id(1))
idOfIdOfTrueVar2 = id(id(True))
idOfIdOf1Var2 = id(id(1))

print(dir(print))



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


