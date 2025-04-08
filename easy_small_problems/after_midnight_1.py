def time_of_day(num):
    minutes = num
    hours = 0

    while minutes > 0:
        minutes -= 60
        hours += 1

    while minutes < 0:
        minutes += 60
        hours -= 1

    while hours > 24:
        hours -= 24

    while hours < 0:
        hours += 24

    return f'{hours:02d}:{minutes:02d}'


print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
