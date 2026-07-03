from pathlib import Path

dlg_file = Path("dock.dlg")
output_file = Path("best_pose.pdbqt")

lines = dlg_file.read_text(errors="ignore").splitlines()

capture = False
atoms = []

for line in lines:
    if line.startswith("DOCKED: MODEL        1"):
        capture = True
        continue

    if capture and line.startswith("DOCKED: ENDMDL"):
        break

    if capture and (
        line.startswith("DOCKED: ATOM")
        or line.startswith("DOCKED: HETATM")
    ):
        atoms.append(line.replace("DOCKED: ", ""))

output_file.write_text("\n".join(atoms))

print("Done!")
print("Saved as:", output_file)