# Docking Utility Scripts

This folder contains helper scripts developed to automate analysis of AutoDock4 docking experiments.

## Scripts

### extract_best_pose.py

Extracts the coordinates of the best-scoring docking pose from an AutoDock4 `.dlg` file and saves it as a `.pdbqt` structure.

---

### parse_docking_results.py

Reads an AutoDock4 docking log (`.dlg`) and extracts important docking statistics including:

- Best binding energy
- Estimated inhibition constant (Ki)
- Best docking model

These scripts simplify downstream analysis and improve workflow reproducibility.
