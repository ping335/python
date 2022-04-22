from string import digits, ascii_letters


def get_valid_values(radix=None):
    """Возвращает допустимые символы в указанной СС."""
    values = digits + ascii_letters
    
    if radix is None:
        radix = len(values)
    
    if 0 < radix <= len(values):
        return values[:radix]
    
    raise ValueError('Radix out of range.')


def dec2ns(number, radix):
    """Переводит число из десятичной СС в указанную."""
    if not isinstance(number, int):
        raise ValueError('Number must be integer type.')
    
    valid_values = get_valid_values(radix)
    result = []
    
    while number:
        result.append(valid_values[number % radix])
        number //= radix
    
    result.reverse()
    
    return ''.join(result)


def ns2dec(number, radix):
    """Переводит число из указанной СС в десятичную."""
    valid_values = get_valid_values(radix)
    result = 0
    
    for p, i in enumerate(reversed(number)):
        if i not in valid_values:
            raise ValueError('Incorrect number.')
        n = valid_values.index(i)
        result += n * radix ** p
    
    return result


def dec2bin(number):
    return dec2ns(number, 2)


def bin2dec(number):
    return ns2dec(number, 2)


if __name__ == '__main__':
    print(
        get_valid_values(2),
        get_valid_values(8),
        get_valid_values(16),
        get_valid_values(32)
    )
    
    print(dec2ns(25, 8), dec2ns(25, 16), dec2ns(255, 16))
    print(ns2dec('ff', 16), ns2dec('FF', 16))
