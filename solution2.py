# Define a function that checks if exactly two out of three numbers are positive
def two_exact_positive_numbers(a,b,c):
 
# Initialize counter to track positive numbers  
 positive_count = 0

# Check if a,b and c are positive
 if a > 0:
  positive_count +=1

 if b > 0:
   positive_count +=1

 if c > 0:
    positive_count +=1

# Check if count of positive numbers is exactly 2
 return positive_count == 2
   
# Prompt user to enter first,second and third integer   
a = int(input("Enter the first integer:"))
b = int(input("ENter the second integer:"))
c = int(input("Enter the third integer:"))

# Call the function and print the result
result = two_exact_positive_numbers(a,b,c)
print(result) 

