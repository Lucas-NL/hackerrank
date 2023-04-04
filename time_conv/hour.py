def timeConversion(s):
    hour = int(s[0:2])
    if hour == 12: 
        if 'AM' in s:
            hour -= 12
            shour = str(0) + str(hour) + s[2:len(s)-2]
            return  shour
        else:
            return  str(hour) + s[2:len(s)-2]


    if 'PM' in s:
        hour += 12    
        shour = str(hour) + s[2:len(s)-2]
        return  shour
    
    shour = str(0) + str(hour) + s[2:len(s)-2]
    return  shour
    
hora = "01:40:22AM"
print(timeConversion(hora))
