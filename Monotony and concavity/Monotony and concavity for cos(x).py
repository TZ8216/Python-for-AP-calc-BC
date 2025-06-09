from sympy import symbols, cos, diff

x = symbols('x')
f = cos(x)
f_prime = diff(f, x)
value = f_prime.evalf(subs={x: 0})

if value > 0:
    print("increasing")
elif value <0:
    print("decreasing")
else:
    print("constant")

f_2nd_prime=diff(f_prime,x)
vvalue=f_2nd_prime.evalf(subs={x: 0})
if vvalue >0:
    print("concave up")
elif vvalue <0:
    print("concave down")
else:
    print("neither concave up nor concave down")