MINUTES_IN_DAY = 60 * 24

def after_midnight(str):
    hour = int(str[0:2])
    minute = int(str[3:5])

    if hour == 24:
        hour = 0
    return (hour * 60) + minute

def before_midnight(str):

    if after_midnight(str) == 0:
        return 0
    else:
        return MINUTES_IN_DAY - after_midnight(str)

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
