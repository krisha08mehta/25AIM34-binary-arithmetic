BITS = 8
MASK = (1 << BITS) - 1          # 0b11111111
MIN_VAL = -(1 << (BITS - 1))    # -128
MAX_VAL = (1 << (BITS - 1)) - 1  # +127
 
 
def to_twos_complement(n):
    """Convert a signed decimal integer to an 8-bit 2's complement string."""
    if n < MIN_VAL or n > MAX_VAL:
        raise ValueError(f"{n} cannot be represented in {BITS}-bit 2's complement")
    return format(n & MASK, f"0{BITS}b")
 
 
def from_twos_complement(bits):
    """Convert an 8-bit 2's complement string to a signed decimal integer."""
    value = int(bits, 2)
    if bits[0] == "1":          # sign bit set -> negative number
        value -= (1 << BITS)
    return value
 
 
def add_binary(a_bits, b_bits):
    """
    Add two 8-bit binary strings bit by bit (like manual addition).
    Returns (result_bits, carry_into_sign_bit, carry_out_of_sign_bit).
    """
    result = ""
    carry = 0
    carry_into_msb = 0
    for i in range(BITS - 1, -1, -1):       # from LSB to MSB
        if i == 0:
            carry_into_msb = carry
        total = int(a_bits[i]) + int(b_bits[i]) + carry
        result = str(total % 2) + result
        carry = total // 2
    return result, carry_into_msb, carry    # final carry = carry out of MSB
 
 
def detect_overflow(a_bits, b_bits, result_bits):
    """Overflow occurs if both operands have the same sign but the result's sign differs."""
    return a_bits[0] == b_bits[0] and result_bits[0] != a_bits[0]
 
 
def perform_addition(label, a, b):
    print("=" * 60)
    print(f"Expression {label}: ({a}) + ({b})")
    print("=" * 60)
 
    a_bits = to_twos_complement(a)
    b_bits = to_twos_complement(b)
    print(f"Operand 1 ({a:>4}) in 8-bit 2's complement : {a_bits}")
    print(f"Operand 2 ({b:>4}) in 8-bit 2's complement : {b_bits}")
 
    result_bits, c_in, c_out = add_binary(a_bits, b_bits)
 
    print("\nBinary addition:")
    print(f"      {a_bits}")
    print(f"    + {b_bits}")
    print(f"    ------------")
    print(f"    {c_out} {result_bits}   (leading digit = carry out of MSB, discarded)")
 
    result_dec = from_twos_complement(result_bits)
    print(f"\nResult (binary, 8-bit) : {result_bits}")
    print(f"Result (decimal)       : {result_dec}")
 
    expected = a + b
    print(f"Expected (decimal)     : {expected}")
    print(f"Verification           : {'MATCH' if result_dec == expected else 'MISMATCH'}")
 
    overflow = detect_overflow(a_bits, b_bits, result_bits)
    print(f"\nCarry into sign bit    : {c_in}")
    print(f"Carry out of sign bit  : {c_out}")
    print(f"Overflow detected      : {'YES' if overflow else 'NO'}")
    print()
 
 
if __name__ == "__main__":
    perform_addition("a", 25, +18)
    perform_addition("b", -25, -18)
 