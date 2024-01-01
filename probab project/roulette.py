import random
import csv
import matplotlib.pyplot as plt
import numpy as np
def run_roulette_simulation():
    results = []
    for _ in range(1000):
        spin_result = random.randint(0, 36)  # Simulate the roulette spin
        results.append(spin_result)

    with open('roulette_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Spin Result'])
        for result in results:
            writer.writerow([result])

run_roulette_simulation()

def calculate_probabilities():
    red_count = 0
    black_count = 0
    odd_count = 0
    even_count = 0
    specific_number_count = 0
    results=[]

    with open('roulette_results.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            spin_result = int(row[0])
            results.append(spin_result)
            if spin_result in (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
                red_count += 1
            elif spin_result in (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35):
                black_count += 1
            if spin_result % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            if spin_result == 14:  # Replace with the specific number you want to calculate the probability for
                specific_number_count += 1

    total_count = red_count + black_count
    red_probability = red_count / total_count
    black_probability = black_count / total_count
    odd_probability = odd_count / 1000
    even_probability = even_count / 1000
    specific_number_probability = specific_number_count / 1000

    print('Probability of winning on red/black:', red_probability, '/', black_probability)
    print('Probability of winning on odd/even:', odd_probability, '/', even_probability)
    print('Probability of winning on a specific number:', specific_number_probability)
    # Pie chart for the distribution of colors
    colors = ['red', 'black']
    counts = [red_count, black_count]
    plt.pie(counts, labels=colors, autopct='%1.1f%%')
    plt.title('Distribution of Colors')
    plt.show()

    # Bar graph for the probability of winning on different types of bets
    types = ['Red/Black', 'Odd/Even', 'Specific Number']
    probabilities = [red_probability, odd_probability, specific_number_probability]
    plt.bar(types, probabilities)
    plt.title('Probability of Winning on Different Types of Bets')
    plt.show()


calculate_probabilities()

def single_number_bet_simulation(num_simulations):
    outcomes = []
    for _ in range(num_simulations):
        spin_result = random.randint(0, 36)  # Simulate the roulette spin
        outcomes.append(spin_result)

    plt.hist(outcomes, bins=37, range=(-0.5, 36.5), density=True, alpha=0.75)
    plt.title('Probability Distribution for Single-Number Bet')
    plt.xlabel('Number')
    plt.ylabel('Probability')
    plt.show()

single_number_bet_simulation(1000)

def simulated_probability(num_simulations):
    outcomes = []
    for _ in range(num_simulations):
        spin_result = random.randint(0, 36)  # Simulate the roulette spin
        outcomes.append(spin_result)

    expected_probability = 1/37  # Theoretical probability of winning on a single number bet
    #simulated_probability = sum(outcomes) / (num_simulations * 36)  # Calculate the simulated probability
    simulated_probability = outcomes.count(17) / len(outcomes)  # Calculate the simulated probability of any number (17)
    print(f'Theoretical probability: {expected_probability}')
    print(f'Simulated probability: {simulated_probability}')

simulated_probability(10)




def roulette_box_plots(num_simulations):
    single_number_outcomes = [random.randint(0, 36) for _ in range(num_simulations)]
    red_black_outcomes = [random.choice(['red', 'black']) for _ in range(num_simulations)]
    odd_even_outcomes = [random.choice(['odd', 'even']) for _ in range(num_simulations)]

    # Count the frequencies of outcomes
    single_number_counts = {i: single_number_outcomes.count(i) for i in range(37)}
    red_black_counts = {'red': red_black_outcomes.count('red'), 'black': red_black_outcomes.count('black')}
    odd_even_counts = {'odd': odd_even_outcomes.count('odd'), 'even': odd_even_outcomes.count('even')}

    # Plot bar plots with smaller size
    fig, axes = plt.subplots(nrows=3, figsize=(8, 10))

    axes[0].bar(single_number_counts.keys(), single_number_counts.values())
    axes[0].set_title('Single Number Outcomes')
    axes[0].set_xlabel('Number')
    axes[0].set_ylabel('Frequency')

    axes[1].bar(red_black_counts.keys(), red_black_counts.values())
    axes[1].set_title('Red/Black Outcomes')
    axes[1].set_xlabel('Color')
    axes[1].set_ylabel('Frequency')

    axes[2].bar(odd_even_counts.keys(), odd_even_counts.values())
    axes[2].set_title('Odd/Even Outcomes')
    axes[2].set_xlabel('Type')
    axes[2].set_ylabel('Frequency')

    plt.tight_layout()
    plt.show()

roulette_box_plots(1000)

def update_probability(num_black_observed, prior_probability):
    likelihood_black_to_red = 1 - prior_probability  # Likelihood of observing red after black
    for _ in range(num_black_observed):
        posterior_probability = (likelihood_black_to_red * prior_probability) / ((likelihood_black_to_red * prior_probability) + ((1 - likelihood_black_to_red) * (1 - prior_probability)))
        prior_probability = posterior_probability
    return posterior_probability

# Initial probability of winning on red
prior_probability_red = 18/37  # Initial probability of winning on red

# Update the probability after observing 10 consecutive black outcomes
posterior_probability_red = update_probability(10, prior_probability_red)
print(f'Updated probability of winning on red: {posterior_probability_red}')


#Consider a scenario where a player simultaneously places bets on red, black, and a specific number. The multinomial distribution can model the probabilities of winning on each of these outcomes in a single spin.
def roulette_multinomial_distribution(num_simulations):
    outcomes = np.random.choice(['red', 'black', 'specific_number'], p=[18/37, 18/37, 1/37], size=num_simulations)

    red_count = np.sum(outcomes == 'red')
    black_count = np.sum(outcomes == 'black')
    specific_number_count = np.sum(outcomes == 'specific_number')

    plt.figure(figsize=(10, 6))
    plt.bar(['Red', 'Black', 'Specific Number'], [red_count, black_count, specific_number_count])
    plt.title('Multinomial Distribution of Roulette Outcomes')
    plt.xlabel('Outcome')
    plt.ylabel('Frequency')
    plt.show()

roulette_multinomial_distribution(1000)

# Model the number of successful bets (e.g., hitting a specific number) in a fixed number of spins using the Poisson distribution. This is particularly relevant for rare events.
def poisson_distribution_simulation(num_simulations, mean_successes):
    successes = np.random.poisson(mean_successes, num_simulations)

    plt.figure(figsize=(10, 6))
    plt.hist(successes, bins=np.arange(-0.5, mean_successes * 2 + 1.5, 1), density=True, alpha=0.75)
    plt.title('Poisson Distribution Simulation')
    plt.xlabel('Number of Successful Bets')
    plt.ylabel('Probability')
    plt.show()

# Simulate the Poisson distribution for the number of successful bets
poisson_distribution_simulation(1000, 3)  # Example: Mean number of successful bets is 3


#Suppose you're interested in the average winnings over 100 spins. According to the Central Limit Theorem, the distribution of the sample mean of winnings will approach a normal distribution, even if the individual outcomes are not normally distributed.  
def roulette_central_limit_theorem(num_simulations):
    winnings = []
    for _ in range(num_simulations):
        spin_results = [random.randint(0, 36) for _ in range(100)]  # Simulate 100 roulette spins
        total_winnings = sum([1 if result == 17 else -1 for result in spin_results])  # Calculate total winnings
        average_winnings = total_winnings / 100  # Calculate average winnings
        winnings.append(average_winnings)

    # Calculate the mean and standard deviation of the sample
    sample_mean = np.mean(winnings)
    sample_std = np.std(winnings)

    # Create a normal distribution to represent the sample mean
    normal_distribution = np.random.normal(sample_mean, sample_std, 1000)

    # Create a histogram to visualize the distribution of the sample mean
    plt.figure(figsize=(10, 6))
    plt.hist(normal_distribution, bins=30, density=True, alpha=0.75)
    plt.title('Central Limit Theorem Simulation')
    plt.xlabel('Average Winnings')
    plt.ylabel('Probability')
    plt.show()

roulette_central_limit_theorem(1000)


#Analyze the covariance and correlation between the outcomes of different types of bets. For instance, investigate whether winning on red is correlated with winning on even numbers.
def simulate_roulette_spin():
    return random.randint(0, 36)

def roulette_correlation(num_simulations):
    red_outcomes = []
    black_outcomes = []
    single_number_outcomes = []

    for _ in range(num_simulations):
        spin_result = simulate_roulette_spin()

        # Red/Black outcomes (0 for black, 1 for red)
        if spin_result == 0 or spin_result == 00:
            black_outcomes.append(1)  # 1 for black
            red_outcomes.append(0)    # 0 for not red
        elif spin_result % 2 == 0:
            black_outcomes.append(1)  # 1 for black
            red_outcomes.append(0)    # 0 for not red
        else:
            black_outcomes.append(0)  # 0 for not black
            red_outcomes.append(1)    # 1 for red

        # Single Number outcomes
        single_number_outcomes.append(spin_result)

    # Calculate the covariance and correlation between red, black, and single number outcomes
    covariance_red_single_number = np.cov([red_outcomes, single_number_outcomes])[0, 1]
    covariance_black_single_number = np.cov([black_outcomes, single_number_outcomes])[0, 1]
    correlation_red_single_number = np.corrcoef([red_outcomes, single_number_outcomes])[0, 1]
    correlation_black_single_number = np.corrcoef([black_outcomes, single_number_outcomes])[0, 1]

    # Display covariance and correlation
    print(f"Covariance between Red and Single Number: {covariance_red_single_number}")
    print(f"Covariance between Black and Single Number: {covariance_black_single_number}")
    print(f"Correlation between Red and Single Number: {correlation_red_single_number}")
    print(f"Correlation between Black and Single Number: {correlation_black_single_number}")

# Run the simulation and calculate covariance and correlation
roulette_correlation(1000)