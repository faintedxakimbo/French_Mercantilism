import matplotlib.pyplot as plt
import numpy as np

# Demand curve parameters
a1, b1 = 112, 21.54
a2, b2 = 276, 100.57
MC = 0  # Marginal Cost

# Range of quantities
Q = np.linspace(0, 120, 200)

# Inverse demand equations: P = (a - Q) / b
P1 = (a1 - Q) / b1
P2 = (a2 - Q) / b2

#maximum prices
p_max_oligop = a1 / b1
p_max_compet = a2 / b2

#Deadweight loss and Surplus analysis
Producer_surplus_oligopoly = 56 * 2.6
Consumer_suplus_oligopoly = .5 * ((p_max_oligop - 2.6) * 56)
Producer_surplus_compet = 100 * 1.75
Consumer_surplus_compet = .5 * ((p_max_compet - 1.75) * 100)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(Q, P1, label='Oligopoly Demand Curve ', color='blue')
plt.plot(Q, P2, label='Smuggler Demand Curve ', color='green')
plt.scatter(56, 2.6, color='red', label='Oligopoly/Guild (56, 2.6)')
plt.scatter(100, 1.75, color='purple', label='Competitive/ Smuggler (100, 1.75)')

#cs shades
Q_fill1 = np.linspace(0, 56, 200)
P_fill1 = (a1 - Q_fill1) / b1
Q_fill2 = np.linspace(0, 100, 200)
P_fill2 = (a2 - Q_fill2) / b2
plt.fill_between(Q_fill1, P_fill1, 2.6, color='#66c2a5', alpha=0.6, label='Consumer Surplus under Oligopoly')  # teal-green


#ps Shades
#Fill producer surplus (PS) for both curves
plt.fill_between(Q_fill1, 2.6, 0, color='#fc8d62', alpha=0.6, label='Producer Surplus under Oligopoly')  # orange-salmon
plt.fill_between(Q_fill2, 1.75, 0, color='#ffd92f', alpha=0.6, label='Producer Surplus under Smuggler 2')  # golden yellow

#dwl shades
# Create quantity range between Q1 and Q2
Q_gap = np.linspace(56, 100, 200)

# Calculate prices on both demand curves over that quantity range
P1_gap = (a1 - Q_gap) / b1  # Oligopoly demand curve
P2_gap = (a2 - Q_gap) / b2  # Competitive/smuggler demand curve

plt.fill_between(Q_gap, P1_gap, P2_gap, color='#e78ac3', alpha=0.7, label='DWL Triangle')  # pink-violet
plt.fill_between(Q_gap, P2_gap, 0, color='#a6d854', alpha=0.5, label='DWL Rectangle')  # lime green




plt.title('Inverse Demand Curves (Guild vs Smuggler)')
plt.xlabel('Quantity (Q)')
plt.ylabel('Price (Livre Tournois)')
plt.grid(True)
plt.legend()
plt.xlim(0, 120)
plt.ylim(0, 5)
plt.show()

#calculations
# Parameters at equilibrium points
Q1, Q2 = 56, 100
P1_val = 2.6
P2_val = 1.75

# DWL triangle: between the demand curves
dwl_triangle = 0.5 * (P1_val - P2_val) * (Q2 - Q1)

# DWL rectangle: below P2 down to MC = 0
dwl_rectangle = (Q2 - Q1) * P2_val

# Total DWL
total_dwl = dwl_triangle + dwl_rectangle

print("Oligopoly Demand Curve: Q = 112 - 21.54P")
print("Smuggler Demand Curve: Q = 276 - 100.57P")
print("Producer Suplus under Oligopoly: ", Producer_surplus_oligopoly)
print("Consumer Surplus under Oligopoly: ",Consumer_suplus_oligopoly)
print("Producer Surplus under Smuggler: ", Producer_surplus_compet)
print(f"DWL Triangle: {dwl_triangle:.2f}")
print(f"DWL Rectangle: {dwl_rectangle:.2f}")
print(f"Total DWL: {total_dwl:.2f}")
