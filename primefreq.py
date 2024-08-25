import numpy as np
import matplotlib.pyplot as plt
from sympy import sieve, prime

def generate_primes_and_gaps(n):
    primes = list(sieve.primerange(2, n))
    gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
    return primes, gaps

def plot_gap_frequency(gaps, max_gap=50):
    gap_counts = np.bincount(gaps)
    gap_counts = gap_counts[:max_gap+1]  # Limit to max_gap for better visualization
    
    plt.figure(figsize=(12, 6))
    plt.bar(range(len(gap_counts)), gap_counts, align='center')
    plt.title('Frequency Distribution of Prime Gaps')
    plt.xlabel('Gap Size')
    plt.ylabel('Frequency')
    plt.xticks(range(0, max_gap+1, 2))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    n = 100000  # Generate primes up to this number
    max_gap_to_display = 50  # Maximum gap size to display in the plot

    print(f"Generating primes up to {n}...")
    primes, gaps = generate_primes_and_gaps(n)
    
    print(f"Number of primes generated: {len(primes)}")
    print(f"Number of gaps calculated: {len(gaps)}")
    
    print("Plotting frequency distribution...")
    plot_gap_frequency(gaps, max_gap_to_display)

    print(f"Largest gap found: {max(gaps)}")
    print(f"Average gap size: {sum(gaps)/len(gaps):.2f}")

if __name__ == "__main__":
    main()
