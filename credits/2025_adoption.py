# 2025 Adoption Credit
# Max $16,840 per eligible child (Indexed 2025)
# MAGI phase-out begins at $252,520 (Indexed 2025)

def adoption_calc():
    """Calculates the estimated 2025 Adoption Credit."""
    print("--- 2025 Adoption Credit ---")
    
    try:
        magi = float(input("Enter MAGI: "))
        qual_expenses = float(input("Qual. Expenses: "))
        is_special_needs = input("Special Needs? (Y/N): ").upper()
    except ValueError:
        print("Invalid input.")
        return

    # 2025 Indexed Limits
    max_credit_limit = 16840.0
    
    # 1. Determine maximum pre-phase-out credit
    if is_special_needs == "Y":
        max_credit = max_credit_limit
    else:
        max_credit = min(qual_expenses, max_credit_limit)

    # 2. Apply income phase-out (2025 Indexed Ranges)
    phase_start = 252520.0
    phase_end = 292520.0 # $40k phase-out range
    credit_amount = max_credit

    if magi >= phase_end:
        credit_amount = 0.0
    elif magi > phase_start:
        phase_range = phase_end - phase_start
        reduction_ratio = (magi - phase_start) / phase_range
        credit_amount = max_credit * (1.0 - reduction_ratio)
    
    print("---------------------------------")
    print("Estimated 2025 Adoption Credit (Nonrefundable):")
    print("$", round(credit_amount, 2))

adoption_calc()