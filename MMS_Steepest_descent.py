'''
Rahul Asok Tiwari
BIM-2021-28

1. Write a program to find the minima of the following equations using Steepest Descent Method. 
x^2-4x- 10=0

Interval point will be user defined, the output should print the minima and number of iterations
'''

x1=float(input("Enter x ="))
f_x1= 2*x1 -4
i=1
# print(x1,fx1,i)
while abs(f_x1)>0.000001:
    x1=x1 + (0.1)*(-f_x1)
    fx1= x1**2-4*x1-10
    i+=1
print("Root is ",x1,"and number of iterations =",i)