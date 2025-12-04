# 2025 Credit for the Elderly or Disabled - Simplified
# Based on Initial Base Amount reduced by non-taxable income (SS, pensions)

def elderly_calc():
    """Calculates a simplified estimate of the 2025 Elderly/Disabled Credit."""
    print("--- 2025 Credit for Elderly/Disabled ---")
    print("--- SIMPLIFIED ESTIMATE ---")
    
    try:
        filing_status = input("Status (S/MFJ-1/MFJ-2): ").upper()
        ss_income = float(input("SS/Pensions Rec'd: "))
    except ValueError:
        print("Invalid input.")
        return

    # Initial Base Amounts (Approximate 2025 values)
    if filing_status in ("S", "HOH"): # Single / Head of Household
        initial_amount = 5000.0
    elif filing_status == "MFJ-1": # Married Filing Jointly (one spouse qualifies)
        initial_amount = 5000.0
    elif filing_status == "MFJ-2": # Married Filing Jointly (both qualify)
        initial_amount = 7500.0
    else:
        print("Invalid filing status entered.")
        return

    # Reduction: Initial Amount is reduced by non-taxable SS/Pensions
    reduction = ss_income
    
    # Calculate final credit amount (max 15% of the result)
    credit_base = max(0.0, initial_amount - reduction)
    
    estimated_credit = credit_base * 0.15
    
    print("---------------------------------")
    print("Credit Base Amount:", round(credit_base, 2))
    print("Estimated 2025 Credit (Max 15%):")
    print("$", round(estimated_credit, 2))

elderly_calc()