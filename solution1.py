def convert_to_24_hour(hour,minute,period):
    if period == "pm" and hour !=12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0

    time_to_24_hour = f"{hour:02d}{minute:02d}"
    return time_to_24_hour



