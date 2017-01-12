# How old am I
print("How old are you (in years)")
years = int(input())

def monthsOld(years):
    return years * 12

def weeksOld(years):
    return years * 52

def daysOld(years):
    return years * 365

def hoursOld(years):
    return daysOld(years) * 24

def minutesOld(years):
    return hoursOld(years) * 60

def secondsOld(years):
    return minutesOld(years) * 60

def milisOld(years):
    return secondsOld(years) * 1000

print("Months old:", monthsOld(years))
print("Weeks old: ", weeksOld(years))
print("Days old: ", daysOld(years))
print("Hours old: ", hoursOld(years))
print("Minutes old: ", minutesOld(years))
print("Seconds old: ", secondsOld(years))
print("Miliseconds old: ", milisOld(years))
