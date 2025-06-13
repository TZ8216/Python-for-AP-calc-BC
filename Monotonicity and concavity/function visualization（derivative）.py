from sympy import symbols, diff, sympify,lambdify
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x = symbols('x')
func=input("please input an expression:")
expr=sympify(func)
derivative = diff(expr, x)
f = lambdify(x, expr, "numpy")
f_prime = lambdify(x, derivative, "numpy")
x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)
y_prime_vals = f_prime(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f(x)", color="blue")
plt.plot(x_vals, y_prime_vals, label="f'(x)", color="red", linestyle="--")

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title("Function and Derivative")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig('function_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("图像已保存为 function_plot.png")
print("请在文件管理器中查看生成的图像文件")