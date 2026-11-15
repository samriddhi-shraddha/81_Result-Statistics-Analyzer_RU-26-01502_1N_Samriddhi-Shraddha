"""Result Statistics Analyzer
Reads results.csv (RollNo, Marks) and shows statistics, pass percentage
and a distribution bar chart.
"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PASS_MARK = 40
FILE_NAME = "results.csv"


def load_data(path=FILE_NAME):
    """Read CSV, skip invalid marks with a warning. Returns a DataFrame or None."""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        return None
    except pd.errors.EmptyDataError:
        print("No valid marks found. Nothing to analyse.")
        return None

    if df.empty or "Marks" not in df.columns:
        print("No valid marks found. Nothing to analyse.")
        return None

    marks = pd.to_numeric(df["Marks"], errors="coerce")
    valid = marks.between(0, 100)  # NaN -> False
    for idx in df.index[~valid]:
        roll = df.loc[idx, "RollNo"]
        print(f"Warning: Row {roll} skipped - marks must be between 0 and 100.")

    clean = df[valid].copy()
    clean["Marks"] = marks[valid]
    if clean.empty:
        print("No valid marks found. Nothing to analyse.")
        return None
    return clean


def show_statistics(df):
    m = df["Marks"].to_numpy()
    mode = df["Marks"].mode().iloc[0]
    passed = int((m >= PASS_MARK).sum())
    print(f"Students: {len(m)}")
    print(f"Mean: {np.mean(m):.2f}")
    print(f"Median: {np.median(m):.2f}")
    print(f"Mode: {mode:.2f}")
    print(f"Highest: {m.max():.0f} | Lowest: {m.min():.0f}")
    print(f"Standard deviation: {np.std(m):.2f}")  # population std (ddof=0)
    print(f"Pass percentage: {passed / len(m) * 100:.2f}%")


def pass_distribution(df):
    m = df["Marks"]
    passed = int((m >= PASS_MARK).sum())
    failed = len(m) - passed
    print(f"Passed: {passed} | Failed: {failed} | "
          f"Pass percentage: {passed / len(m) * 100:.2f}%")

    bands = {
        "0-39": int(m.between(0, 39).sum()),
        "40-59": int(m.between(40, 59).sum()),
        "60-79": int(m.between(60, 79).sum()),
        "80-100": int(m.between(80, 100).sum()),
    }
    for band, count in bands.items():
        print(f"{band} : {count}")

    plt.figure(figsize=(6, 4))
    bars = plt.bar(bands.keys(), bands.values(), color="steelblue")
    plt.bar_label(bars)
    plt.title("Marks Distribution")
    plt.xlabel("Marks band")
    plt.ylabel("Number of students")
    plt.tight_layout()
    plt.show()


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else FILE_NAME
    df = load_data(path)
    if df is None:
        return

    while True:
        print("\n1. Show statistics")
        print("2. Pass percentage and distribution")
        print("3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            show_statistics(df)
        elif choice == "2":
            pass_distribution(df)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
