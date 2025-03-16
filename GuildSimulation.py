import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


# If you would like to change the number of workers in the simulation, simply add more names to the list. 
worker_names = [
    "Julien", "Jean", "Pierre", "Nicolas",
    "Etienne", "Vincent", "Henri", "Antoine", "Alexandre"
]
workerDict = {name: random.randint(1, 25) for name in worker_names}
user_bank = int(0)
base_bank = int(0)
round_number = 1

# Data storage for plotting
SmugglerToWorkerRatios = []
cheat_odds = []
individual_revenues = []

# 3D plot setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



while round_number < 61:
    worker_count = len(workerDict) + 1
    smuggle_workers = [name for name, value in workerDict.items() if value == 1]
    
    # 1/7 chance of smuggler being caught. You can change the odds by changing '7' to whatever you'd like
    for smuggler in smuggle_workers:
        if random.randint(1, 7) == 1:
            print(f"{smuggler} has been caught smuggling")
            workerDict.pop(smuggler)
            worker_count -= 1

    smuggler_count = len(smuggle_workers)

    user_choice_prompt = 'c'
   
#income algorithms: The below values are given from the 2nd model and informed by qualititaitve data from Tobacco markets of Grenoble
    x = worker_count
    y = smuggler_count
    SmugglerToWorkerRatio = y / x
    oligopoly_revenue = int(98)
    smuggler_surplus = int(175)

# The given Individual revenue function is the function where productivity is maximized at a sensible, though selected, value of 4 workers.
#(x variable) and the presence of smuggling (y variable) is considered unambigously harmful to revenue.
# In other words: THE FUNCTION SHOULD ALWAYS BE DOWNWARD SLOPING
# When changing the revenue function keep in mind A. Whether the function is parabolic, linear or exponential
# and B. the individual functions of x (the number of workers) and y (the number of smugglers) on income.

    individual_revenue = -0.2 * (x ** 2) + 1.6 * x - 2.4 * y + 14.8
    
    oligopoly_surplus = (individual_revenue * worker_count)
    if smuggler_count > 0:
        smuggle_revenue = (((smuggler_surplus - oligopoly_revenue) / (SmugglerToWorkerRatio)) + individual_revenue)
    else:
        smuggle_revenue = ((smuggler_surplus - oligopoly_revenue) + individual_revenue)
        dummy_condition = 'blue'

    if user_choice_prompt == 's':
        user_bank += smuggle_revenue if dummy_condition != 'blue' else 0
    else:
        user_bank += individual_revenue
    base_bank += individual_revenue
    print(f"{worker_count} Workers")
    print(f"{smuggler_count} Smuggler(s)")
    print(f"Individual revenue: {individual_revenue}")
    print(f"Smuggle revenue: {smuggle_revenue}")
    print(f"User bank: {user_bank}")



    # AI strategy for deciding whether or not to cheat
    base_pace = (base_bank + (individual_revenue * (60 - round_number)))
    
    for i in workerDict:
        if base_pace < 600:
            workerDict[i] = random.randint(1, 8)
            cheat_odd = .125
        elif base_pace < 850:
            workerDict[i] = random.randint(1, 12)
            cheat_odd = .083
        elif base_pace < 1000:
            workerDict[i] = random.randint(1, 17)
            cheat_odd = .059
        elif base_pace < 1250:
            workerDict[i] = random.randint(1, 20)
            cheat_odd = .05
        elif base_pace >= 1250:
            workerDict[i] = random.randint(1, 100)
            cheat_odd = .01
        else:
            workerDict[i] = random.randint(1, 20)
            cheat_odd = .05
            
    # Stores data for plotting
    SmugglerToWorkerRatios.append(SmugglerToWorkerRatio)
    cheat_odds.append(cheat_odd)
    individual_revenues.append(individual_revenue)
    
    print(f'Month {round_number} complete!')
    print(f'base pace: {base_pace}')
    round_number += 1
    

# After the simulation loop, we plot the 3D graph
ax.scatter(SmugglerToWorkerRatios, cheat_odds, individual_revenues, c='b', marker='o')

ax.set_xlabel('Smuggler To Worker Ratio')
ax.set_ylabel('Cheat Odds')
ax.set_zlabel('Individual Revenue')

data = pd.DataFrame({
    'Smuggler_To_Worker_Ratio': SmugglerToWorkerRatios,
    'Cheat_Odds': cheat_odds,
    'Individual_Revenue': individual_revenues
})

# Fits the model
model = ols("Individual_Revenue ~ Smuggler_To_Worker_Ratio + Cheat_Odds", data).fit()
# Prints the summary
print(model.summary())
# Performs analysis of variance on fitted linear model
anova_results = anova_lm(model)
print('\nANOVA results')
print(anova_results)
plt.show()

print(f'Over a 60 month period, total individual income of a cooperative member is expected to be {user_bank}')