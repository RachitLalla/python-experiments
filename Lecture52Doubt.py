'''
---------------------------------------------------------
18th dec 2021: TRY OUT TOMORROW 
Also, Try to create a function to read lines of code, print them each of them with their corresponding output and line number 
'''

"""Note :We need to revise basic python commands to use it in a console/command line


python course?
php?

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