import re
from pathlib import Path

def parse_dlg(file_path):
    text = Path(file_path).read_text(errors="ignore")

    results = {}

    # Best binding energy
    energy = re.search(
        r"DOCKED: USER\s+Estimated Free Energy of Binding\s+=\s+(-?\d+\.\d+)",
        text,
    )

    # Estimated Ki
    ki = re.search(
        r"DOCKED: USER\s+Estimated Inhibition Constant,\s+Ki\s+=\s+([\d\.]+)\s+([a-zA-Z]+)",
        text,
    )

    # Docking Run
    run = re.search(
        r"DOCKED:\s+MODEL\s+(\d+)",
        text,
    )

    if energy:
        results["Binding Energy (kcal/mol)"] = energy.group(1)

    if ki:
        results["Estimated Ki"] = f"{ki.group(1)} {ki.group(2)}"

    if run:
        results["Best Model"] = run.group(1)

    return results


if __name__ == "__main__":

    dlg_file = "dock.dlg"

    data = parse_dlg(dlg_file)

    print("=" * 40)
    print(" AutoDock4 Docking Summary")
    print("=" * 40)

    for key, value in data.items():
        print(f"{key:<30}: {value}")
