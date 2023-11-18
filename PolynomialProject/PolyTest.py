import pytest
from mutation_operators import change_coefficients
from Polynomial import Polynomial  # Import the Polynomial class from your module

def test_init():
    poly = Polynomial([3, 0, 2])
    assert poly.coefficients == [3, 0, 2]

def test_str():
    poly = Polynomial([3, 0, 2])
    assert str(poly) == "3x^2 + 2"

    poly2 = Polynomial([1, -1])
    assert str(poly2) == "1x + -1"

    poly3 = Polynomial([0, 0, 0])
    assert str(poly3) == "0" or str(poly3) == ""

def test_add():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 1, 1]

def test_sub():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [3,-1, 3]

def test_mul():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_product = poly1 * poly2
    assert poly_product.coefficients == [3, -3, 2, -2]

def test_first_degree_polynomial():
    poly = Polynomial([2, -3])  # Represents 2x - 3
    root = poly.find_root_bisection(0, 5)
    assert abs(root - 1.5) < 1e-6

def test_second_degree_polynomial():
    poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
    root = poly.find_root_bisection(1, 2)
    assert abs(root - 2.0**0.5) < 1e-6

def test_third_degree_polynomial():
    poly = Polynomial([1, 0, -2, 0])  # Represents x^3 - 2x
    root = poly.find_root_bisection(-2, 2)
    assert abs(root - 0.0) < 1e-6
   
   # Test with mutated coefficients
def test_mutation_change_coefficients():
    original_poly = Polynomial([3, 0, 2])
    mutated_poly = change_coefficients(original_poly, [1, 1, 1])  # Change to [1, 1, 1]

    # Run your tests with the mutated polynomial
    assert str(mutated_poly) == "1x^2 + 1x + 1"
    assert mutated_poly.evaluate(1) == 3
    # Add more assertions as needed

def test_mutation_on_add():
    # Original polynomial
    original_poly1 = Polynomial([3, 0, 2])
    original_poly2 = Polynomial([1, -1])

    # Mutated polynomial
    mutated_poly1 = change_coefficients(original_poly1, [3, 0, -2])  # Change the last coefficient to -2
    mutated_poly2 = original_poly2  # No change for the second polynomial

    # Perform addition with one mutated polynomial
    poly_sum = mutated_poly1 + mutated_poly2
    expected_sum_result = [3, 1, -1]  # What the result would be if using the mutated coefficients

    # Assert that the test fails (which means the mutation is detected)
    with pytest.raises(AssertionError):
        assert poly_sum.coefficients == expected_sum_result

def test_zero_polynomial():
    zero_poly = Polynomial([0])
    assert str(zero_poly) == "0"
    assert zero_poly.evaluate(5) == 0
    assert zero_poly.evaluate(-3) == 0

def test_polynomial_evaluation():
    poly = Polynomial([2, -4, 0, 3])
    assert poly.evaluate(0) == 3


def test_polynomial_derivative():
    poly = Polynomial([3, -2, 0, 6])
    derivative_coeffs = poly.get_derivative_coefficients()
    assert derivative_coeffs == [9, -4, 0]

def test_multiplication_identity():
    poly = Polynomial([4, 2])
    one_poly = Polynomial([1])
    product = poly * one_poly
    assert product.coefficients == poly.coefficients

def test_multiplication_by_zero():
    poly = Polynomial([1, -5, 3])
    zero_poly = Polynomial([0])
    product = poly * zero_poly
    assert product.coefficients == [0, 0 , 0]

