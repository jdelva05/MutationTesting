# mutation_operators.py

from Polynomial import Polynomial

def change_coefficients(polynomial, new_coefficients):
    # Ensure the input is a Polynomial instance
    if not isinstance(polynomial, Polynomial):
        raise TypeError("The object must be an instance of the Polynomial class.")
    
    # Mutate the coefficients
    polynomial.coefficients = new_coefficients

    return polynomial  # Return the mutated Polynomial object
