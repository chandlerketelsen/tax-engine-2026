# 2025 District of Columbia First-Time Homebuyer Credit (Federal)
# Max $5,000 credit for buying a home in D.C.
# Phase-out begins at $90k (S/HOH) / $130k (MFJ) (Simplified)

def dc_home_calc():
    """Calculates the estimated 2025 DC First-Time Homebuyer Credit."""
    print("--- 2025 DC First-Time Homebuyer Credit ---")
    
    try:
        magi = float(input("Enter MAGI: "))
        filing_status = input("Status (MFJ/OTH): ").upper()
    except ValueError:
        print("Invalid input.")
        return

    max_credit = 5000.0
    
    # 1. Determine phase-out thresholds (approximate)
    if filing_status == "MFJ":
        phase_start = 130000.0
        phase_end = 150000.0
    else: # Single, HOH, MFS
        phase_start = 90000.0
        phase_end = 110000.0

    credit_amount = max_credit
    
    # 2. Apply income phase-out
    if magi >= phase_end:
        credit_amount = 0.0
    elif magi > phase_start:
        phase_range = phase_end - phase_start
        reduction_ratio = (magi - phase_start) / phase_range
        credit_amount = max_credit * (1.0 - reduction_ratio)
        
    print("---------------------------------")
    print("Estimated 2025 DC Homebuyer Credit (Nonrefundable):")
    print("$", round(credit_amount, 2))

dc_home_calc()