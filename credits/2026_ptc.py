# 2025 Premium Tax Credit (PTC) - Highly Simplified Estimate
# This script simulates the cost contribution rule.

def ptc_calc():
    """Provides a highly simplified PTC estimate."""
    print("--- 2025 Premium Tax Credit Simplified ---")

    try:
        household_income = float(input("Household Income: "))
        fpl = float(input("FPL % (e.g., 150): "))
        annual_premium = float(input("2nd Lowest Silver Prem: "))
    except ValueError:
        print("Invalid input.")
        return

    # Determine Maximum Required Contribution Rate (Enhanced 2025 Rates)
    max_rate = 0.0
    if fpl <= 150.0:
        max_rate = 0.0
    elif fpl <= 200.0:
        max_rate = 0.02 * (fpl - 150.0) / 50.0
    elif fpl <= 400.0:
        max_rate = 0.02 + (0.065 * (fpl - 200.0) / 200.0)
    else:
        max_rate = 0.085

    max_contrib = household_income * max_rate
    
    # Credit is the excess of the premium over the maximum contribution
    credit_amount = max(0.0, annual_premium - max_contrib)

    print("---------------------------------")
    print("Max Contrib. Rate:", round(max_rate * 100, 2), "%")
    print("Max Annual Contrib.:", round(max_contrib, 2))
    print("Estimated 2025 PTC (Refundable):")
    print("$", round(credit_amount, 2))

ptc_calc()