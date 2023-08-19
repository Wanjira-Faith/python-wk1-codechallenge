def two_exact_positive_numbers(a,b,c):
 positive_count = 0

 if a > 0:
  positive_count +=1

 if b > 0:
   positive_count +=1

 if c > 0:
    positive_count +=1

 return positive_count == 2
   
a = int(input("Enter the first integer:"))
b = int(input("ENter the second integer:"))
c = int(input("Enter the third integer:"))

 

