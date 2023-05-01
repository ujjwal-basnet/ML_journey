# Derivation of Sigmoid Function

The sigmoid function is a commonly used activation function
and it is represented by sigma(x) 
let sigmoid functin be  = f(X)

f(x) = 1 / (1 + e^(-x))
where e is Euler's number, approximately equal to 2.71828.

To derive the sigmoid function, we can start by expressing it in terms of its output y and input x:


y = 1 / (1 + e^(-x))
Next, we can differentiate both sides of the equation with respect to x:


dy/dx = d/dx (1 / (1 + e^(-x)))
Using the quotient rule, we can simplify the right-hand side of the equation:


dy/dx = -(1 / (1 + e^(-x))^2) * d/dx (1 + e^(-x))
The derivative of 1 + e^(-x) with respect to x is simply e^(-x):


dy/dx = -(1 / (1 + e^(-x))^2) * e^(-x)
Now, we can substitute y back into the equation:


dy/dx = -(y^2) * e^(-x)
Multiplying both sides of the equation by (1 + e^(-x)) and expanding the right-hand side yields:


dy/dx * (1 + e^(-x)) = -y^2 + y
We can isolate dy/dx on one side of the equation:


dy/dx = y * (1 - y)
This is the derivative of the sigmoid function with respect to x. We can also express it in terms of the function f(x):


dy/dx = f(x) * (1 - f(x))
Therefore, the derivative of the sigmoid function is given by:


f'(x) = f(x) * (1 - f(x))
This derivative is useful in neural network training for backpropagation, which adjusts the weights of connections between neurons based on the error between predicted and actual output
