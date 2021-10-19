
def convert_integer_to_roman(x):
    integer_to_roman = {'1': 'I', '4': 'IV', '5': 'V', '9': 'IX', '10': 'X',
    '40': 'XL', '50': 'L', '90': 'XC', '100': 'C', '400': 'CD', '500': 'D',
    '900': 'CM', '1000': 'M'}

    dec_value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    temp = ''

    for i in dec_value:
        if x != 0:
            if i <= x:
                x = x- i
                temp = temp + str(integer_to_roman[i])
        print(temp)
        return temp