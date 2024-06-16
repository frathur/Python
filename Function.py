def factorial(x):
    fact = 1
    for a in range(1,x+1):
        fact = fact * a 
    return (fact)

input_num = int(input("Enter a number to determine the factorial: "))
fact = factorial(input_num)
print(f"The factorial of {input_num} is {fact}")