import matplotlib.pyplot as plt
import numpy as np
import pickle
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--measurement', help='the measurement we want to plot in the phase diagram')
parser.add_argument('--TT', help='translational diffusion')

args = parser.parse_args()

measurement = args.measurement
TT = args.TT

# Define the ranges for P and v0
P_range = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0, 1.4, 2.0]
v0_range = [0.1, 0.2, 0.5]

# Create empty lists to store the data
v0_values = []
P_values = []
m_values = []

# Retrieve the Da values and corresponding P, v0
for P in P_range:
    for v0 in v0_range:
        # Load the Da value from the corresponding file
        filename = f'P={P}v0={v0}phi=0.05T_R=5e-02T_T={TT}_{measurement}'
        filepath = f'/Users/vv19005/Desktop/Xichen_supervision/2023.05.18/measurements/{measurement}/{filename}'
        with open(filepath, 'rb') as file:
            m = pickle.load(file)
            if type(m)!=float:
                m = np.mean(m)
            
        # Append the values to the lists
        v0_values.append(v0)
        P_values.append(P)
        m_values.append(m)

# Convert the lists to numpy arrays
v0_values = np.array(v0_values)
P_values = np.array(P_values)
m_values = np.array(m_values)

# Plot the phase diagram using scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(v0_values, P_values, s=200, c=m_values, cmap='viridis')

# Add labels and a colorbar
plt.xlabel(r'$v_0$', fontsize=14)
plt.ylabel(r'$P$', fontsize=14)
plt.title(f'Phase Diagram - {measurement}', fontsize=16)
plt.colorbar(label=f'{measurement}')

# Show or save the plot
plt.show()
