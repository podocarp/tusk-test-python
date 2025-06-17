import pytest
import math
from utils.calculator import add, mul, mod


def test_add():
    assert add(1, 2) == 3


def test_mul_positive_integers():
    """
    Test that mul returns the product of two positive integers.
    """
    # Arrange: Define two positive integer inputs
    num1 = 2
    num2 = 3
    expected_product = 6

    # Act: Call the mul function with the positive integers
    actual_product = mul(num1, num2)

    # Assert: Verify that the result is the expected product
    assert actual_product == expected_product

    # Test with another pair of positive integers for good measure
    num1_alt = 5
    num2_alt = 10
    expected_product_alt = 50

    actual_product_alt = mul(num1_alt, num2_alt)
    assert actual_product_alt == expected_product_alt


def test_mul_zero_input():
    """
    Test that mul returns 0 when one of the inputs is 0.
    """
    # Arrange: Define inputs with one zero
    num1 = 0
    num2 = 5
    expected_product = 0

    # Act: Call the mul function
    actual_product = mul(num1, num2)

    # Assert: Verify that the result is 0
    assert actual_product == expected_product

    # Test with the arguments swapped
    num1_alt = 10
    num2_alt = 0
    expected_product_alt = 0

    actual_product_alt = mul(num1_alt, num2_alt)
    assert actual_product_alt == expected_product_alt


def test_mul_negative_integers():
    """
    Test that mul returns a positive number when both inputs are negative integers.
    """
    # Arrange: Define two negative integer inputs
    num1 = -2
    num2 = -3
    expected_product = 6

    # Act: Call the mul function with the negative integers
    actual_product = mul(num1, num2)

    # Assert: Verify that the result is the expected product
    assert actual_product == expected_product

    # Test with another pair of negative integers for good measure
    num1_alt = -5
    num2_alt = -10
    expected_product_alt = 50

    actual_product_alt = mul(num1_alt, num2_alt)
    assert actual_product_alt == expected_product_alt


def test_mul_positive_and_negative_integers():
    """
    Test that mul returns a negative number when one input is positive and the other is negative.
    """
    # Arrange: Define one positive and one negative integer input
    num1 = 2
    num2 = -3
    expected_product = -6

    # Act: Call the mul function with the positive and negative integers
    actual_product = mul(num1, num2)

    # Assert: Verify that the result is the expected product
    assert actual_product == expected_product

    # Test with another pair of positive and negative integers for good measure
    num1_alt = -5
    num2_alt = 10
    expected_product_alt = -50

    actual_product_alt = mul(num1_alt, num2_alt)
    assert actual_product_alt == expected_product_alt


def test_mul_floating_point_numbers():
    """
    Test that mul returns the correct product when both inputs are floating-point numbers.
    """
    # Arrange: Define two floating-point inputs
    num1 = 2.5
    num2 = 3.0
    expected_product = 7.5

    # Act: Call the mul function with the floating-point numbers
    actual_product = mul(num1, num2)

    # Assert: Verify that the result is the expected product
    assert actual_product == expected_product

    # Test with another pair of floating-point numbers for good measure
    num1_alt = 1.5
    num2_alt = 2.5
    expected_product_alt = 3.75

    actual_product_alt = mul(num1_alt, num2_alt)
    assert actual_product_alt == expected_product_alt


def test_mul_non_numeric_types():
    """
    Test that mul returns the expected result when called with non-numeric types (string and list).
    """
    # Test with a string and an integer
    string_input = "abc"
    integer_input = 3
    expected_string_output = "abcabcabc"
    actual_string_output = mul(string_input, integer_input)
    assert actual_string_output == expected_string_output

    # Test with a list and an integer
    list_input = [1, 2]
    integer_input = 2
    expected_list_output = [1, 2, 1, 2]
    actual_list_output = mul(list_input, integer_input)
    assert actual_list_output == expected_list_output


def test_mul_large_integers():
    """
    Test that mul correctly handles multiplication of very large integers.
    """
    # Arrange: Define two very large integers
    num1 = 10**20
    num2 = 10**15
    expected_product = 10**35

    # Act: Call the mul function with the large integers
    actual_product = mul(num1, num2)

    # Assert: Verify that the result is the expected product
    assert actual_product == expected_product


def test_mod_positive_integers():
    """
    Test that mod returns the correct remainder when both inputs are positive integers.
    """
    # Arrange: Define two positive integer inputs
    num1 = 7
    num2 = 3
    expected_remainder = 1

    # Act: Call the mod function with the positive integers
    actual_remainder = mod(num1, num2)

    # Assert: Verify that the result is the expected remainder
    assert actual_remainder == expected_remainder

    # Test with another pair of positive integers where remainder is 0
    num1_alt = 10
    num2_alt = 5
    expected_remainder_alt = 0

    actual_remainder_alt = mod(num1_alt, num2_alt)
    assert actual_remainder_alt == expected_remainder_alt

    # Test with another pair where num1 < num2
    num1_another = 5
    num2_another = 10
    expected_remainder_another = 5

    actual_remainder_another = mod(num1_another, num2_another)
    assert actual_remainder_another == expected_remainder_another


