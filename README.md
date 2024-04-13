# Quantum Computing for Atomic Clock Design

## Overview

This repository documents our exploration of quantum computing applications in improving the design and precision of atomic clocks. The project aimed to leverage quantum algorithms like Variational Quantum Eigensolvers (VQE) and Quantum Phase Estimation (QPE) to optimize clock transitions and measure phase or frequency shifts.

## QRISE 2024 Team: MaybeACat

### Team Members:
- Ankon Dey Animesh
- Ganisetti Gunadham
- Prince Odoi Asare
- Tulsi Chaudhari
- Shivani Mayekar

## Objectives

- Understand quantum algorithms (VQE, QPE) and their potential impact on atomic clock design.
- Implement prototypes using VQE and QPE algorithms to optimize clock transitions and measure phase or frequency shifts.
- Explore simulated experiments with programmable quantum sensors to enhance clock precision.

## Approach

- **Task Allocation**: Tasks were divided among the team members for self-exploration and understanding of quantum concepts.
- **Collaborative Learning**: Regular virtual meetings were held to share progress, insights, and challenges encountered during the project.

## Implementation

- **Prototypes**: Implemented prototypes using VQE and QPE algorithms to optimize clock transitions and measure phase or frequency shifts.
- **Simulations**: Conducted simulated experiments with programmable quantum sensors to explore clock precision enhancement techniques.
- **Optimization**: Utilized scipy library and its `minimize` function as a substitute for the COBYLA optimizer to optimize the quantum circuits.

## Implemented Prototypes:

- **Quantum Circuit Code**: The code for the implemented quantum circuit can be found [here](https://github.com/ShivaniDM/qrise2024-infleqtion-challenge/blob/main/circuit.py).
- **Circuit Results**: The results of the quantum circuit simulations are visualized [here](https://github.com/ShivaniDM/qrise2024-infleqtion-challenge/blob/main/circuit_result.png).

## Challenges and Solutions

- **Version Compatibility**: Faced issues with different versions of Qiskit. Resolved by debugging and optimizing code for compatibility.
- **Integration Complexity**: Challenges integrating error correction and feedback control systems with quantum algorithms. Addressed by conducting in-depth research and seeking assistance from mentors.

## Results and Limitations

- **Successes**: Successfully implemented solutions and gained valuable insights into quantum computing applications for atomic clock design.
- **Limitations**: Interpretability challenges with VQE and integration complexities remain unresolved.
- 

## Future Directions

- **Version Compatibility**: Address version compatibility issues with Qiskit and explore alternative optimization algorithms.
- **Integration Optimization**: Investigate synergies with machine learning techniques for improved integration of error correction and feedback control systems.
- we will be using scipy optimiser which is compatible with latest version of qiskit to implement VQE algorithm on our circuit.
- Scipy optimiser reference.py
- this file references implementation of VQE algorithm using scipy optimiser method.

## Pros and Cons of Quantum Algorithms

- **VQE**: Offers enhanced sensitivity and immunity to noise but may have interpretability challenges.
- **QPE**: Enables precise measurement of phase or frequency shifts but may require complex circuit design.

## Potential Applications

- **Fault-Tolerant Systems**: Explore applications of fault-tolerant quantum computing in enhancing clock stability and accuracy.
- **Machine Learning Integration**: Investigate the integration of machine learning techniques to optimize clock control and performance.

## Conclusion

While concrete results were not achieved due to certain challenges, the project has provided valuable insights and paved the way for future exploration and improvement in atomic clock design using quantum computing techniques.
