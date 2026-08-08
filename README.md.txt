# Resistor Color Code Calculator

A simple GUI-based Resistor Color Code Calculator built using Python and Tkinter.

## Features

- Select resistor color bands using dropdown menus
- Calculates resistance value
- Displays tolerance
- Visually changes resistor bands according to selected colors
- Simple and user-friendly GUI

## Technologies Used

- Python
- Tkinter

## How It Works

The calculator uses the first two color bands to determine the significant digits, the third band as the multiplier, and the fourth band to determine tolerance.

For example:

Red - Violet - Yellow - Gold

27 × 10,000 = 270,000 Ω

Result:

270.0 kΩ ±5%

## How to Run

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL