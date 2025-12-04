# 2025 New Clean Vehicle Tax Credit
# Max $7,500 (composed of two $3,750 parts)
# MAGI limit: $300k MFJ / $225k HOH / $150k Other

def new_ev_calc():
    """Calculates the estimated 2025 New Clean Vehicle Credit."""
    print("--- 2025 New Clean Vehicle Credit ---")
    
    try:
        magi = float(input("Enter MAGI: "))
        is_na_assembly = input("NA Assembly? (Y/N): ").upper()
        minerals_met = input("Minerals Met? (Y/N): ").upper()
        components_met = input("Components Met? (Y/N): ").upper()
        filing_status = input("Status (MFJ/HOH/OTH): ").upper()
    except ValueError:
        print("Invalid input.")
        return

    # 1. Check AGI Limit
    if filing_status == "MFJ":
        agi_limit = 300000
    elif filing_status == "HOH":
        agi_limit = 225000
    else:
        agi_limit = 150000
    
    if magi > agi_limit:
        print("AGI exceeds the limit.")
        return

    # 2. Check Assembly Requirement (Hard Stop)
    if is_na_assembly != "Y":
        print("Must be NA assembled.")
        print("Estimated 2025 Credit: $0")
        return

    # 3. Calculate Credit Amount (up to $7,500)
    credit_amount = 0.0
    
    if minerals_met == "Y":
        credit_amount += 3750.0
        
    if components_met == "Y":
        credit_amount += 3750.0

    print("---------------------------------")
    print("Estimated 2025 New EV Credit (Nonrefundable):")
    print("$", round(credit_amount, 2))

new_ev_calc()