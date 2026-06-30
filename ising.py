import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init_lattice(N):
    spins = np.random.choice([-1, 1], size=(N, N))
    return spins

def get_neighbors_sum(spins, i, j, N):
    top = spins[(i-1) % N, j]
    bottom = spins[(i+1) % N, j]
    left = spins[i, (j-1) % N]
    right = spins[i, (j+1) % N]
    
    return top + bottom + left + right


def metropolis(spins, N, T, J=1.0):
    i = random.randint(0, N-1)
    j = random.randint(0, N-1)

    current_spin = spins[i, j]
    neighbors_sum = get_neighbors_sum(spins, i, j, N)

    dE = 2 * J * current_spin * neighbors_sum

    if dE <= 0 or random.random() < np.exp(-dE / T):
        spins[i, j] *= -1



#config stuff
grid_size = 150
T = 2.269
steps_per_frame = 50000

grid1 = init_lattice(grid_size)

fig, ax = plt.subplots()

#-1 is black and 1 is white

im = ax.imshow(grid1, cmap='gray', vmin=-1, vmax=1)

def update(frame):
    for _ in range(steps_per_frame):
        metropolis(grid1, grid_size, T)
    im.set_data(grid1)
    return [im]

# Create the live animation window
ani = animation.FuncAnimation(fig, update, interval=10, blit=True, cache_frame_data=False)

plt.show()