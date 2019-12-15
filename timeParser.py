numbers = {1:"one", 2: "two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"night", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 15:"a quater", 20:"twenty"}

def parse(hour, minute):
    if type(minute) != int or minute<0 or minute>=60:
        return "invalid minite"
    if type(hour) != int or hour<=0 or hour>12:
        return "invalid hour"
    reverse = False
    if minute == 0:
        return numbers[hour] + " o'clock"
    if minute == 30:
        return "half past " + numbers[hour]
    if minute > 30:
        if hour == 12:  hour = 1
        else:   hour += 1
        minute = 60 - minute
        reverse = True

    i = int(minute / 10)
    if minute not in numbers:
        minute = minute % 10

    if minute in numbers:
        minute = numbers[minute]
    else:
        if i == 0:
            minute = numbers[minute]
        elif i == 1:
            minute = numbers[minute] + "teen"
        elif i == 2:
            minute = "twenty-" + numbers[minute]

    if reverse == False:
        return minute+" past "+ numbers[hour]
    else:
        return minute+" to "+ numbers[hour]

print(parse(1,47))
