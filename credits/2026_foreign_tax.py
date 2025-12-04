# 2025 Foreign Tax Credit (FTC) - Simplified
# Limit = (Foreign Taxable Income / Total Taxable Income) * U.S. Tax

def ftc_calc():
    """Calculates a basic estimate of the 2025 Foreign Tax Credit limit."""
    print("--- 2025 Foreign Tax Credit Limit ---")
    
    try:
        foreign_tax_paid = float(input("Foreign Tax Paid: "))
        foreign_taxable_income = float(input("Foreign Taxable Inc: "))
        total_taxable_income = float(input("Total US Taxable Inc: "))
        us_tax_liability = float(input("US Tax Liab (Pre-Cr): "))
    except ValueError:
        print("Invalid input.")
        return

    if total_taxable_income <= 0:
        print("Total Taxable Income must be positive.")
        return

    # Limit Calculation: The credit cannot exceed the U.S. tax on the foreign income.
    ftc_limit = (foreign_taxable_income / total_taxable_income) * us_tax_liability

    # Final credit is the lesser of the foreign tax paid or the calculated limit
    credit_amount = min(foreign_tax_paid, ftc_limit)

    print("---------------------------------")
    print("Calculated FTC Limit:", round(ftc_limit, 2))
    print("Estimated 2025 FTC (Nonrefundable):")
    print("$", round(credit_amount, 2))

ftc_calc()