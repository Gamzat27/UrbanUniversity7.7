def get_multiplied_digits(number):
    str_number = str(number)   # В виде строки 'String'
    first = int(str_number [0])

    if len(str_number) > 1:

        return first * get_multiplied_digits(int(str_number[1:]))
    if first != 0:
        return first
    else:
         return 1

result = get_multiplied_digits(40203)
result2 = get_multiplied_digits(402030)

print(result,result2)
