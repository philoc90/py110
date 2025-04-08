def dms(start_num):
    DEGREE = "\u00b0"

    start_num = check_start_num(start_num)

    degree_value = int(start_num)

    degree_decimal = start_num - degree_value

    minute_with_decimal = degree_decimal * 60

    minute = int(minute_with_decimal)

    split_minute = split_digits(minute)

    second_with_decimal = minute_with_decimal - minute

    second = int(second_with_decimal * 60)

    split_second = split_digits(second)

    degree_minute_second = f"{degree_value}{DEGREE}{split_minute[0]}{split_minute[1]}'{split_second[0]}{split_second[1]}\""

    return degree_minute_second


def split_digits(num):
    split = []

    if num >= 10:
        split.append(int(num / 10))
        split.append(num % 10)

    else:
        split.append(0)
        split.append(num)

    return split

def check_start_num(start_num):
    while start_num < 0 or start_num > 360:
        if start_num > 360:
            start_num -= 360
        elif start_num < 0:
            start_num += 360

    return start_num

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"
