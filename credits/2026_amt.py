# 2025 Nonrefundable Credit for Prior Year Minimum Tax (AMT)
# Allows recovery of certain AMT paid in prior years.

def amt_credit_calc():
    """Calculates the amount of prior year AMT credit carryforward that can be used."""
    print("--- 2025 Prior Year AMT Credit ---")
    
    try:
        amt_credit_carryforward = float(input("AMT Carryforward: "))
        regular_tax_liability = float(input("Reg Tax Liab (Post Cr): "))
    except ValueError:
        print("Invalid input.")
        return

    # The credit is nonrefundable and limited to the amount of regular tax liability
    credit_used_this_year = min(amt_credit_carryforward, regular_tax_liability)
    
    remaining_carryforward = amt_credit_carryforward - credit_used_this_year

    print("---------------------------------")
    print("Credit Used This Year:", round(credit_used_this_year, 2))
    print("Remaining Carryforward:", round(remaining_carryforward, 2))

amt_credit_calc()