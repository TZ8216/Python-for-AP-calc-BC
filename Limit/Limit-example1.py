from sympy import symbols, limit, oo, simplify, lambdify, sympify
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=symbols('x')
f1=(x**3+1)/(x+1)
func=simplify(f1)
print(func)
lim1=limit(f1,x,-1)
print(f"lim (x**3+1)/(x+1) when x→-1: {lim1}")  
lim1_right=limit(f1,x,-1,dir='+')
print(f"lim (x**3+1)/(x+1) when x→-1+: {lim1_right}")
lim1_left=limit(f1,x,-1,dir='-')
print(f"lim (x**3+1)/(x+1) when x→-1−: {lim1_left}")
if lim1_left == lim1_right:
    print("The limit of the segment function exists when x→-1, and the value is:", lim1_left)
else:
    print("The limit of the segmented function does not exist when x→-1 (the left and right limits are not equal)")
expr=sympify(f1)
f = lambdify(x, expr, "numpy")
x_vals = np.linspace(-10, 10, 400)
x_vals = x_vals[x_vals != -1]
y_vals = f(x_vals)
plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, label='f(x)', color='black')
y_hole = 3 
plt.scatter([-1], [y_hole],
            facecolors='none',
            edgecolors='black',
            label='hole at x=-1')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("limit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig('function_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("画像已保存为 function_plot.png")
print("请在文件管理器中查看生成的图像文件")
