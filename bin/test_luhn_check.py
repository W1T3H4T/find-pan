#!/usr/bin/env python3
# ===========================================================================
# Luhn algorithm check
# ===========================================================================
def luhn_check(num):
    rev_digits = [int(x) for x in str(num)][::-1]
    checksum = 0
    for i, d in enumerate(rev_digits):
        n = d if i % 2 == 0 else 2 * d
        checksum += n if n < 10 else n - 9
    return checksum % 10 == 0


def test_luhn_check():
    # Test cases with valid numbers
    assert luhn_check(4111111111111111) is True
    assert luhn_check(5500000000000004) is True
    assert luhn_check(340000000000009) is True
    assert luhn_check(6011000000000004) is True
    assert luhn_check(3530111333300000) is True

    # Test cases with invalid numbers
    assert luhn_check(4111111111111112) is False
    assert luhn_check(5500000000000005) is False
    assert luhn_check(340000000000008) is False
    assert luhn_check(6011000000000005) is False
    assert luhn_check(3530111333300001) is False

    # Test case with a number that has a checksum of 0
    assert luhn_check(0)

    print("All test cases passed!")


test_luhn_check()
