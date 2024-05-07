## Variational Quantum Ramsey Interferometry Simulation

This project explores the simulation of a variational quantum Ramsey interferometry circuit for frequency estimation.

### Background

The project builds upon the following concepts:

* **Variational Quantum Eigensolvers (VQEs):** A type of quantum algorithm for solving eigenvalue problems.
* **Variational Quantum Circuits (VQCs):** Quantum circuits where some parameters are variable and can be optimized.
* **Ramsey Interferometry:** A technique used in quantum metrology for precise frequency estimation.
* **Atomic Clocks:** The most precise timekeeping devices, and a key application of Ramsey interferometry.

### Reference Material

The project references the paper "Optimal metrology with programmable quantum sensors" by Christian D. Marciniak et al., which is summarized in a document titled "Q-sensing" located in our GitHub repository.

### Project Goals

1. **Simulate a Variational Quantum Ramsey Interferometer Circuit:** The project aims to create a simulation of a VQC specifically designed for Ramsey interferometry. This simulation is implemented in the Jupyter Notebook file `optimal_ramsey.ipynb`.
2. **Convergence of the Cost Function:** The simulation optimizes a cost function to achieve the desired outcome. The project successfully achieved convergence, visualized in the plot file `cost_function.png`.
3. **Allan Deviation Calculation:** While the initial attempt to calculate the Allan deviation from the simulation data was unsuccessful, the project explored alternative methods for calculating it. This exploration involved simulating data points with specific assumptions (nominal transition frequency and sampling period) and implementing the calculation in the Python script `allan_code.py`.

### Future Work

The project acknowledges the use of idealized data and aims to improve upon the simulation in the future. The Allan deviation calculation serves as a valuable tool for further development.

### Code Files

* `optimal_ramsey.ipynb`: Jupyter Notebook containing the VQC simulation.
* `cost_function.png`: Plot visualization of the cost function convergence.
* `allan_code.py`: Python script for calculating the Allan deviation.

This project demonstrates the potential of using VQCs for Ramsey interferometry and lays the groundwork for further exploration and refinement of the simulation.
