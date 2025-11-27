print("Let us write a simple code for Fibonacci series without using any function")

a=0 #initializing the first term of the series
b=1 #initializing second term
n = int(input("Enter the number of terms in Fibonacci series: "))  #Prompting user to enter the number of terms for Fibonacci series

print(a) #Printing the first term at index 0
print(b) #Printing index 1 term
for i in range(2,n):    #for loop to print sequence from index 2 till n
    c=a+b  #variable used to store the sum of previous two terms
    a=b  #swapping the values to calculate next value of c(fibonacci series)
    b=c  #same reason as above
    print(c) #printing sequence from inex 2 till n
    
    
