#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    return int(digits, base)
    # TODO: Decode digits from binary (base 2)
    # TODO: Decode digits from hexadecimal (base 16)
    # TODO: Decode digits from any base (2 up to 36)
    # digits = int(digits)
    # result = 0
    # exponent = 0
    # if base == 2:
    #     '''
    #     while digits > 0:
    #         result += base ** exponent * (digits % 10)
    #         digits //= 10
    #         power += 1
    #     return result

    #     '''
    #     return int(digits, base)
    # elif base == 16:
    #     '''
    #     while digits > 0:
    #         result += base ** exponent * (digits % 16)
    #         digits //= 16
    #         power += 1
    #     return result
    #     '''
    #     return int(digits, base)
    # else:
    #     return int(digits, base)
    #     '''
    #     string = string[::-1]
    #     decimal_num = 0
    #     for exponent in range(len(string)):
    #         single_num = string[exponent]
    #         if single_num.isdigit():
    #             single_num = int(single_num)
    #         else:
    #             single_num = ord(single_num()) - ord('A') + 10
    #         decimal_num += single_num * (base ** exponent)
    #     '''


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    '''
    digits = digits[::-1]
    decimal_num = 0
    for i in range(len(digits)):
        digit = digits[i]
        digit = int(digit)
        decimal_num += digit * base ** 1
    return decimal_num
    '''
    new_num = ""
    while number > 0:
        temp = int(number%base)
        if temp < 10:
            new_num += str(temp)
        else:
            new_num += chr(ord('a') + temp -10)
        number //= base
    
    new_num = new_num[::-1]
    return new_num
    



def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    old_string = decode(digits, base1)
    new_string = encode(int(old_string), base2)
    return new_string
    
    


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
