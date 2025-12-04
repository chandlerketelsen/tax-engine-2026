# 2025 U.S. Tax Rules Engine (TI-84 Python Edition)

## Project Overview

This repository contains a collection of Python scripts designed to accurately estimate 2025 U.S. Federal Tax liability and specific tax credits, tailored specifically for the Python interpreter on the Texas Instruments TI-84 Plus CE graphing calculator.

The structure allows users to easily navigate to the desired tax law calculation (e.g., Child Tax Credit, Tax Brackets) and read the rules directly within the Python code, making the tax code transparent and accessible based on official 2025 figures.

## Repository Structure (TI-84 Compatible)

Since the TI-84 Python interpreter does not support external file imports (like JSON) or standard library features, all rules, thresholds, and rates are hardcoded directly into the script files.tax_calc.py: Core Tax Liability. Calculates Adjusted Gross Income (AGI), Taxable Income (using Standard Deduction), and Gross Tax Liability using the progressive bracket system./credits: Contains 20 individual scripts for calculating specific, complex tax credits, including phase-outs and limits.

## Execution on TI-84 CE

Transfer the desired .py file to the calculator (e.g., using TI-Connect CE). Run the script from the Python App menu. Enter the requested inputs (e.g., income, status, expenses). The script will output the estimated credit or gross tax liability. Key Calculation Mappings

To ensure short input prompts:
**Filing Status**: S=Single, M=MFJ (Married Filing Jointly), H=HOH (Head of Household), F=MFS (Married Filing Separately).
**AGI**: Adjusted Gross Income.MAGI: Modified Adjusted Gross Income.