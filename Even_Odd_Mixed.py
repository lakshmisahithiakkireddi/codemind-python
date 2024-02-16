def check_number_type(number):
    even_flag = True
    odd_flag = True

    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            odd_flag = False
        else:
            even_flag = False
        number //= 10

    if even_flag:
        return "Even"
    elif odd_flag:
        return "Odd"
    else:
        return "Mixed"
number = int(input())
print(check_number_type(number))