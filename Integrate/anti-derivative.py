import sympy as sp
try:
  # Input function expressions
  x = sp.symbols('x')
  expr = input("please input an expression:")  
  anti_derv=sp.integrate(expr,x)
  print(anti_derv)#indefinite integral
  integral = sp.integrate(expr,(x,1,2))
  print(integral)#definite integral
  point_B=sp.integrate(expr,(x,2))
  point_A=sp.integrate(expr,(x,1))
  minus_BA=point_B-point_A
  if minus_BA==integral:
    print("prove the fundamental theorem !")
  else:
    print("something goes wrong, please check it again")
except Exception as e:
  print(f"Error: {e}")