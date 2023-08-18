def convert_to_24_hour(hour,minute,period):
    if period == "pm" and hour !=12:
        hour += 12
     
