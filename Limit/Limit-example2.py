from sympy import Symbol, limit, oo, sympify, diff, lambdify
import numpy as np
import matplotlib.pyplot as plt
x=Symbol('x')
f3 = 1 / x
lim_pinf = limit(f3, x, 0, dir='+')
print(f"when x→0⁺: {lim_pinf}")
lim_ninf=limit(f3,x,0,dir='-')
print(f"when x→0⁻: {lim_ninf}")

if lim_pinf==lim_ninf:
    print("the limit exists")
else:
    print("the limit doesn't exist")
expr=sympify(f3)
derivative = diff(expr, x)
f = lambdify(x, expr, "numpy")
f_prime = lambdify(x, derivative, "numpy")
x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)
y_prime_vals = f_prime(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f(x)", color="blue")

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title("Limit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig('function_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("图像已保存为 function_plot.png")
print("请在文件管理器中查看生成的图像文件")
