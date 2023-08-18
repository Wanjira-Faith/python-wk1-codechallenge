def solve(x):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    max_value = 0
    current_value = 0

    for char in x:
        if char in consonants:
           current_value += ord(char) -ord('a') + 1

 
