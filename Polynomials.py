class Polynomial:

    def __init__(self, *coefficients):
        """ input: coefficients are in the form a_n, ...a_1, a_0
        """
        # for reasons of efficiency we save the coefficients in reverse order,
        # i.e. a_0, a_1, ... a_n
        self.coefficients = coefficients[::-1]  # tuple is also turned into list

    def __repr__(self):
        """
        method to return the canonical string representation
        of a polynomial.

        """
        # The internal representation is in reverse order,
        # so we have to reverse the list
        return "Polynomial" + str(self.coefficients[::-1])

    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x ** index
        return res


p = Polynomial(4, 0, -4, 3, 0)
for x in range(-3, 3):
    print(x, p(x))

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3, 3, 50)
F = p(x)
plt.plot(x, F)
plt.show()