def capitalize_first_letter(sentence):
    result = ""  # Initialize an empty string to store the result
    capitalize_next = True  # Flag to indicate whether the next character should be capitalized
    
    for char in sentence:
        if char.isalpha():
            if capitalize_next:
                result += char.upper()  # Capitalize the current character
                capitalize_next = False  # Reset the flag
            else:
                result += char.lower()  # Keep other characters lowercase
        else:
            result += char
            capitalize_next = True  # Set the flag to capitalize the next character if it's alphabetic

    return result

# Test the function
input_string = input("Enter a string: ")
result_string = capitalize_first_letter(input_string)
print("Capitalized string:", result_string)
