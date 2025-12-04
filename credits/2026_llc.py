# 2025 Lifetime Learning Credit (LLC)
# Max $2,000 per return (20% of first $10,000 in expenses)
# Phase-out begins at $160k (MFJ) / $80k (Other)

def llc_calc():
    """Calculates the estimated 2025 Lifetime Learning Credit."""
    print("--- 2025 Lifetime Learning Credit ---")
    
    try:
        agi = float(input("Enter Mod. AGI: "))
        expenses = float(input("Qual. Exp. ($10k max): "))
        filing_status = input("Status (MFJ/OTH): ").upper()
    except ValueError:
        print("Invalid input.")
        return

    # 1. Calculate maximum pre-phase-out credit
    capped_expenses = min(expenses, 10000.0)
    max_credit = capped_expenses * 0.20
    
    # Max credit is strictly $2,000
    max_credit = min(max_credit, 2000.0)

    # 2. Apply income phase-out (simplified phase-out ranges)
    if filing_status == "MFJ":
        phase_start = 160000
        phase_end = 180000
    else:
        phase_start = 80000
        phase_end = 90000

    credit_amount = max_credit
    
    if agi > phase_end:
        credit_amount = 0.0
    elif agi > phase_start:
        phase_range = phase_end - phase_start
        reduction_ratio = (agi - phase_start) / phase_range
        credit_amount = max_credit * (1.0 - reduction_ratio)
        
    print("---------------------------------")
    print("Estimated 2025 LLC:")
    print("$", round(credit_amount, 2))

llc_calc()