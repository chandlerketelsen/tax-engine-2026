# 2025 Child Tax Credit (CTC) Calculation
# Max $2,200 per child, up to $1,700 refundable
# Income phase-out begins at $400k (MFJ) or $200k (All others)

def ctc_calc():
    """Calculates the estimated 2025 Child Tax Credit."""
    print("--- 2025 Child Tax Credit ---")
    
    # Get user inputs
    try:
        agi = float(input("Enter Mod. AGI: "))
        num_children = int(input("Children (<17): "))
        filing_status = input("Status (MFJ/OTH): ").upper()
    except ValueError:
        print("Invalid input. Please enter numbers for AGI/children.")
        return

    max_credit_per_child = 2200
    max_total_credit = num_children * max_credit_per_child
    
    # Determine phase-out threshold
    if filing_status == "MFJ":
        threshold = 400000
    else:
        threshold = 200000

    credit_amount = max_total_credit

    # Phase-out calculation (simplified: credit reduced by $50 for every $1,000 over threshold)
    if agi > threshold:
        phase_out_amount = max(0, agi - threshold)
        reduction_per_1000 = 50.0
        reduction = (phase_out_amount / 1000.0) * reduction_per_1000
        
        credit_amount = max(0, max_total_credit - reduction)

    print("---------------------------------")
    print("Estimated 2025 CTC:")
    print("$", round(credit_amount, 2))

ctc_calc()