# tax_calc.py - Core Tax Liability Calculation
# This script loads all complex data from 'tax_data.py' via standard import.
# IT USES ONLY SIMPLE PYTHON SYNTAX (NO F-STRINGS OR .FORMAT()) FOR TI-84 COMPATIBILITY.

# --- 1. Data Loading ---
# This imports the TAX_DATA dictionary defined in the tax_data.py file
# Note: Both files must be in the same location on the calculator.
import tax_data 

TAX_DATA = tax_data.TAX_DATA
DEDUCTIONS = TAX_DATA.get("DEDUCTIONS", {})
BRACKETS = TAX_DATA.get("BRACKETS", {})

# --- 2. Core Calculation Function ---

def calculate_tax_liability(agi, status):
    """Calculates gross tax liability based on AGI and filing status."""
    
    # Ensure the status is valid and data exists
    if status not in BRACKETS or status not in DEDUCTIONS:
        # Using string concatenation for maximum compatibility
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
        if bracket_list.index(bracket) > 0:
            previous_max = bracket_list[bracket_list.index(bracket) - 1]['max']
        
        # If TI falls within this bracket (or is the last bracket)
        if taxable_income > previous_max:
            if taxable_income <= max_limit:
                # TI falls into this bracket
                taxable_at_rate = taxable_income - previous_max
                gross_liability = base_tax + (taxable_at_rate * rate)
                break
            elif max_limit == 999999999.0:
                # Handle the final, uncapped bracket (if using a placeholder max)
                taxable_at_rate = taxable_income - previous_max
                gross_liability = base_tax + (taxable_at_rate * rate)
                break
            else:
                # TI exceeds this bracket, move to next
                pass # The loop continues

    return round(gross_liability, 2), round(taxable_income, 2)


# --- 3. Main Program Execution ---

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
        
    status_input = input("Enter Status (SINGLE/MARRIED_JOINT/HOH): ").upper()
    
    if not BRACKETS:
        print("Cannot run calculation due to missing tax data.")
        return

    # Check if the entered status is valid
    valid_statuses = list(DEDUCTIONS.keys())
    if status_input not in valid_statuses:
        # Use simple concatenation to guarantee no syntax failure
        print("Invalid filing status. Use one of: " + ', '.join(valid_statuses))
        return

    liability, ti = calculate_tax_liability(agi, status_input)

    # Line 86 fix: Switched to simple string concatenation
    print("\n--- RESULTS (" + status_input + ") ---") 
    
    # Switched to C-style formatting or concatenation for maximum compatibility
    print("Standard Deduction Used: $" + str(round(DEDUCTIONS.get(status_input, 0.00), 2)))
    print("Taxable Income: $" + str(round(ti, 2)))
    print("Gross Tax Liability: $" + str(round(liability, 2)))


run_tax_calc()