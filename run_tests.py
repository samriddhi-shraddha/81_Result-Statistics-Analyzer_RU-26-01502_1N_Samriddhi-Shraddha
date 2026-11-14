"""Runs the 4 test cases from the problem sheet using the CSV files in test_data/.

For Test Case 4 the bar chart opens in a window. Close the chart window to
continue with the remaining output.
"""
import subprocess
import sys

CASES = [
    ("Test Case 1: Normal Input", "test_data/case1_normal.csv", "1\n3\n"),
    ("Test Case 2: Boundary / Minimum Input", "test_data/case2_single_row.csv", "1\n3\n"),
    ("Test Case 3(a): Marks outside 0-100", "test_data/case3a_invalid_marks.csv", "1\n3\n"),
    ("Test Case 3(b): Header only", "test_data/case3b_header_only.csv", ""),
    ("Test Case 4: Pass % and distribution", "test_data/case4_distribution.csv", "2\n3\n"),
]

for title, csv, keys in CASES:
    print("=" * 60)
    print(title)
    print("=" * 60, flush=True)
    # Output is not captured, so it prints live and the chart window can open.
    subprocess.run([sys.executable, "result_analyzer.py", csv], input=keys, text=True)
    print(flush=True)