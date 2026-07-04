import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, TextBox
from matplotlib.colors import ListedColormap

"""---CONFIG STUFF---"""
grid_size = 75
initial_state = 0 # 0 = completely random, 1 = all +1 spin, -1 = all -1 (no in between)
pctg_impurities = 0.39

T = 1.9 # initial temperature
steps_per_frame = 100000

show_graph = True
graph_length = 100

show_bottom_controls = True
input_mode = 1 # 0 = Use slider, 1 = Use text box

"""------------------"""


colors = ["blue", "black", "red"]
custon_cmap = ListedColormap(colors)

def init_lattice(N):
    if initial_state == 0:
        p_spin = (1 - pctg_impurities) / 2
        spins = np.random.choice([0, -1, 1], size=(N, N), p=[pctg_impurities, p_spin, p_spin])
    elif initial_state == 1:
        p_spin = 1 - pctg_impurities
        spins = np.random.choice([0, -1, 1], size=(N, N), p=[pctg_impurities, 0, p_spin])
    elif initial_state == -1:
        p_spin = 1 - pctg_impurities
        spins = np.random.choice([0, -1, 1], size=(N, N), p=[pctg_impurities, p_spin, 0])
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

    if spins[i, j] == 0:
        return

    current_spin = spins[i, j]
    neighbors_sum = get_neighbors_sum(spins, i, j, N)

    dE = 2 * J * current_spin * neighbors_sum

    if dE <= 0 or random.random() < np.exp(-dE / T):
        spins[i, j] *= -1

def get_net_magnetization(spins):
    active_spins = spins[spins != 0]
    return np.mean(active_spins) if len(active_spins) != 0 else 0.0




#note that -1 is black and 1 is white

grid1 = init_lattice(grid_size)

mag_history = []

num_cols = 2 if show_graph else 1
num_rows = 2 if show_bottom_controls else 1
height_ratios = [20, 1] if show_bottom_controls else [1]
width_ratios = [1, 1] if show_graph else [1]


fig = plt.figure(figsize=(11 if show_graph else 6, 6 if show_bottom_controls else 5.5))
fig.canvas.manager.set_window_title('2D Ising Model Simulation')
gs = fig.add_gridspec(num_rows, num_cols, 
                      width_ratios=width_ratios, 
                      height_ratios=height_ratios, 
                      wspace=0.3, hspace=0.4)


ax1 = fig.add_subplot(gs[0, 0])  # Grid is always top-left

if show_graph:
    ax2 = fig.add_subplot(gs[0, 1])  # Graph is top-right
    line, = ax2.plot([], [], color='black')
    ax2.set_xlim(0, graph_length)
    ax2.get_xaxis().set_visible(False)
    ax2.set_ylim(-1.1, 1.1)

    graph_title = ax2.set_title("Net Magnetization", fontsize=10)

if show_bottom_controls:
    ax_control = fig.add_subplot(gs[1, :]) 
    
    if input_mode == 0:
        t_slider = Slider(ax_control, 'Temperature (T)', 0.1, 5.0, valinit=T, valfmt='%1.2f')
    elif input_mode == 1:
        t_box = TextBox(ax_control, 'Enter Temperature (T): ', initial=str(T))

im = ax1.imshow(grid1, cmap=custon_cmap, vmin=-1, vmax=1)

def update(frame):

    if show_bottom_controls:
        if input_mode == 0:
            current_T = t_slider.val
        elif input_mode == 1:
            try:
                current_T = float(t_box.text)
            except ValueError:
                current_T = T  # Fallback to initial config T if box is blank/invalid
    else:
        current_T = T
    
    for _ in range(steps_per_frame):
        metropolis(grid1, grid_size, current_T)
    
    im.set_data(grid1)

    if show_graph:
        net_mag = get_net_magnetization(grid1)
        mag_history.append(net_mag)
    
        line.set_data(range(len(mag_history)), mag_history)
        if len(mag_history) > 100:
            ax2.set_xlim(0, len(mag_history))
        
        graph_title.set_text("Net Magnetization (M):")

        return [im, line]
    else:
        return [im]
    
    

ani = animation.FuncAnimation(fig, update, interval=10, blit=True, cache_frame_data=False)

plt.show()