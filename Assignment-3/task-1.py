def fact(num): 
    if num == 1:
        return num
    else:
        return num * fact(num - 1)


number = int(input('Enter a number : '))
factorial_result = fact(number)

print(f"Factorial of {number} is : {factorial_result}")