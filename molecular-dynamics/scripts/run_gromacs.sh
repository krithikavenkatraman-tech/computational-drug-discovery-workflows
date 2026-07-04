#!/bin/bash

echo "Generate topology"
gmx pdb2gmx

echo "Create simulation box"
gmx editconf

echo "Solvate system"
gmx solvate

echo "Add ions"
gmx genion

echo "Energy minimization"
gmx grompp
gmx mdrun

echo "NVT equilibration"
gmx grompp
gmx mdrun

echo "NPT equilibration"
gmx grompp
gmx mdrun

echo "Production Molecular Dynamics"
gmx grompp
gmx mdrun

echo "Simulation Completed"