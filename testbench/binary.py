import math

from cocotb.binary import BinaryValue, BinaryRepresentation

def float2fixed(x: float, bit_width: int, frac_width: int) -> BinaryValue:
  """ Convert a floating point number to a fixed point number

  sign-bit(1-bit) + integer-part(bit_width - frac_width - 1 bits) + fractional-part(frac_width bits)

  Args:
      x (float): floating point number
      bit_width (int): number of bits in the fixed point number
      frac_width (int): number of bits in the fractional part

  Returns:
      BinaryValue: fixed point number
  """
  # Sign bit
  sign_bit = '1' if x < 0 else '0'
  # Check if the number is too large
  x = abs(x)
  if x >= 2**(bit_width - frac_width - 1):
    assert False, "float2fixed: number too large"
  # Calculate the integer part
  int_part = math.floor(x)
  int_bin = bin(int_part)[2:].zfill(bit_width - frac_width - 1)
  # Calculate the fractional part
  frac_part = x - int_part
  frac_bin = ""
  for i in range(frac_width):
    frac_part *= 2
    frac_bin += str(int(frac_part))
    frac_part -= int(frac_part)
  # Combine the parts
  return BinaryValue(sign_bit + int_bin + frac_bin,
                     n_bits=bit_width,
                     binaryRepresentation=BinaryRepresentation.UNSIGNED)

def fixed2float(x: BinaryValue, bit_width: int, frac_width: int) -> float:
  """ Convert a fixed point number to a floating point number

  sign-bit(1-bit) + integer-part(bit_width - frac_width - 1 bits) + fractional-part(frac_width bits)

  Args:
      x (BinaryValue): fixed point number
      bit_width (int): number of bits in the fixed point number
      frac_width (int): number of bits in the fractional part

  Returns:
      float: floating point number
  """
  # Extract the parts
  sign_bit = x.binstr[0]
  int_bin = x.binstr[1:bit_width - frac_width]
  int_part = int(int_bin, 2)
  frac_bin = x.binstr[bit_width - frac_width:]
  frac_part = 0
  for i in range(frac_width):
    frac_part += int(frac_bin[i]) * 2**(-i - 1)
  # Calculate the number
  return (-1)**int(sign_bit) * (int_part + frac_part)

if __name__ == "__main__":
  print("Binary library 0.0.1v")
