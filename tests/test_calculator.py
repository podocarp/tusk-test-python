import pytest
import math
from utils.calculator import add, mul


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


def test_mul_nan_infinity():
    """
    Test that mul correctly handles NaN and infinity inputs.
    """
    # Test case 1: NaN * 5
    assert math.isnan(mul(float("nan"), 5))

    # Test case 2: 5 * NaN
    assert math.isnan(mul(5, float("nan")))

    # Test case 3: Infinity * 5
    assert mul(float("inf"), 5) == float("inf")

    # Test case 4: -Infinity * 5
    assert mul(float("-inf"), 5) == float("-inf")

    # Test case 5: Infinity * NaN
    assert math.isnan(mul(float("inf"), float("nan")))
