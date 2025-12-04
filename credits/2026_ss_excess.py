# 2025 Credit for Excess Social Security Tax Withheld
# Occurs when wages from multiple employers exceed the Social Security Wage Base Limit.

def ss_excess_calc():
    """Calculates the estimated 2025 excess SS tax withheld."""
    print("--- 2025 Excess SS Tax Credit ---")
    
    try:
        total_ss_wages = float(input("Total SS Wages: "))
        ss_tax_paid = float(input("Total SS Tax Withheld: "))
    except ValueError:
        print("Invalid input.")
        return

    # Estimated 2025 Social Security Wage Base Limit
    wage_base_limit = 170000.0 
    ss_tax_rate = 0.062

    # Maximum SS tax that should have been paid by employee
    max_ss_tax = wage_base_limit * ss_tax_rate
    
    # Taxpayer must have paid in excess of the max tax limit
    excess_tax = max(0.0, ss_tax_paid - max_ss_tax)
    
    print("---------------------------------")
    print("SS Wage Base Limit:", round(wage_base_limit, 2))
    print("Max SS Tax Liab.:", round(max_ss_tax, 2))
    
    if total_ss_wages > wage_base_limit:
        print("Wages exceeded limit.")
    else:
        print("Wages did not exceed limit.")

    print("Estimated 2025 Credit:")
    print("$", round(excess_tax, 2))

ss_excess_calc()