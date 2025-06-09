import sympy as sp
from sympy import symbols, sin

x = symbols('x')
f = sin(x)
taylor = f.series(x, 0, 7).removeO()
print(taylor)


def lagrange(f, a, n):
  x_value = 0.5
  taylor_sum = 0
  for r in range(n + 1):
    deriv = f.diff(x, r)
    term = deriv.subs(x, a) / sp.factorial(r) * (x - a)**r
    taylor_sum = term + taylor_sum
    deriv_N = f.diff(x, n + 1)
  remain = deriv_N.subs(x,
                        x_value) / sp.factorial(n + 1) * (x_value - a)**(n + 1)
  return taylor_sum, remain.evalf()


print(lagrange(f, a=0, n=6))
