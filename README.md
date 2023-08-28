# Configuration Manual(For GitHub)

Note: My research powerpoint presentation is also in the root folder

## 1. Introduction

The purpose of this configuration manual is to guide users through the process of setting up the simulation environment and custom implementations used in the research project. It provides detailed instructions to ensure the successful execution of simulations, custom algorithm implementations, and data analysis.

## 2. System Requirements

Before proceeding with the installation, ensure that your system meets the following requirements:

- Operating System: Windows, MacOS, or Linux
- Java Runtime Environment (JRE) version 8 or higher
- Python version 3.7.x or higher
- Python package manager pip
- Visual Studio Code, Jupyter Notebook, or a compatible environment for running Python scripts

## 3. Installation and Setup

### 3.1 PureEdgeSim Simulator

The modified PureEdgeSim simulator called "myPureEdgeSim" is provided for our implementation on PureEdgeSim Simulator.

### 3.2 Installing Python and pip

1. Download and install Python from the [official website](https://www.python.org/downloads/).
2. Verify the installation by opening a terminal or command prompt and entering `python --version`.
3. Generally, pip is automatically installed if you are using Python downloaded from the official website.

## 4. Running Simulations and Analysis

### 4.1 Running the Customized Example

1. Open Eclipse IDE.
2. Go to `File` > `Open Projects from File System`.
3. Navigate to `PureEdgeSim` > `examples` > `Example8.java`.
4. Right-click on the project and select `Run As` > `Java Application`.
5. After completion, the output should display "Data file written".

### 4.2 Running Algorithm Implementations with mealpy

MEALPY is a Python library for advanced population-based meta-heuristic algorithms. Follow these steps:

1. Open the Python implementation of the selected algorithm (e.g., `copy_of_mealpy_algorithm.ipynb`).
2. Run the application using Visual Studio Code, Jupyter Notebook, or an alternative solution.
3. Press Enter in the console window of Eclipse to resume execution after the ipynb program finishes running.

### 4.3 Collecting and Analyzing Results

1. Results will be saved in the Example 8 outputs folder (`examples.Example8_output`) for the modified Example 8.
2. Each output is named with the current date, inside of which the results are dumped in an Excel file named "Sequential simulation."
3. Compile all algorithm results into a single CSV file.

#### 4.3.1 Analyzing the Results

To analyze the results, a Python script is used:

1. Open the Python program `Data Analysis` located in the root folder `myPureEdgeSim`.
2. Change `file_url` to `file_path` and assign it the path of the combined `results.csv`.
3. Run the program. It will analyze and print the results.
