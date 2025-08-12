import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, LogFormatter

# Import data files
plot_data = pd.read_csv('BJH-plot-data.csv')

# Convert imported data to numpy arrays
Radius = plot_data['Radius (A)'].to_numpy()
CPV = plot_data['Pore Volume (cc/g)'].to_numpy()
CSA = plot_data['Pore Surface Area (m2/g)'].to_numpy()
dV = plot_data['dV(r) (cc/A/g)'].to_numpy()
dS = plot_data['dS(r) (m2/A/g)'].to_numpy()

# Optional conversion to nm
Radius_nm = Radius * 0.1
dV_nm = dV * 10

fig1, ax1 = plt.subplots(layout="constrained")
line1, = ax1.plot(Radius, CPV, color='r', marker='s', markeredgecolor='r', markerfacecolor=(1, 0, 0, 0), label='Cumulative Pore Volume')

ax1.set_xlabel(r'Pore Radius ($\mathrm{\AA}$)')
ax1.set_ylabel('Cumulative Pore Volume (cc/g)', color='r')
ax1.tick_params(axis='y', labelcolor='r')

# Create a second y-axis sharing the same x-axis
ax2 = ax1.twinx()

# Plot on the right y-axis
line2, = ax2.plot(Radius, dV, color='b', marker='s', markeredgecolor='b', markerfacecolor=(1, 0, 0, 0), label='dV(r)')
ax2.set_ylabel(r'dV(r) (cc/$\mathrm{\AA}$/g)', color='b')
ax2.tick_params(axis='y', labelcolor='b')

# Combine legends
lines = [line1, line2]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc=0)

ax1.axis((min(10, min(Radius)) * 0.95, max(Radius) * 1.1, 0, max(CPV) * 1.2))
ax2.axis((min(10, min(Radius)) * 0.95, max(Radius) * 1.1, 0, max(dV) * 1.1))

# Set x-axis to log scale
ax1.set_xscale('log')

# Set all major + minor ticks (2–9 per decade)
ax1.xaxis.set_major_locator(LogLocator(base=10))
ax1.xaxis.set_minor_locator(LogLocator(base=10, subs=[2,3,4,5,6,7,8,9], numticks=100))

# Set ticks (locations to show labels at)
tick_positions = [10, 20, 30, 50, 100, 200, 500, 1000]
tick_labels = [str(t) for t in tick_positions]

# Apply ticks and labels
ax1.set_xticks(tick_positions)
ax1.set_xticklabels(tick_labels)

plt.savefig('BJH-V-Angstrom.svg')
plt.savefig('BJH-Angstrom.jpg', dpi=300)


fig2, ax3 = plt.subplots(layout="constrained")
line3, = ax3.plot(Radius_nm, CPV, color='r', marker='s', markeredgecolor='r', markerfacecolor=(1, 0, 0, 0), label='Cumulative Pore Volume')

ax3.set_xlabel(r'Pore width (nm)')
ax3.set_ylabel('Cumulative Pore Volume (cc/g)', color='r')
ax3.tick_params(axis='y', labelcolor='r')

# Create a second y-axis sharing the same x-axis
ax4 = ax3.twinx()

# Plot on the right y-axis
line4, = ax4.plot(Radius_nm, dV_nm, color='b', marker='s', markeredgecolor='b', markerfacecolor=(1, 0, 0, 0), label='dV(r)')
ax4.set_ylabel(r'dV(r) (cc/nm/g)', color='b')
ax4.tick_params(axis='y', labelcolor='b')

# Combine legends
lines = [line3, line4]
labels = [line.get_label() for line in lines]
ax3.legend(lines, labels, loc=0)

ax3.axis((min(1, min(Radius_nm)) * 0.95, max(Radius_nm) * 1.1, 0, max(CPV) * 1.2))
ax4.axis((min(1, min(Radius_nm)) * 0.95, max(Radius_nm) * 1.1, 0, max(dV_nm) * 1.1))

# Set x-axis to log scale
ax3.set_xscale('log')

# Set all major + minor ticks (2–9 per decade)
ax3.xaxis.set_major_locator(LogLocator(base=10))
ax3.xaxis.set_minor_locator(LogLocator(base=10, subs=[2,3,4,5,6,7,8,9], numticks=100))

# Set ticks (locations to show labels at)
tick_positions = [1, 2, 5, 10, 20, 50]
tick_labels = [str(t) for t in tick_positions]

# Apply ticks and labels
ax3.set_xticks(tick_positions)
ax3.set_xticklabels(tick_labels)

plt.savefig('BJH-V-nm.svg')
plt.savefig('BJH-V-nm.jpg', dpi=300)