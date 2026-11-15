# Result Statistics Analyzer

**PS No. 81** | Rungta International Skills University
School of Computer Science and Engineering - B.Tech CSE, First Semester

A Python 3 console program that reads student marks from `results.csv` and shows
statistics, pass percentage and a marks distribution bar chart.

## Features
- Reads `results.csv` (`RollNo`, `Marks`) using **Pandas**
- Handles a missing file and a file with only the header row
- Skips marks outside 0-100 (or non-numeric) with a warning
- Calculates mean, median, mode, highest, lowest and standard deviation (`np.std`) using **NumPy** / Pandas
- Pass percentage (pass mark = 40)
- Student count in bands **0-39, 40-59, 60-79, 80-100** with a **Matplotlib** bar chart
- Simple console menu

## Concepts used
Pandas, NumPy, Visualization, Statistics

## Project structure
```
repository/
├── Codebase/
│   ├── README.md
│   ├── requirements.txt
│   ├── result_analyzer.py
│   └── results.csv
└── Testcases/             # screenshots
```

## Installation
```bash
git clone https://github.com/samriddhi-shraddha/81_Result-Statistics-Analyzer_RU-26-01502_1N_Samriddhi-Shraddha.git
cd 81_Result-Statistics-Analyzer_RU-26-01502_1N_Samriddhi-Shraddha/Codebase
pip install -r requirements.txt
```

## Usage
```bash
python result_analyzer.py              # uses results.csv
python result_analyzer.py my_file.csv  # optional: use another CSV
```

Menu:
```
1. Show statistics
2. Pass percentage and distribution
3. Exit
```

### CSV format
```
RollNo,Marks
1,45
2,58
...
```

## Sample output (results.csv)
Option 1:
```
Students: 10
Mean: 70.20
Median: 72.00
Mode: 72.00
Highest: 95 | Lowest: 38
Standard deviation: 17.78
Pass percentage: 90.00%
```
Option 2:
```
Passed: 9 | Failed: 1 | Pass percentage: 90.00%
0-39 : 1
40-59 : 2
60-79 : 3
80-100 : 4
```
![Marks distribution](../Testcases/distribution_chart.png)

> Note: the sample marks add up to 702, so the program gives mean **70.20** and
> standard deviation **17.78** (population, `np.std`). The problem sheet lists 70.00 and 17.92.

## Author
Samriddhi Shraddha - ERP01502
