# 2025 Saver's Credit
# Credit Rate: 50%, 20%, 10% (max $2,000 for MFJ)
# Max contribution used for calculation: $2,000 (other) / $4,000 (MFJ)

def savers_calc():
    """Calculates the estimated 2025 Saver's Credit."""
    print("--- 2025 Saver's Credit ---")
    
    try:
        agi = float(input("Enter AGI: "))
        contribution = float(input("Contributed: "))
        status = input("Status (MFJ/HOH/OTH): ").upper()
    except ValueError:
        print("Invalid input.")
        return

    # 1. Determine Credit Rate (2025 AGI Limits)
    rate = 0.0
    max_contrib_credit = 2000.0  # Default for single/other filers

    if status == "MFJ":
        max_contrib_credit = 4000.0
        if agi <= 47500: rate = 0.50
        elif agi <= 51000: rate = 0.20
        elif agi <= 79000: rate = 0.10
    elif status == "HOH":
        if agi <= 35625: rate = 0.50
        elif agi <= 38250: rate = 0.20
        elif agi <= 59250: rate = 0.10
    elif status == "OTHER":
        if agi <= 23750: rate = 0.50
        elif agi <= 25500: rate = 0.20
        elif agi <= 39500: rate = 0.10
    
    if rate == 0.0:
        print("AGI is above the max limit.")

    # 2. Calculate credit
    capped_contribution = min(contribution, max_contrib_credit)
    credit_amount = capped_contribution * rate

    print("---------------------------------")
    print("Qualifying Contrib.:", round(capped_contribution, 2))
    print("Credit Rate:", round(rate * 100, 1), "%")
    print("Estimated 2025 Credit (Nonrefundable):")
    print("$", round(credit_amount, 2))

savers_calc()