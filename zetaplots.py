import numpy as np
import matplotlib.pyplot as plt
import math as mt

yvaluesMain = []
beta = 10
terms = 25


# Define the range of values for num_terms
x_values = np.arange(1, terms +1 )
alpha_values = array = np.linspace(0, 1, 100)

for i in range(1,terms +1 ):
    yvalues = [];

    def thisRho(alpha,beta, sumToValue):
        sum_result = 0.000
        for n in range(1, i):
            sum_result += (-1)**(n-1) * np.sin(mt.log(beta * n)) / n**alpha
        return sum_result

    for alpha in alpha_values:
        yvalues.append(thisRho(alpha, beta, i))   
    
    yvaluesMain.append(yvalues)

print(yvaluesMain[2])

# Plot the graphs
try:
    for n in range(terms):
        if n % 2 == 0:  # Even
            plt.plot(alpha_values, yvaluesMain[n], color='red', label=f'Term {n+1}')
        else:  # Odd
            plt.plot(alpha_values, yvaluesMain[n], color='green', label=f'Term {n+1}')
    plt.xlabel('Real part $\Re(s)$')
    plt.ylabel('Pertubatations of $\sin(\ln(b) x)$')
    plt.title('Pertubatations')
    plt.legend()
    plt.grid(True)
    plt.show()
except Exception as e:
    print("An error occurred while plotting:", e)
