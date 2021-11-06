"""In this lesson we will be getting familiar with arithmetic operators such as 
+ addition
- substraction
* product
/ division (returns the dividant of the division)
% modulus (returns the remainder of the division)
"""
#variable Declaration
x=4
y=3
counter=0
#Basic calculations
x+y#= 4+3 = 7
x-y#= 4-3 = 1
x*y#= 4*3 = 12
x/y#= 4/3 = 1.333333
x%y#= 4%3 = 1
#incrementation: here we need to understand the logic
#we have an original state of counter = 0 and incrementing it will set it to 1
#the logic is as follows: variable = (old value)  (operator) (value)
#After the calculation is done the variable will have a new value depending on the operation 
counter = counter + 1# this operation is done as follows: counter = 0(old value) +(operator) 1(value) that will set the counter to 1
#another way of doing it is as follows
counter += 1
#these two ways are applicable with all operators
counter = counter - 1
counter -=1
counter = counter * 1
counter *=1
counter = counter / 1
counter /=1
