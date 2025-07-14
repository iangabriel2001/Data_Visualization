# 📊 Disk Read Speed Visualization

A simple data visualization project in Python using `matplotlib` (and optionally `seaborn`) to show disk read speeds for different image files.

---

## 📂 Project Structure

├── disk_plot.py # Python script for creating the bar chart
├── DISK CATDOG - Sheet1.csv # Dataset containing image numbers and disk speeds
└── README.md # Project documentation


## 📈 What It Does

- Reads disk read speed data from a `.csv` file
- Creates a bar chart showing the speed per image
- Uses Python's `matplotlib` for visualization
- Clean and readable layout

---

## 🛠 Requirements

Install the required libraries (if not already installed):

```bash
pip install matplotlib pandas

📄 Example CSV Format

| Image # | Disk Read Speed |
| ------- | --------------- |
| 1       | 145             |
| 2       | 162             |
| 3       | 139             |
