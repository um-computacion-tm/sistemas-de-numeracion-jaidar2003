import unittest
from conversor import hex_to_binary
from conversor import decimal_to_binary
from conversor import octal_to_binary

from conversor import hex_to_decimal
from conversor import binary_to_decimal
from conversor import octal_to_decimal

from conversor import hex_to_octal
from conversor import decimal_to_octal
from conversor import binary_to_octal

from conversor import octal_to_hex
from conversor import decimal_to_hex
from conversor import binary_to_hex

class TestConversion(unittest.TestCase):

# Test to Binary
    def test_hex_to_binary(self):
        self.assertEqual(hex_to_binary("2F"), "101111")
        self.assertEqual(hex_to_binary("7B"), "1111011")
        self.assertEqual(hex_to_binary("AF"), "10101111")
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(35), "100011")
        self.assertEqual(decimal_to_binary(129), "10000001")
        self.assertEqual(decimal_to_binary(255), "11111111")
    def test_octal_to_binary(self):
        self.assertEqual(octal_to_binary("63"), "110011")
        self.assertEqual(octal_to_binary("71"), "111001")
        self.assertEqual(octal_to_binary("17"), "1111")

# Test to Decimal
    def test_hex_to_decimal(self):
        self.assertEqual(hex_to_decimal('1A'), 26)
        self.assertEqual(hex_to_decimal('FF'), 255)
        self.assertEqual(hex_to_decimal('10'), 16)
    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal('1010'), 10)
        self.assertEqual(binary_to_decimal('11111111'), 255)
        self.assertEqual(binary_to_decimal('10000'), 16)
    def test_octal_to_decimal(self):
        self.assertEqual(octal_to_decimal('10'), 8)
        self.assertEqual(octal_to_decimal('777'), 511)
        self.assertEqual(octal_to_decimal('20'), 16)

# Test to Decimal
    def test_hex_to_octal(self):
        self.assertEqual(hex_to_octal('1A'), '32')
        self.assertEqual(hex_to_octal('FF'), '377')
        self.assertEqual(hex_to_octal('10'), '20')
    def test_decimal_to_octal(self):
        self.assertEqual(decimal_to_octal(10), '12')
        self.assertEqual(decimal_to_octal(255), '377')
        self.assertEqual(decimal_to_octal(16), '20')
    def test_binary_to_octal(self):
        self.assertEqual(binary_to_octal('1010'), '12')
        self.assertEqual(binary_to_octal('11111111'), '377')
        self.assertEqual(binary_to_octal('10000'), '20')

# Test to Hexadecimal
    def test_octal_to_hex(self):
        self.assertEqual(octal_to_hex('12'), 'A')
        self.assertEqual(octal_to_hex('377'), 'FF')
        self.assertEqual(octal_to_hex('20'), '10')
    def test_decimal_to_hex(self):
        self.assertEqual(decimal_to_hex(10), 'A')
        self.assertEqual(decimal_to_hex(255), 'FF')
        self.assertEqual(decimal_to_hex(16), '10')
    def test_binary_to_hex(self):
        self.assertEqual(binary_to_hex('1010'), 'A')
        self.assertEqual(binary_to_hex('11111111'), 'FF')
        self.assertEqual(binary_to_hex('10000'), '10')

if __name__ == '__main__':
    unittest.main()