import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt


def initialize(N):
    ''' Set up an NnX array with spins randomly initialized to -1 or +1'''
    state = 2 * np.random.randint(2, size=(N, N)) - 1
    return state


def flip_site(lattice, beta):
    '''Flip a site using Metropolis algo'''
    for i in range(N):
        for j in range(N):
            # select a random site at coordinates a, b
            a = np.random.randint(0, N)
            b = np.random.randint(0, N)
            # what is the state of that site:
            s = lattice[a, b]
            # nearest neighbors ... %N applies periodic boundary conditions
            nb = lattice[(a + 1) % N, b] + lattice[a, (b + 1) % N] + lattice[(a - 1) % N, b] + lattice[a, (b - 1) % N]
            # delta_energy of flipping the current site
            delta_energy = 2 * s * nb
            if delta_energy < 0:
                s *= -1 # if delta_energy is neg, flip the site
            elif rand() < np.exp(-delta_energy * beta):
                s *= -1 # if delta_energy is not neg, flip with specified probability
            lattice[a, b] = s # update site with new spin state
    return lattice


def energy(lattice):
    '''Compute the energy level. This is a weighted summation really, O(N^2)'''
    energy = 0
    for i in range(len(lattice)):
        for j in range(len(lattice)):
            S = lattice[i, j]
            nb = lattice[(i + 1) % N, j] + lattice[i, (j + 1) % N] + lattice[(i - 1) % N, j] + lattice[i, (j - 1) % N]
            energy += -nb * S
    return energy


def magnetization(lattice):
    '''Magnetization is the sum across the entire lattice'''
    m = np.sum(lattice)
    return m


## Simulation spec
nt = 32  # number of temperature points
N = 10  # size of the lattice, N x N
equilibrium_steps = 16  # number of MC sweeps for equilibration
monte_carlo_steps = 16  # number of MC sweeps for calculation

T = np.linspace(1.53, 3.28, nt); # temperature spacing
E, M, C, X = np.zeros(nt), np.zeros(nt), np.zeros(nt), np.zeros(nt) # arrays with values for each temperature step
n1, n2 = 1.0 / (monte_carlo_steps * N * N), 1.0 / (monte_carlo_steps * monte_carlo_steps * N * N) # normalization factors

# ----------------------------------------------------------------------
#  MAIN PART OF THE CODE
# ----------------------------------------------------------------------
for temperature_step in range(nt):
    cumulative_energy = cumulative_magnetization = cumulative_energy_squared = cumulative_magnetization_squared = 0
    simulated_lattice = initialize(N)
    iT = 1.0 / T[temperature_step]; # inverse temperature ; faster to compute outside loop
    iT2 = iT * iT; # inverse temperature squared ; faster to compute outside loop

    # prep the lattice into a relative equilibrium state for this temperature
    # Think of this part as allowing the system to adjust to the new temperature
    for i in range(equilibrium_steps):  # this range should be sufficient to allow lattice to relax.
        flip_site(simulated_lattice, iT)  # Agitate the lattice by flipping random sites

    # Now that the system has been relaxed, conduct the actual experiments, accumulating
    # energy and magnetization values to be averaged latter.
    for i in range(monte_carlo_steps):
        flip_site(simulated_lattice, iT)
        e = energy(simulated_lattice)  # calculate the energy
        m = magnetization(simulated_lattice)  # calculate the magnetisation

        # update the accumulators
        cumulative_energy = cumulative_energy + e
        cumulative_magnetization = cumulative_magnetization + m
        cumulative_magnetization_squared = cumulative_magnetization_squared + m * m
        cumulative_energy_squared = cumulative_energy_squared + e * e

    # Averaging and normalizing to compute energy, magnetization, heat capacity, and susceptibility
    E[temperature_step] = n1 * cumulative_energy
    M[temperature_step] = n1 * cumulative_magnetization
    C[temperature_step] = (n1 * cumulative_energy_squared - n2 * cumulative_energy * cumulative_energy) * iT2
    X[temperature_step] = (n1 * cumulative_magnetization_squared - n2 * cumulative_magnetization * cumulative_magnetization) * iT

figure = plt.figure(figsize=(18, 10));  # plot the calculated values

# ENERGY PLOT
sub_plot = figure.add_subplot(2, 2, 1);
plt.scatter(T, E, s=50, marker='o', color='IndianRed')
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Energy ", fontsize=20);
plt.axis('tight');

# MAGNETIZATION PLOT
sub_plot = figure.add_subplot(2, 2, 2);
plt.scatter(T, abs(M), s=50, marker='o', color='RoyalBlue')
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Magnetization ", fontsize=20);
plt.axis('tight');

# HEAT CAPACITY
sub_plot = figure.add_subplot(2, 2, 3);
plt.scatter(T, C, s=50, marker='o', color='IndianRed')
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Specific Heat ", fontsize=20);
plt.axis('tight');

# SUSCEPTIBILITY
sub_plot = figure.add_subplot(2, 2, 4);
plt.scatter(T, X, s=50, marker='o', color='RoyalBlue')
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Susceptibility", fontsize=20);
plt.axis('tight');