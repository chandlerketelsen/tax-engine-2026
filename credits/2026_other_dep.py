# 2025 Credit for Other Dependents (ODC)
# Max $500 per qualifying dependent (non-refundable)

def odc_calc():
    """Calculates the estimated 2025 Credit for Other Dependents."""
    print("--- 2025 Credit for Other Dependents ---")
    
    try:
        agi = float(input("Enter Mod. AGI: "))
        num_dependents = int(input("Other Dependents: "))
        filing_status = input("Status (MFJ/OTH): ").upper()
    except ValueError:
        print("Invalid input.")
        return

    max_credit_per_dependent = 500
    max_total_credit = num_dependents * max_credit_per_dependent
    
    # Phase-out thresholds
    if filing_status == "MFJ":
        threshold = 400000
    else:
        threshold = 200000

    credit_amount = max_total_credit

    # Phase-out calculation (credit reduced by $50 for every $1,000 over threshold)
    if agi > threshold:
        phase_out_amount = max(0, agi - threshold)
        reduction_per_1000 = 50.0
        reduction = (phase_out_amount / 1000.0) * reduction_per_1000
        
        credit_amount = max(0, max_total_credit - reduction)
        
    print("---------------------------------")
    print("Estimated 2025 ODC (Nonrefundable):")
    print("$", round(credit_amount, 2))

odc_calc()