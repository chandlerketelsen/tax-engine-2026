# tax_calc.py - Core Tax Liability Calculation
# Uses raw file I/O (tax_raw_data.txt) to avoid memory crashes from large dictionary literals.
# TI-84 compatible: uses only simple string and float operations.
# NOTE: Only the 10%, 12%, 22%, and 24% tax brackets are included to save memory.

# --- 1. Data Loading Function (Reads RAW text file) ---

def load_tax_data(filename="tax_raw_data.txt"):
    """
    Reads delimited tax data from a text file and builds the DEDUCTIONS and BRACKETS dictionaries.
    Uses simple file I/O to minimize memory overhead during loading.
    """
    deductions = {}
    brackets = {}

    try:
        # Use simple file open which is supported
        f = open(filename, 'r')
        
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if line.startswith('#') or not line:
                continue
            
            # Split the line by comma and clean up spaces
            parts = [p.strip() for p in line.split(',')]
            
            data_type = parts[0]
            status = parts[1]
            
            if data_type == "DEDUCTION":
                # DEDUCTION, STATUS, AMOUNT
                deductions[status] = float(parts[2])
            
            elif data_type == "BRACKET":
                # BRACKET, STATUS, RATE, MAX_THRESHOLD, BASE_TAX_LIABILITY
                bracket_entry = {
                    "rate": float(parts[2]),
                    "max": float(parts[3]),
                    "base_tax": float(parts[4])
                }
                
                if status not in brackets:
                    brackets[status] = []
                
                brackets[status].append(bracket_entry)
        
        f.close()

    except FileNotFoundError:
        print("Error: " + filename + " not found. Cannot calculate tax.")
        return {}, {}
    except ValueError:
        print("Error: Data in " + filename + " is corrupted.")
        return {}, {}
    # Use generic exception catch for other errors (like memory/read errors)
    except:
        print("Error: Failed to process data file.")
        return {}, {}

    return deductions, brackets


# Load the data immediately using the memory-efficient function
DEDUCTIONS, BRACKETS = load_tax_data()


# --- 2. Core Calculation Function ---

def calculate_tax_liability(agi, status):
    """Calculates gross tax liability based on AGI and filing status."""
    
    # Ensure the status is valid and data exists
    if status not in BRACKETS or status not in DEDUCTIONS:
        print("Error: Invalid status or data missing for: " + status)
        return 0.00, 0.00

    # 1. Determine Taxable Income (TI)
    standard_deduction = DEDUCTIONS.get(status.upper(), 0.00)
    taxable_income = max(0, agi - standard_deduction)

    gross_liability = 0.00
    
    # 2. Iterate through Brackets
    bracket_list = BRACKETS[status.upper()]

    for bracket in bracket_list:
        rate = bracket['rate']
        max_limit = bracket['max']
        base_tax = bracket['base_tax']
        
        # Calculate the starting point of the current bracket
        previous_max = 0.00
        # NOTE: Using bracket_list.index(bracket) is generally slow, but necessary 
        # for these highly simplified Python environments.
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
            
    # Handle case where TI is extremely high (should be caught by the last bracket logic)
    if gross_liability == 0.00 and taxable_income > 0.00:
        # This occurs if TI exceeds the final bracket's threshold (e.g. > $191,950 for SINGLE)
        # The logic above should handle this, but this is a fallback debug indicator.
        if taxable_income > bracket_list[-1]['max']:
             print("Warning: TI exceeds 24% threshold.")


    return round(gross_liability, 2), round(taxable_income, 2)


# --- 3. Main Program Execution ---

def run_tax_calc():
    """Main execution block for user interaction."""
    print("--- 2025 TAX CALCULATOR (24% Max) ---")
    
    # Simple Input
    try:
        agi_input = input("Enter AGI: ")
        agi = float(agi_input)
    except ValueError:
        print("Invalid AGI entered. Please use numbers.")
        return
        
    status_input = input("Enter Status (SINGLE/MARRIED_JOINT/HOH): ").upper()
    
    # Check if the load failed silently
    if not BRACKETS:
        print("Cannot run calculation due to failed data load.")
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