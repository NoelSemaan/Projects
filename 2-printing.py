#Step 1 Basic Printing
print("Hello World")
#Step 2 Printing Contents of Variables
text = 'Hello World'
print(text)
#Step 3 Formating Variables
v1 = 'Hello'
v2 = 'World'
#the output is formated as following: each {} will be replaced by a variable present in the .format function and depending on the way you place them
print('The output of v1 is: {} and the output of v2 is: {}'.format(v1,v2))
#the ouput  will be the same but the variable placement will b different because of he numbering provided (the count starts from 0) and is set depending on
#the number you place in the {} and the role in witch the variables v1 and v2 are placed in the format()
print('The output of v1 is: {1} and the output of v2 is: {0}'.format(v1,v2))
