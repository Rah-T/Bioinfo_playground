'''
Rahul Asok Tiwari
BIM-2021-28

Practical 8
1. Write a program to find the root ( use termination criteria abs(f(x0)) = 0) of the following equations using Secant method. 
x^2-4x- 10=0
Interval points will be user defined, the output should print the root and number of iterations
'''

x1=float(input("Enter x1 = "))
x2=float(input("Enter x2 = "))
fx1= x1**2-4*x1-10
fx2= x2**2-4*x2-10
x0= x2-((fx2*(x2-x1))/(fx2-fx1))
fx0= x0**2-4*x0-10
i=0
while abs(fx0) > 0.0000001:
    x1=x2
    x2=x0
    fx1= x1**2-4*x1-10
    fx2= x2**2-4*x2-10
    x0=x2-((fx2*(x2-x1))/(fx2-fx1))
    fx0= x0**2-4*x0-10
    i+=1
print("root is ",x0,"and number of iterations",i,"by secant method")