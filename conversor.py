
# Binary Converter
def hex_to_binary(hex_num):
    decimal_num = int(hex_num, 16)
    return decimal_to_binary(decimal_num)
def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num)
    return binary_num[2:]
def octal_to_binary(octal_num):
    decimal_num = int(octal_num, 8)
    return decimal_to_binary(decimal_num)

# Decimal Converter
def hex_to_decimal(hex_num):
    return int(hex_num, 16)
def binary_to_decimal(binary_num):
    return int(binary_num, 2)
def octal_to_decimal(octal_num):
    return int(octal_num, 8)

# Octal Converter
def hex_to_octal(hex_num):
    decimal_num = int(hex_num, 16)
    return decimal_to_octal(decimal_num)
def decimal_to_octal(decimal_num):
    octal_num = oct(decimal_num)
    return octal_num[2:]
def binary_to_octal(binary_num):
    decimal_num = int(binary_num, 2)
    return decimal_to_octal(decimal_num)

# Convesor a  Hexadecimal
def octal_to_hex(octal_num):
    decimal_num = int(octal_num, 8)
    return decimal_to_hex(decimal_num)
def decimal_to_hex(decimal_num):
    hex_num = hex(decimal_num)
    return hex_num[2:].upper()
def binary_to_hex(binary_num):
    decimal_num = int(binary_num, 2)
    return decimal_to_hex(decimal_num)
