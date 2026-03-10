#concatanation
first_name="muttappa"
last_name="junjarawad"
full_name= first_name+"  "+last_name
print(full_name)
# repitetion
mesg="muttu"
print(mesg *10)

#strings methods
name="muttu"
print(name.upper())
print(name.lower())
print(name.strip())
print(name.replace("muttu","mallu"))



#string denoted by three types

nam="muttu"
name="muttu'"
# to find the length of the string by using len()
print(len(name))
print(len(nam))

# to find the which postion in word 
college="sgbit college belagavi"
print(len(college))
print(college[2])   #[2] that means index
print(college[-1])
print(college[-2])
print(college[5])
print(college[1:23]) 
print(college[0:23])
print(college[0::2])  # skip the two alphabets

# exmplas 
# 1.write the python program that asks the user for their name and age,then prints a personalized greeting messages 
name=input("enter your name")
age=int(input("enter your age"))
print("my name is " + name +" " +"my age is ",str(age))

#take the one string  

father_name="mallappa"
print(father_name.upper())
print(father_name.lower())
print(father_name.replace("mallappa","mallu"))

# write the one string 
name="muttappa mallappa junjarwad"
print(len(name))

#operators

# assignment operators
a=10
b=20
a=a+100   # a=a+100 that means a=10+100
a+=100   
print(a)

# comparison operators
x=10
y=30
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)


#logical operators


print(True and True) # and opperator if both condiation true then the output is true
print(True and False) # output is false
print(False and False)# output is false


#membership operators
name="muttu"
print(name in "m")
print(name not in "m")

name="shivabasu junjarawad"
print(name in "va")
print(name in "basu")