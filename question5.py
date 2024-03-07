def reverse_integer(n):
    reversed_n = 0
    negative = False
    
    # Handle negative numbers
    if n < 0:
        negative = True
        n = abs(n)
    
    # Reverse the digits of the number
    while n > 0:
        digit = n % 10
        reversed_n = (reversed_n * 10) + digit
        n //= 10
    
    # Add back the negative sign if necessary
    if negative:
        reversed_n *= -1
    
    return reversed_n

input_number = int(input("Enter an integer: "))
reversed_number = reverse_integer(input_number)
print("Reversed integer:", reversed_number)
