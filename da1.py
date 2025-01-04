# Simple probability 
 # Probability of rolling a 4 on a six-sided die 
 total_outcomes = 6  
favorable_outcomes = 1 
 # Rolling a 4  
probability_4 = favorable_outcomes / total_outcomes  
print(f"Probability of rolling a 4: {probability_4}")  
import numpy as np  
import matplotlib.pyplot as plt from scipy.stats 
 import norm, poisson, binom, expon  
# Normal Distribution - Quality Control example  
# Generating and plotting a normal distribution  
mean = 50  
std_dev = 10  
samples = np.random.normal(mean, std_dev, 1000)  
plt.figure(figsize=(8, 6))  
plt.hist(samples, bins=30, density=True, alpha=0.6, color='blue')  
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 100)  
plt.plot(x, norm.pdf(x, mean, std_dev), 'r-', lw=2, label='Normal Distribution')  
plt.title('Normal Distribution Example (Quality Control)') plt.xlabel('Values')  
plt.ylabel('Probability Density')  
plt.legend()  