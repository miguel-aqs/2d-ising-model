# 2D Ising Model - Monte Carlo Simulation

> First of all, its pronounced "EE-zing" not "EYE-zing" technically but no one seems to care.

This is a simple Monte Carlo Markov Chain simulation made with the intent to model magnets as a large grid of cells each representing an atom's individual 'spin' or what can be thought of as magnetic charge.

## Parameters
The parameters that can be easily adjusted in `ising.py` are:
* **Grid size** (Resolution of the atomic lattice)
* **Steps per frame** (Math steps calculated before updating the screen)
* **Temperature** (`T`)

## History

In 1944, Lars Onsager solved the 2D Ising model, finding the critical temperature at which the magnet will no longer become ferromagnetic to be at roughly `T ≈ 2.269`.

*Note that Boltzmann's constant is set to 1 in order to avoid underflow errors, so T is measured in natural units.*

## Dependencies
This project is built using standard Python and requires the following external libraries:
* **NumPy** - For efficient multidimensional grid manipulation and math.
* **Matplotlib** - For handling the live, real-time GUI animation.

## Learn More
Read more about the physics [here](https://en.wikipedia.org/wiki/Ising_model).
