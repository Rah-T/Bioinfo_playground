

'''
Exercise
1. Write a program to find the root ( use termination criteria abs(f(x0)) = 0) of the following equations using Newton Raphson method. 
x^2-4x- 10=0

Initial guess point will be user defined, the output should print the root and number of iterations
'''
x=float(input("Enter x ="))
x1 = x - ((x**2-4*x-10)/(2*x-4))
fx1= x1**2-4*x1-10
# print(fx1)
i=0
while abs(fx1)>=0.00001:
        i+=1         
        # x(i+1) = x(i) - f(x) / f'(x)
        x=x1
        x1 = x - (x**2-4*x-10)/(2*x-4)
        fx1= x1**2-4*x1-10
        # x0 = x**2-4*x-10 / 2*x-4
print("root = ",x1," and number of iterations = ",i,"By newton-raphson method")




        
