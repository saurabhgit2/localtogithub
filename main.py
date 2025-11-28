
n=int(input("Enter a number for Fibonacci series and factorial: "))  #Prompting Accepting user input
def fibonacci(n):  #function declaration to print Fibonacci series
    a,b=0,1   #first and second term in sequence declared
    if n==1:   #statment to print if n=1
        print(a)
        print(b)
    elif n==0:
        print(a)
    elif n<1: #statment to print if entered n value is negative
        print("the number of terms cannot be negative")

    else:  # for n value more than 1
        print(a)
        print(b)
    for i in range(1,n):  #for loop using to print series from index 2 till the n
        c=a+b
        a=b
        b=c
        print(c) #Printing series from index 2
           
fibonacci(n) #Function called

def factorial (n): # function to calculate factorial
    f=1  #initializing f to 1
    for i in range (1,n+1): #executing a loop for value of i from 1 to n+1
        f=f*i 
    return f

result=factorial(n) #assigning the value returned by function to result
print(result) # printing the final factorial value
