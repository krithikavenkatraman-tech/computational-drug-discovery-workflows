# Molecular Dynamics using GROMACS

## Overview

Molecular Dynamics (MD) simulation is a computational technique used to study the movement of atoms and molecules over time. Unlike molecular docking, which predicts a single binding pose, MD evaluates the structural stability and dynamic behavior of biomolecular systems under simulated physiological conditions.

This module documents the standard Molecular Dynamics workflow using GROMACS.

---

## Objectives

- Learn the Molecular Dynamics workflow
- Prepare a protein for simulation
- Understand equilibration and production MD
- Analyze simulation trajectories
- Perform structural stability analysis

---

## Workflow

1. Protein Preparation
2. Force Field Selection
3. Simulation Box Generation
4. Solvation
5. Ion Addition
6. Energy Minimization
7. NVT Equilibration
8. NPT Equilibration
9. Production Molecular Dynamics
10. Trajectory Analysis

---

## Workflow Description

### Protein Preparation
Prepare the protein by removing unnecessary molecules and ensuring the structure is suitable for simulation.

### Force Field
Select a force field (e.g., CHARMM, AMBER, GROMOS) that defines the mathematical parameters governing atomic interactions.

### Simulation Box
Generate a simulation box around the protein to provide space for molecular movement.

### Solvation
Fill the simulation box with water molecules to mimic the biological environment.

### Ion Addition
Add Na⁺ or Cl⁻ ions to neutralize the system and simulate physiological ionic conditions.

### Energy Minimization
Remove steric clashes and relax the system to a low-energy state.

### NVT Equilibration
Stabilize the system temperature while maintaining constant Number of atoms, Volume, and Temperature.

### NPT Equilibration
Stabilize pressure and density while maintaining constant Number of atoms, Pressure, and Temperature.

### Production MD
Run the actual molecular dynamics simulation and generate a trajectory describing atomic motion over time.

### Trajectory Analysis
Analyze the simulation using RMSD, RMSF, Radius of Gyration, SASA, and Hydrogen Bond calculations.

---

## Repository Structure

```text
molecular-dynamics/
├── analysis/
├── figures/
├── input-files/
├── mdp-files/
├── references/
├── scripts/
└── README.md
```

---

## Software Used

- GROMACS
- Discovery Studio Visualizer
- Visual Studio Code
- GitHub

---

## Learning Outcome

This repository documents the complete Molecular Dynamics workflow and serves as a reference for GROMACS-based biomolecular simulations.
