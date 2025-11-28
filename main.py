
n=int(input("Enter the number of terms: "))  #Prompting Accepting user input
def fibonacci(n):  #function declaration to print Fibonacci series
    a,b=0,1   #first and second term in sequence declared
    print(a)
    print(b)
    for i in range(2,n):  #for loop using to print series from index 2 till the n
        c=a+b
        a=b
        b=c
        print(c) #Printing series from index 2

fibonacci(n) #Function called
