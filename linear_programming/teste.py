import numpy as np
import matplotlib.pyplot as plt
import pulp

N = 10
x = np.linspace(1, 10, N)
y = 6 * x * (1 + 0.1 * np.random.normal(size=N)) + 1

# Create a linear programming problem
lp_problem = pulp.LpProblem("Linear_Programming_Problem", pulp.LpMinimize)

# Define decision variables
x_vars = [pulp.LpVariable(f'x_{i}', lowBound=0) for i in range(N)]

# Set up the objective function
lp_problem += pulp.lpSum(x_vars)

# Define the inequality constraints
for j in range(2):
    sign = 1 if j == 0 else -1
    for i in range(N):
        lp_problem += sign * x_vars[i] >= x[i] * sign

# Define the equality constraints (the same as ineq_a)
ineq_b = y.tolist()
for i in range(N):
    ineq_b.append(-y[i])

# Solve the linear programming problem
lp_problem.solve()

# Print the optimized values
print([x_var.varValue for x_var in x_vars])

# Scatter plot of the data points
plt.scatter(x, y)
plt.savefig('teste.png')
