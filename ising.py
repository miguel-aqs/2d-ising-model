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

def get_net_magnetization(spins):
    return np.mean(spins)


"""---CONFIG STUFF---"""
grid_size = 100
T = 4
steps_per_frame = 50000
graph_length = 100
show_graph = True

"""------------------"""


#note that -1 is black and 1 is white

grid1 = init_lattice(grid_size)

if show_graph == True:
    mag_history = []

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    line, = ax2.plot([], [], color='black')


    ax2.set_xlim(0, graph_length)
    ax2.get_xaxis().set_visible(False)
    ax2.set_ylim(-1.1, 1.1)
else:
    fig, (ax1) = plt.subplots(figsize=(6, 6))

im = ax1.imshow(grid1, cmap='gray', vmin=-1, vmax=1)
#tx = ax2.set_title(get_net_magnetization(grid1))

def update(frame):
    for _ in range(steps_per_frame):
        metropolis(grid1, grid_size, T)
    
    im.set_data(grid1)

    if show_graph == True:
        net_mag = get_net_magnetization(grid1)
        mag_history.append(net_mag)
    
        line.set_data(range(len(mag_history)), mag_history)
        if len(mag_history) > 100:
            ax2.set_xlim(0, len(mag_history))
        return [im, line]
    else:
        return [im]
    
    

ani = animation.FuncAnimation(fig, update, interval=10, blit=True, cache_frame_data=False)

plt.show()