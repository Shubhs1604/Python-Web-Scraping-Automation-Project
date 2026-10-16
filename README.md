# Flipkart Laptop Web Scraping Automation

A Python-based web scraping automation project that extracts laptop product information from Flipkart using Selenium and processes the collected data with Pandas. The extracted data is exported to a CSV file for further analysis.

## Project Overview

This project demonstrates practical skills in Python programming, browser automation, web scraping, data processing, and CSV file handling.

The script automates the process of opening Flipkart, searching for laptop products, collecting available product information, and saving the results in a structured format.

## Features

- **Automated browser interaction:** Uses Selenium to automate web browsing.
- **Product data extraction:** Collects available laptop product details from Flipkart.
- **Data processing:** Uses Pandas to organize the extracted information.
- **CSV export:** Saves the collected data in `flipkart_laptops.csv`.
- **Reusable Python scripts:** Includes the main scraping script and a Selenium test script.

## Technologies Used

- Python
- Selenium
- Pandas
- Web Scraping
- Browser Automation
- CSV

## Project Structure

```text
Python-Web-Scraping-Automation-Project/
│
├── flipkart_search.py       # Main web scraping script
├── test_selenium.py         # Selenium testing script
├── requirements.txt         # Python dependencies
├── flipkart_laptops.csv     # Scraped laptop data
├── .gitignore               # Excluded files and folders
└── README.md                # Project documentation
```

## Prerequisites

- Python 3.10 or a compatible Python version
- Google Chrome browser
- Git (optional, for cloning the repository)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Shubhs1604/Python-Web-Scraping-Automation-Project.git
```

### 2. Navigate to the project directory

```bash
cd Python-Web-Scraping-Automation-Project
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the scraping script

```bash
python flipkart_search.py
```

To run the Selenium test script:

```bash
python test_selenium.py
```

## Output

The scraped laptop product data is stored in:

`flipkart_laptops.csv`

The CSV file can be opened using Microsoft Excel, Google Sheets, or Pandas for further analysis.

## Skills Demonstrated

- Python scripting
- Selenium browser automation
- Web scraping and data extraction
- Pandas data processing
- CSV file generation
- Dependency management
- Git and GitHub version control

## Important Notes

- Website layouts and
