# Define a function 'solve' that calculates highest value of consonant substrings in lowercase string
def solve(x):
    consonants = 'bcdfghjklmnpqrstvwxyz'

# Initialize variables to keep track of the maximum and current values    
    max_value = 0
    current_value = 0

# Loop through each character in x and check if the character is a consonant and calculate it's value based on its position in the alphabet        
    for char in x:
        if char in consonants:
           current_value += ord(char) -ord('a') + 1
        else:
            max_value = max(max_value,current_value)
            current_value = 0

# Return maximum value calculated during the loop
            return max(max_value,current_value)

# Prompt user to enter lowercase string
x = input("Enter a lowercase string: ")

# Call the function and print the result
result = solve(x)
print(f"The highest value of consonant substrings is: {result}")



 
