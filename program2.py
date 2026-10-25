BITS = 8
 
 
def logical_left_shift(bits, positions):
    """Shift left; MSB is discarded, 0 is filled in on the right."""
    print(f"Original  : {bits}")
    for step in range(1, positions + 1):
        dropped = bits[0]
        bits = bits[1:] + "0"
        print(f"Step {step}    : {bits}   (bit '{dropped}' shifted out on the left, '0' added on the right)")
    return bits
 
 
def logical_right_shift(bits, positions):
    """Shift right; LSB is discarded, 0 is filled in on the left."""
    print(f"Original  : {bits}")
    for step in range(1, positions + 1):
        dropped = bits[-1]
        bits = "0" + bits[:-1]
        print(f"Step {step}    : {bits}   (bit '{dropped}' shifted out on the right, '0' added on the left)")
    return bits
 
 
def verify(label, original, result, expected_int):
    """Cross-check against Python's built-in shift operators."""
    ok = result == format(expected_int & 0xFF, f"0{BITS}b") and len(result) == BITS
    print(f"Final result ({label}) : {result}  [{len(result)} bits]")
    print(f"Decimal              : {int(original, 2)} -> {int(result, 2)}")
    print(f"Verification         : {'MATCH' if ok else 'MISMATCH'} with Python operator")
    print()
 
 
if __name__ == "__main__":
    # a) Logical left shift of 10110110 by 2
    print("=" * 60)
    print("a) Logical left shift of 10110110 by 2 positions")
    print("=" * 60)
    a_in = "10110110"
    a_out = logical_left_shift(a_in, 2)
    verify("a", a_in, a_out, int(a_in, 2) << 2)   # & 0xFF keeps it 8-bit
 
    # b) Logical right shift of 11010100 by 2
    print("=" * 60)
    print("b) Logical right shift of 11010100 by 2 positions")
    print("=" * 60)
    b_in = "11010100"
    b_out = logical_right_shift(b_in, 2)
    verify("b", b_in, b_out, int(b_in, 2) >> 2)
 