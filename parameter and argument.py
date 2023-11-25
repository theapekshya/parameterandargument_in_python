#parameter and argument 

def number(num1 , num2):   #parameter
    print('num1=',num1)
    print('num2=',num2)

number(10,20)             #argument

#positional argument

def display(name, age):
    print('name=',name ,'age=',age)
display('apekshya',20)
#display('apekshya')         error, no of argument and parameter should be equal

#keyword argument
def display(name,age):
    print(name,age)
display(age=20,name='app')    #using keyword argument


#parameter with default value
def display(name,age=20):    
    print(name,age)
display('aaa')          #age=20 is default value so no need to provide during calling function






         









