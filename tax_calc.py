# 2025 Federal Tax Liability Calculator (Pre-Credits)
# All data is official 2025 inflation-adjusted values.

# 1. HARDCODED 2025 TAX DATA (Standard Deduction)
DEDUCTIONS = {
    "SINGLE": 14600,
    "MFJ": 29200,
    "HOH": 21900,
    "MFS": 14600
}

# 2. HARDCODED 2025 TAX DATA (Brackets based on 2025 indexing)
# Keys: r=Rate, t=Threshold (start of the bracket)
BRACKETS = {
    "SINGLE": [
      {"r": 0.10, "t": 0},          # Up to $11,600
      {"r": 0.12, "t": 11600},       # Up to $47,150
      {"r": 0.22, "t": 47150},       # Up to $100,525
      {"r": 0.24, "t": 100525},      # Up to $191,950
      {"r": 0.32, "t": 191950},      # Up to $243,750
      {"r": 0.35, "t": 243750},      # Up to $609,350
      {"r": 0.37, "t": 609350}       # Over $609,350
    ],
    "MFJ": [
      {"r": 0.10, "t": 0},          # Up to $23,200
      {"r": 0.12, "t": 23200},       # Up to $94,300
      {"r": 0.22, "t": 94300},       # Up to $201,050
      {"r": 0.24, "t": 201050},      # Up to $383900
      {"r": 0.32, "t": 383900},      # Up to $487500
      {"r": 0.35, "t": 487500},      # Up to $731200
      {"r": 0.37, "t": 731200}       # Over $731,200
    ],
    "HOH": [
      {"r": 0.10, "t": 0},          # Up to $16,550
      {"r": 0.12, "t": 16550},       # Up to $63,200
      {"r": 0.22, "t": 63200},       # Up to $100,500
      {"r": 0.24, "t": 100500},      # Up to $191,900
      {"r": 0.32, "t": 191900},      # Up to $243,700
      {"r": 0.35, "t": 243700},      # Up to $609,350
      {"r": 0.37, "t": 609350}       # Over $609,350
    ],
    "MFS": [
      {"r": 0.10, "t": 0},          # Up to $11,600
      {"r": 0.12, "t": 11600},       # Up to $47,150
      {"r": 0.22, "t": 47150},       # Up to $100,525
      {"r": 0.24, "t": 100525},      # Up to $191,950
      {"r": 0.32, "t": 191950},      # Up to $243,750
      {"r": 0.35, "t": 243750},      # Up to $365600
      {"r": 0.37, "t": 365600}       # Over $365,600
    ]
}

def gross_tax_calc(tax_inc, status):
    """Calculates gross federal income tax."""
    tax_brackets = BRACKETS.get(status)
    if not tax_brackets:
        return 0.0

    tax_due = 0.0
    
    # Sort brackets by threshold 't' for safety
    tax_brackets.sort(key=lambda x: x['t'])

    for i in range(len(tax_brackets)):
        bracket = tax_brackets[i]
        rate = bracket['r']
        threshold = bracket['t']
        
        # Determine the upper limit of the current bracket
        if i + 1 < len(tax_brackets):
            top_limit = tax_brackets[i+1]['t']
        else:
            top_limit = float('inf')

        # Check if any income falls into this bracket
        if tax_inc > threshold:
            # Amount of income taxed at this rate
            income_in_bracket = min(tax_inc, top_limit) - threshold
            tax_due += income_in_bracket * rate
            
    return tax_due

def run_calc():
    """Main function to run the tax calculation process."""
    print("--- 2025 Tax Liability ---")
    
    # 1. Get Inputs (short prompts)
    try:
        g_inc = float(input("Gross Income: "))
        adj = float(input("Adjustments: "))
        s_in = input("Status (S/M/H/F): ").upper()
        
        # Map input to full status string
        status_map = {"S": "SINGLE", "M": "MFJ", "H": "HOH", "F": "MFS"}
        status = status_map.get(s_in, "SINGLE")
            
    except ValueError:
        print("Invalid number.")
        return
        
    # 2. AGI
    agi = g_inc - adj
    
    # 3. Taxable Income (using Standard Deduction only)
    deduction = DEDUCTIONS.get(status, 0)
    taxable_inc = max(0.0, agi - deduction)
    
    # 4. Gross Tax Liability
    gross_tax_liab = gross_tax_calc(taxable_inc, status)
    
    # 5. Display Results
    print("\n--- Summary ---")
    print(f"AGI: {round(agi, 0)}")
    print(f"Deduction: {round(deduction, 0)}")
    print(f"Taxable: {round(taxable_inc, 0)}")
    print("-----------------")
    print(f"Gross Tax: ${round(gross_tax_liab, 2)}")

run_calc()