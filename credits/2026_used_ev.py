# 2025 Previously Owned Clean Vehicle Credit
# Max $4,000 (30% of sale price, limited to $4,000)
# Price limit: $25,000. MAGI limit: $150k MFJ / $112.5k HOH / $75k Other

def used_ev_calc():
    """Calculates the estimated 2025 Used Clean Vehicle Credit."""
    print("--- 2025 Used Clean Vehicle Credit ---")
    
    try:
        magi = float(input("Enter MAGI: "))
        sale_price = float(input("Sale Price ($25k max): "))
        filing_status = input("Status (MFJ/HOH/OTH): ").upper()
    except ValueError:
        print("Invalid input.")
        return

    # 1. Check Price Limit (Hard Stop)
    if sale_price > 25000.0:
        print("Price must be $25k or less.")
        print("Estimated 2025 Credit: $0")
        return
        
    # 2. Check AGI Limit
    if filing_status == "MFJ":
        agi_limit = 150000
    elif filing_status == "HOH":
        agi_limit = 112500
    else:
        agi_limit = 75000
    
    if magi > agi_limit:
        print("AGI exceeds the limit.")
        print("Estimated 2025 Credit: $0")
        return

    # 3. Calculate Credit Amount
    credit_amount = min(sale_price * 0.30, 4000.0)

    print("---------------------------------")
    print("Estimated 2025 Used EV Credit (Nonrefundable):")
    print("$", round(credit_amount, 2))

used_ev_calc()