def test_mod_zero_input():
    """
    Test that mod returns 0 when the first input is 0.
    """
    # Arrange: Define inputs with the first one zero
    num1 = 0
    num2 = 5
    expected_remainder = 0

    # Act: Call the mod function
    actual_remainder = mod(num1, num2)

    # Assert: Verify that the result is 0
    assert actual_remainder == expected_remainder

    # Test with another pair of numbers
    num1_alt = 0
    num2_alt = 10
    expected_remainder_alt = 0

    actual_remainder_alt = mod(num1_alt, num2_alt)
    assert actual_remainder_alt == expected_remainder_alt


def test_mod_second_input_is_one():
    """
    Test that mod returns 0 when the second input is 1.
    """
    # Arrange
    num1 = 5
    num2 = 1
    expected_remainder = 0

    # Act
    actual_remainder = mod(num1, num2)

    # Assert
    assert actual_remainder == expected_remainder

    # Test with another number
    num1_alt = 100
    num2_alt = 1
    expected_remainder_alt = 0
    actual_remainder_alt = mod(num1_alt, num2_alt)
    assert actual_remainder_alt == expected_remainder_alt

    # Test with a negative number
    num1_negative = -7
    num2_negative = 1
    expected_remainder_negative = 0
    actual_remainder_negative = mod(num1_negative, num2_negative)
    assert actual_remainder_negative == expected_remainder_negative


def test_mod_negative_and_positive_integers():
    """
    Test that mod returns the correct remainder when the first input is negative and the second input is positive.
    """
    # Arrange: Define a negative integer and a positive integer
    num1 = -7
    num2 = 3
    expected_remainder = 2

    # Act: Call the mod function with the negative and positive integers
    actual_remainder = mod(num1, num2)

    # Assert: Verify that the result is the expected remainder
    assert actual_remainder == expected_remainder

    # Test with another pair of negative and positive integers
    num1_alt = -10
    num2_alt = 5
    expected_remainder_alt = 0

    actual_remainder_alt = mod(num1_alt, num2_alt)
    assert actual_remainder_alt == expected_remainder_alt

    # Test with another pair where abs(num1) < num2
    num1_another = -5
    num2_another = 10
    expected_remainder_another = 5

    actual_remainder_another = mod(num1_another, num2_another)
    assert actual_remainder_another == expected_remainder_another


def test_mod_negative_integers():
    """
    Test that mod returns the correct remainder when both inputs are negative.
    """
    # Arrange: Define two negative integer inputs
    num1 = -7
    num2 = -3
    expected_remainder = -1

    # Act: Call the mod function with the negative integers
    actual_remainder = mod(num1, num2)

    # Assert: Verify that the result is the expected remainder
    assert actual_remainder == expected_remainder

    # Test with another pair of negative integers
    num1_alt = -10
    num2_alt = -5
    expected_remainder_alt = 0

    actual_remainder_alt = mod(num1_alt, num2_alt)
    assert actual_remainder_alt == expected_remainder_alt

    # Test with another pair where num1 < num2
    num1_another = -5
    num2_another = -10
    expected_remainder_another = -5

    actual_remainder_another = mod(num1_another, num2_another)
    assert actual_remainder_another == expected_remainder_another


def test_mod_floating_point_numbers():
    """
    Test that mod returns the correct remainder when both inputs are floating-point numbers.
    """
    # Arrange: Define two floating-point inputs
    num1 = 7.5
    num2 = 2.0
    expected_remainder = 1.5

    # Act: Call the mod function with the floating-point numbers
    actual_remainder = mod(num1, num2)

    # Assert: Verify that the result is the expected remainder
    assert actual_remainder == expected_remainder

    # Test with another pair of floating-point numbers for good measure
    num1_alt = 5.25
    num2_alt = 1.5
    expected_remainder_alt = 0.75

    actual_remainder_alt = mod(num1_alt, num2_alt)
    assert actual_remainder_alt == expected_remainder_alt


def test_mod_division_by_zero():
    """
    Test that mod raises a ZeroDivisionError when the second parameter is zero.
    """
    with pytest.raises(ZeroDivisionError):
        mod(5, 0)


def test_mod_large_integers():
    """
    Test that mod correctly handles very large integers.
    """
    # Arrange
    num1 = 10**20
    num2 = 7
    expected_remainder = 2  # 10**20 % 7 = 2

    # Act
    actual_remainder = mod(num1, num2)

    # Assert
    assert actual_remainder == expected_remainder


def test_mod_incompatible_types():
    """
    Test that mod raises a TypeError when called with incompatible types.
    """
    with pytest.raises(TypeError):
        mod("string", 5)
    with pytest.raises(TypeError):
        mod({}, [])


def test_mod_nan_infinity():
    """
    Test that mod correctly handles NaN and infinity inputs.
    """
    # Test case 1: NaN % 5
    assert math.isnan(mod(float("nan"), 5))

    # Test case 2: 5 % NaN
    assert math.isnan(mod(5, float("nan")))

    # Test case 3: Infinity % 5
    assert math.isnan(mod(float("inf"), 5))

    # Test case 4: 5 % Infinity
    assert mod(5, float("inf")) == 5.0

    # Test case 5: NaN % Infinity
    assert math.isnan(mod(float("nan"), float("inf")))

    # Test case 6: Infinity % NaN
    assert math.isnan(mod(float("inf"), float("nan")))
