# 2025 American Opportunity Tax Credit (AOTC)
# Max $2,500 per student (100% of first $2,000, 25% of next $2,000)
# Phase-out begins at $160k (MFJ) / $80k (Other)

def aotc_calc():
    """Calculates the estimated 2025 American Opportunity Tax Credit."""
    print("--- 2025 American Opportunity Tax Credit ---")
    
    try:
        agi = float(input("Enter Mod. AGI: "))
        expenses = float(input("Qual. Edu. Exp.: "))
        filing_status = input("Status (MFJ/OTH): ").upper()
    except ValueError:
        print("Invalid input.")
        return

    # 1. Calculate maximum pre-phase-out credit
    credit_calc = 0.0
    
    # 100% of the first $2,000
    credit_calc += min(expenses, 2000.0)
    remaining_expenses = max(0.0, expenses - 2000.0)
    
    # 25% of the next $2,000 (up to $4,000 total expenses)
    credit_calc += min(remaining_expenses, 2000.0) * 0.25
    
    max_credit = min(credit_calc, 2500.0)

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
    print("Estimated 2025 AOTC:")
    print("$", round(credit_amount, 2))
    print("Up to $1,000 may be refundable.")

aotc_calc()