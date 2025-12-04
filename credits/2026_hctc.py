# 2025 Health Coverage Tax Credit (HCTC)
# For certain trade-affected workers/retirees.
# Credit: 72.5% of qualified health insurance premiums paid.

def hctc_calc():
    """Calculates the estimated 2025 HCTC."""
    print("--- 2025 Health Coverage Tax Credit ---")
    
    try:
        qual_premiums_paid = float(input("Qual. Premiums Paid: "))
    except ValueError:
        print("Invalid input.")
        return

    credit_percentage = 0.725
    
    # Calculation
    credit_amount = qual_premiums_paid * credit_percentage
    
    print("---------------------------------")
    print("Qualifying Percentage: 72.5%")
    print("Estimated 2025 HCTC (Nonrefundable):")
    print("$", round(credit_amount, 2))

hctc_calc()