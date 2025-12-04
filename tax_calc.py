# tax_calc.py - Core Tax Liability Calculation
# ULTIMATE COMPATIBILITY VERSION: No file I/O (no open()), no external imports, 
# no f-strings, no .format(), and simplified nested lists for data storage to prevent memory overflow.

# --- 1. Embedded Raw Data ---
# Data stored as simple nested lists to reduce memory overhead during script loading.
# The data is based on the 2025 tax brackets you provided.

RAW_DEDUCTIONS = [
    ["SINGLE", 14600.00],
    ["MARRIED_JOINT", 29200.00],
    ["HEAD_OF_HOUSEHOLD", 21900.00]
]

# FORMAT: [Status, Rate, Max_Threshold, Base_Tax_Liability]
RAW_BRACKETS = [
    ["SINGLE", 0.10, 11600.00, 0.00],
    ["SINGLE", 0.12, 47150.00, 1160.00],
    ["SINGLE", 0.22, 100000.00, 6415.50],
    ["SINGLE", 0.24, 191950.00, 17892.50],
    ["SINGLE", 0.32, 243975.00, 40062.50],
    ["SINGLE", 0.35, 609350.00, 56066.50],

    ["MARRIED_JOINT", 0.10, 23200.00, 0.00],
    ["MARRIED_JOINT", 0.12, 94300.00, 2320.00],
    ["MARRIED_JOINT", 0.22, 200000.00, 12830.00],
    ["MARRIED_JOINT", 0.24, 383900.00, 35785.00],
    ["MARRIED_JOINT", 0.32, 487950.00, 80125.00],
    ["MARRIED_JOINT", 0.35, 731925.00, 112133.00],
    
    # Head of Household data included for completeness
    ["HEAD_OF_HOUSEHOLD", 0.10, 16550.00, 0.00],
    ["HEAD_OF_HOUSEHOLD", 0.12, 65500.00, 1655.00],
    ["HEAD_OF_HOUSEHOLD", 0.22, 100000.00, 8099.00],
    ["HEAD_OF_HOUSEHOLD", 0.24, 191950.00, 17892.50],
    ["HEAD_OF_HOUSEHOLD", 0.32, 243975.00, 40062.50],
    ["HEAD_OF_HOUSEHOLD", 0.35, 609350.00, 56066.50]
]

# --- 2. Manual Data Parsing ---

def parse_raw_data():
    """Converts the simple lists into structured dictionaries."""
    deductions = {}
    brackets = {}

    # Parse Deductions
    for entry in RAW_DEDUCTIONS:
        status = entry[0]
        amount = entry[1]
        deductions[status] = amount

    # Parse Brackets
    for entry in RAW_BRACKETS:
        status = entry[0]
        rate = entry[1]
        max_limit = entry[2]
        base_tax = entry[3]

        bracket_entry = {
            "rate": rate,
            "max": max_limit,
            "base_tax": base_tax
        }
        
        if status not in brackets:
            brackets[status] = []
        
        brackets[status].append(bracket_entry)
        
    return deductions, brackets

# Global variables for the calculation
DEDUCTIONS, BRACKETS = parse_raw_data()

# --- 3. Core Calculation Function ---

def calculate_tax_liability(agi, status):
    """Calculates gross tax liability based on AGI and filing status."""
    
    # Ensure the status is valid
    if status not in BRACKETS or status not in DEDUCTIONS:
        print("Error: Invalid status or data missing for: " + status)
        return 0.00, 0.00

    # 1. Determine Taxable Income (TI)
    standard_deduction = DEDUCTIONS.get(status.upper(), 0.00)
    taxable_income = max(0, agi - standard_deduction)

    gross_liability = 0.00
    bracket_list = BRACKETS[status.upper()]

    # 2. Iterate through Brackets
    for bracket in bracket_list:
        rate = bracket['rate']
        max_limit = bracket['max']
        base_tax = bracket['base_tax']
        
        # Calculate the starting point of the current bracket
        previous_max = 0.00
        current_index = bracket_list.index(bracket)
        
        if current_index > 0:
            previous_max = bracket_list[current_index - 1]['max']
        
        # If TI falls into this bracket
        if taxable_income <= max_limit:
            taxable_at_rate = taxable_income - previous_max
            gross_liability = base_tax + (taxable_at_rate * rate)
            break
        
        # If this is the last bracket and TI exceeds its max, apply the rate to the remainder
        if current_index == len(bracket_list) - 1:
            taxable_at_rate = taxable_income - previous_max
            gross_liability = base_tax + (taxable_at_rate * rate)
            break
            
    return round(gross_liability, 2), round(taxable_income, 2)


# --- 4. Main Program Execution ---

def run_tax_calc():
    """Main execution block for user interaction."""
    print("--- 2025 TAX CALCULATOR ---")
    
    # Simple Input
    try:
        agi_input = input("Enter AGI: ")
        agi = float(agi_input)
    except ValueError:
        print("Invalid AGI entered. Please use numbers.")
        return
        
    status_input = input("Enter Status (SINGLE/MARRIED_JOINT/HEAD_OF_HOUSEHOLD): ").upper()
    
    # Check if data was parsed correctly (should not fail now)
    if not BRACKETS:
        print("Fatal Error: Internal data parsing failed.")
        return

    # Check if the entered status is valid
    valid_statuses = list(DEDUCTIONS.keys())
    if status_input not in valid_statuses:
        print("Invalid filing status. Use one of: " + ', '.join(valid_statuses))
        return

    liability, ti = calculate_tax_liability(agi, status_input)

    # Output using simple string concatenation
    print("\n--- RESULTS (" + status_input + ") ---") 
    print("Standard Deduction Used: $" + str(round(DEDUCTIONS.get(status_input, 0.00), 2)))
    print("Taxable Income: $" + str(round(ti, 2)))
    print("Gross Tax Liability: $" + str(round(liability, 2)))


# Executes the main function immediately.
run_tax_calc()