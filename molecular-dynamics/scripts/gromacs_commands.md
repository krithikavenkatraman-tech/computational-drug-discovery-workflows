# Common GROMACS Commands

## Generate Topology

```bash
gmx pdb2gmx
```

## Define Simulation Box

```bash
gmx editconf
```

## Solvate System

```bash
gmx solvate
```

## Add Ions

```bash
gmx genion
```

## Energy Minimization

```bash
gmx grompp
gmx mdrun
```

## NVT Equilibration

```bash
gmx grompp
gmx mdrun
```

## NPT Equilibration

```bash
gmx grompp
gmx mdrun
```

## Production MD

```bash
gmx grompp
gmx mdrun
```

## Analysis

```bash
gmx rms
gmx rmsf
gmx gyrate
gmx sasa
gmx hbond
```