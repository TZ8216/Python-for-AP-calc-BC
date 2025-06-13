> **Comparing the Slope and Growth Trend Between Different Functions (Monotonicity & Concavity)**

## 📊 Comparison of Slope and Growth Trend

### *(Monotonicity & Concavity of Functions)*

This section investigates how the **first** and **second derivatives** reflect a function’s behavior, specifically:

* 🔹 **Slope (first derivative)** → tells us when the function is increasing or decreasing
* 🔹 **Concavity (second derivative)** → tells us how the rate of change itself changes (acceleration/deceleration)

### 🔧 Derivative Definitions

#### 👉 First Derivative (Slope)

The first derivative of a function is defined as:

```latex
$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$
```

It represents the **instantaneous rate of change** — in simple terms, the slope of the tangent line.

#### 👉 Second Derivative (Concavity)

Using the same limit approach, the second derivative is:

```latex
$$
f''(x) = \lim_{h \to 0} \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}
$$
```

This tells us the **growth trend** (whether the slope is increasing or decreasing).

### 🧪 Code Example

Below is a Python snippet using `Matplotlib` to visualize a function and its derivative:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
f = np.sin(x)
f_prime = np.cos(x)

plt.plot(x, f, label='f(x)', color='blue')
plt.plot(x, f_prime, label="f'(x)", color='red', linestyle='--')
plt.title('Function and Derivative')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
```

---

### 📌 Observations

* When `f'(x) > 0`, the function is increasing.
* When `f''(x) > 0`, the slope is increasing (concave up).
* This behavior is crucial in modeling **physical motion**, **optimization**, and **economic trends**.
  
