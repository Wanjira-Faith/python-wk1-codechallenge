# Define a function to convert time from 12-hour format to 24-hr format
def convert_to_24_hour(hour,minute,period):

#check if it's pm or am    
    if period == "pm" and hour !=12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0

# create a formatted string for 24-hr time and return the converted time(result)
    time_to_24_hour = f"{hour:02d}{minute:02d}"
    return time_to_24_hour

# prompt the user to enter hour,minute and am or pm
hour = int(input("Enter the hour(1-12): "))
minute = int(input("Enter the minute(0-59):"))
period = input("Enter 'am' or 'pm':")

# call the conversion function and print the converted time in 24-hr format
result = convert_to_24_hour(hour,minute,period)
print(result)






