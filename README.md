# Python-wk1-codechallenge

# Challenge 1: Converting 12-hour time to 24-hour time
Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

Your task is to return a four-digit string that encodes that time in 24-hour time.

Notes

By convention, noon is 12:00 pm, and midnight is 12:00 am.

On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015. 

# Solution 1
To solve this challenge:

1. Check the period (am/pm) and the hour value.
2. Adjust the hour accordingly based on the period.
3. Convert the hour and minute to a four-digit string.
4. Return the formatted time.

# Running Solution 1
1. Open a terminal
2. Navigate to the directory 
`cd python-wk1-codechallenge` 
3. Run solution using `python3 solution1.py`

# Challenge 2: Two numbers are positive.
Task:
Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.

Examples:
(2, 4, -3) == True

(-4, 6, 8) == True

(4, -6, 9) == True

(-4, 6, 0) == False

(4, 6, 10) == False

(-14, -3, -4) == False

# Solution 2
To solve this challenge:

1. Count the number of positive integers among the three given.
2. Return True if the count is exactly 2, otherwise return False.

# Running Solution 2
1. Open a terminal
2. Navigate to the directory 
`cd python-wk1-codechallenge` 
3. Run solution using `python3 solution2.py`

# Challenge 3: Consonant value
Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

Examples;
For the word "zodiacs", solve("zodiacs") = 26

For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs"

-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

For the word "strength", solve("strength") = 57.

The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

# Solution 3
To solve this challenge:

1. Iterate through the characters in the input string.
2. Accumulate the value of consonant substrings and track the highest value.
3. Return the highest value.

# Running Solution 3
1. Open a terminal
2. Navigate to the directory 
`cd python-wk1-codechallenge` 
3. Run solution using `python3 solution3.py`

# Author 
Wanjira Faith

# License
MIT License