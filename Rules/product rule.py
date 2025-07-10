import sympy as sp
x = sp.symbols('x')
F = sp.sympify(input("please input a function F(x): "))
G = sp.sympify(input("please input another function G(x): "))
product_derivative = sp.diff(F * G, x)
Derv_F = sp.diff(F, x)
Derv_G = sp.diff(G, x)
expr = F * Derv_G + G * Derv_F
if sp.simplify(product_derivative - expr) == 0:
    print("Proved the product rule symbolically!")
else:
    print("The expressions are not equivalent. Please check again.")