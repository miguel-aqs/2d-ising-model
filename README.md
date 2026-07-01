# 2D Ising Model - Monte Carlo Simulation

> First of all, it's pronounced "EE-zing" not "EYE-zing" technically but no one seems to care.

This is a simple Monte Carlo Markov Chain simulation made with the intent to model magnets as a large grid of cells, each representing an atom's individual 'spin' or what can be thought of as magnetic charge.

Each atom on the grid tends toward the action of least energy. At low temperatures, the energy of neighboring spins attempting to align dominates, forcing the lattice to rapidly minimize energy and snap into giant, highly ordered ferromagnetic domains. These will, granted a large enough grid and along enough time, all eventually align to either +1 or -1. 

Raising the temperature past a certain critical temperature dissolves the magnetic structure into high-entropy, uncorrelated static flipping back and forth as thermal energy is injected, overpowering magnetic bonds.

These probabilities are governed by the Boltzmann distribution, through a Hamiltonian. This Hamiltonian takes the form of a Metropolis algorithm in the code.

In 1944, Lars Onsager solved the 2D Ising model, finding the critical temperature at which the magnet loses its ferromagnetism to be at roughly `T ≈ 2.269`.

*Note that Boltzmann's constant is set to 1 in order to avoid underflow errors, so T is measured in natural units.*

## Parameters
The parameters that can be easily adjusted in `ising.py` are:
* **Grid size** (Resolution of the atomic lattice)
* **Steps per frame** (Math steps calculated before updating the screen)
* **Temperature** (`T`)
* **Show graph** (Toggleable)

## Recommended Settings
Note that this was made on a laptop, so has that level of hardware in mind.

* **For a smooth UI:** Use a `100x100` to `150x150` grid size with `40,000` to `50,000` maximum steps per frame.
* **For deep data/large clusters:** Bump steps up to `100,000` (expect minor frame lag depending on your CPU).
* **If the slider feels laggy:** Simply lower `steps_per_frame` until the UI runs smoothly.
* Hiding the slider and/or graph can also allow larger grid sizes or steps per frame.

## Dependencies
This project is built using standard Python and requires the following external libraries:
* **NumPy** - For efficient multidimensional grid manipulation and math.
* **Matplotlib** - For handling the live, real-time GUI animation.

## Changelog

### [July 1, 2026]
* Added a toggleable graph feature to show net magnetization of the lattice grid with real-time history.
* Optimized with Matplotlib's blit engine.
* Added a toggleable slider for temperature.
* Revamped GUI organization code.

### [June 30, 2026]
* Built the main Metropolis algorithm
* Created the grid from a NumPy and Matplotlib array
* Used `animation.FuncAnimation` to display the changing spin configurations live.


## Credits

* Credit to Revimime for compiling the research into molecular thermodynamics and ferromagnetism.
* Credit to Mulletgoneviral for the rickrolls and slandering macbooks.

## Learn More
Read more about the physics [here](https://en.wikipedia.org/wiki/Ising_model).
Learn more about the math and the Hamiltonian [here](https://www.youtube.com/watch?v=BHHoTagq03A).
