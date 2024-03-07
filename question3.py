def is_power_of_two(n):
    # A power of two has only one bit set in its binary representation
    # So, bitwise AND of n and (n - 1) should be 0 for powers of two
    return n != 0 and (n & (n - 1)) == 0

input_number = int(input("Enter an integer: "))
if is_power_of_two(input_number):
    print(input_number, "is a power of two.")
else:
    print(input_number, "is not a power of two.")
