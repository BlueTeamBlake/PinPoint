# Pinpoint v1.0

## Overview

**Pinpoint** is a Python tool designed to parse and analyze hex dumps of files, displaying human-readable ASCII representations. It helps you analyze binary files by filtering out the noise that we as humans can't understand. Pinpoint makes it easy to distinguish between printable and non-printable characters, improving the readability of hex dumps.

How it works:
Takes non-printable characters and re-assigns them the prefix 0x##
Takes printable ASCII characters and re-assigns them the prefix 1x##


**Features:**
- Converts raw file data into a human-readable hex format.
- Classifies bytes into categories like printable ASCII, extended characters, and control characters.
- Option to remove non-printable characters from the output for cleaner analysis.
- Supports reading from any file format (images, text files, etc.) to visualize the raw byte content.

## Requirements

- Python 3.x
- Required Python packages: `argparse`

## Installation

1. Clone or download the repository:
   ```bash
   git clone https://github.com/BlueTeamBlake/PinPoint.git

2. Naviagate to the project directory.

3. Install any dependencies if needed

## Usage

1. Run the program:
```bash
python pinpoint.py
```
2. Follow the prompts:
Please enter the input file (path): C:\Users\You\Desktop\sample.txt
Please enter the output file (path): output.txt (will save in current Dir if not specified)
Do you want to remove non-printable characters? (Y/N): Y

Once the program is ran, it will create the output file that can be viewed for analysis. 
   

