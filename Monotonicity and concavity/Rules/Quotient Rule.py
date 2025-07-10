import sympy as sp

x = sp.symbols('x')

F = sp.sympify(input("please input a function : "))
G = sp.sympify(input("please input another function : "))

Quotient_derivative = sp.diff(F/G, x)

Derv_F = sp.diff(F, x)
Derv_G = sp.diff(G, x)
expr = (G * Derv_F-F*Derv_G)/(G**2)

if sp.simplify(Quotient_derivative - expr) == 0:
    print("Proved the product rule symbolically!")
else:
    print("The expressions are not equivalent. Please check again.")
