# Homology Modeling

> Comparative protein structure prediction using template-based modeling for computational drug discovery.

---

# Overview

Homology modeling is a computational technique used to predict the three-dimensional structure of a protein based on experimentally resolved homologous structures.

This workflow demonstrates the process of identifying suitable templates, generating structural models using **MODELLER**, validating predicted structures, and preparing them for downstream computational analyses such as molecular docking.

---

# Workflow

<p align="center">
<img src="figures/02_homology_model_workflow.png" width="650">
</p>

---

# Protein Structure

The predicted RIPK2 protein structure generated through homology modeling.

<p align="center">
<img src="figures/01_ripk2_structure.png" width="450">
</p>

---

# Template Selection

Suitable structural templates were identified through sequence similarity searches against the Protein Data Bank (PDB).

<p align="center">
<img src="figures/03_sequence_alignment.png" width="900">
</p>

---

# Structural Validation

## Ramachandran Plot

The stereochemical quality of the predicted model was evaluated using PROCHECK.

<p align="center">
<img src="figures/04_ramachandran_plot.png" width="500">
</p>

---

## SAVES Validation

The final model was further assessed using the SAVES server to evaluate structural quality.

<p align="center">
<img src="figures/05_model_validation.png" width="650">
</p>

---

# Software Used

- MODELLER
- BLAST
- Protein Data Bank (PDB)
- Discovery Studio Visualizer
- PROCHECK
- SAVES v6.1

---

# Learning Outcomes

- Comparative protein modeling
- Template identification
- Sequence alignment
- Structural validation
- Model quality assessment
- Preparation of protein structures for molecular docking

---

# Applications

- Structure-based drug discovery
- Molecular docking
- Protein engineering
- Functional annotation
- Computational structural biology
